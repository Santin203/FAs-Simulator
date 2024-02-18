# By Santiago Jimenez
# Theory of Automata
# Project 1

from classes import *
import json
import os

# Array with the regex types
regex_types = ["*", "+", "?", "^", "$", "(", ")"]

def create_fa_json(data, fa):

    fa.add_states(data["states"])
    fa.add_alphabet(data["alphabet"])
    fa.add_transition(data["delta"])
    fa.set_start_state(data["start_state"])
    fa.set_accept_states(data["accept_states"])
    return fa

def get_data(command):
    os.system('cls' if os.name == 'nt' else 'clear')

    file_path = r"" + command.split("=")[1].strip('"')

    try:
        f = open(file_path)
    except:
        print("File not found.")
        return None

    data = json.load(f)
    return data
    
# Create and configure the FA from the given regex
def fa_from_regex(regex):
    
    #print("Regex: " + regex)
    
    # Set variables
    fas_list = []
    unused_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
                      "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", 
                      "w", "x", "y", "z"]
    used_letters = ["q"]
    symbols = []
    inside_parenthesis = 0

    # Parse the regex
    for i, symbol in enumerate(regex):
        new_input = ""
        if symbol == "*" and inside_parenthesis == 0:
            symbols.pop()  # Remove the last symbol from the list
            
            # If there are symbols in the list, create a FA from them
            # Handle sequences of symbols
            if len(symbols) > 0:
                temp_fa = FA()
                # Get a string from all the symbols in the list
                for s in symbols:
                    new_input += s
                caret_and_dollar_fa(new_input, temp_fa)
                fas_list.append(temp_fa)  # Add the FA to the list
                symbols = []
            
            # Create a FA from the last symbol
            new_input = regex[i-1]  # Get the symbol before the "*"
            if new_input == ")":
                continue
            
            temp_fa = FA()
            star_fa(new_input, temp_fa)
            fas_list.append(temp_fa)  # Add the FA to the list of FAs
            

            
        elif symbol == "+" and inside_parenthesis == 0:
            
            symbols.pop()  # Remove the last symbol from the list
            
            # If there are symbols in the list, create a FA from them
            # Handle sequences of symbols
            if len(symbols) > 0:
                temp_fa = FA()
                # Get a string from all the symbols in the list
                for s in symbols:
                    new_input += s
                caret_and_dollar_fa(new_input, temp_fa)
                fas_list.append(temp_fa)  # Add the FA to the list
                symbols = []
            
            # Create a FA from the last symbol  
            new_input = regex[i-1]
            temp_fa = FA()
            plus_fa(new_input, temp_fa)
            fas_list.append(temp_fa)  # Add the FA to the list
            
        elif symbol == "?" and inside_parenthesis == 0:
            symbols.pop()  # Remove the last symbol from the list
            
            # If there are symbols in the list, create a FA from them
            # Handle sequences of symbols
            if len(symbols) > 0:
                temp_fa = FA()
                # Get a string from all the symbols in the list
                for s in symbols:
                    new_input += s
                caret_and_dollar_fa(new_input, temp_fa)
                fas_list.append(temp_fa)  # Add the FA to the list
                symbols = []
            
            # Create a FA from the last symbol  
            new_input = regex[i-1]
            temp_fa = FA()
            question_mark_fa(new_input, temp_fa)
            fas_list.append(temp_fa)  # Add the FA to the list
            
        elif symbol == "^":
            # list symbols handles this cases
            continue
            
        elif symbol == "$":
            # list symbols handles this cases
            continue

        elif symbol == "(":
            
            # If there are symbols in the list, create a FA from them
            # Handle sequences of symbols
            if len(symbols) > 0:
                temp_fa = FA()
                # Get a string from all the symbols in the list
                for s in symbols:
                    new_input += s
                caret_and_dollar_fa(new_input, temp_fa)
                fas_list.append(temp_fa)  # Add the FA to the list
                symbols = []
                
            # Get the substring inside the parenthesis
            substring = ""
            j = i + 1
            while regex[j] != ")":
                substring += regex[j]
                j += 1

            print("Substring: " + substring)
            # temp_fa = FA()
            # temp_fa = fa_from_regex(substring)
            if regex[j+1] == "*":
                temp_fa = FA()
                star_fa(substring, temp_fa)
            elif regex[j+1] == "+":
                
                temp_fa = FA()
                plus_fa(substring, temp_fa)
            elif regex[j+1] == "?":
                temp_fa = FA()
                question_mark_fa(substring, temp_fa)
            elif regex[j+1] == "$":
                temp_fa = FA()
                caret_and_dollar_fa(substring, temp_fa)
            else:
                print("Error")
            inside_parenthesis = len(substring)
            fas_list.append(temp_fa)
            symbols = []
            
        else:
            # Skip the symbol if already handled
            if inside_parenthesis > 0:
                inside_parenthesis -= 1
                continue
            
            # Add the symbol to the list
            symbols.append(symbol)

    # If there are remaining symbols in the list, create a FA from them       
    if len(symbols) > 0:
        temp_fa = FA()
        # Get a string from all the symbols in the list
        for s in symbols:
            new_input += s
        caret_and_dollar_fa(new_input, temp_fa)
        fas_list.append(temp_fa)  # Add the FA to the list
        symbols = []            
                
         
    for i in range(len(fas_list) - 1):
        
        # Make each FA use a different letter  
        for letter in unused_letters:
            if letter not in used_letters:
                new_data = replace_q(fas_list[i+1], letter)
                used_letters.append(letter)
                break
        
        # Concatenate the FAs    
        fas_list[i+1] = concatenate_fa(fas_list[i], new_data)
    
    # The last FA in the list is the final FA   
    fa = fas_list[-1]
    
    return fa

# Function to replace 'q' with another letter
def replace_q(data, new_letter):
    
    # Make a copy of the FA
    new_fa = FA()
    new_fa.copy_fa(data)
    
    # Replace 'q' in states
    new_fa.states = [state.replace('q', new_letter) for state in data.states]

    # Replace 'q' in delta
    for transition in new_fa.transitions:
        transition["state"] = transition["state"].replace('q', new_letter)
        transition["next_state"] = transition["next_state"].replace('q', new_letter)

    # Replace 'q' in start_state and accept_states
    new_fa.start_state = new_fa.start_state.replace('q', new_letter)
    new_fa.accept_states = [state.replace('q', new_letter) for state in data.accept_states]

    return new_fa

# Function to concatenate two FAs
def concatenate_fa(fa1, fa2):
    # Initialize the new FA
    fa = FA()
    
    # Set the alphabet
    for symbol in fa1.alphabet:
        if symbol not in fa.alphabet and symbol != "<EPSILON>":
            fa.add_alphabet(symbol)
            
        if "<EPSILON>" not in fa.alphabet:
            fa.add_alphabet(["<EPSILON>"])
    
    for symbol in fa2.alphabet:
        if symbol not in fa.alphabet and symbol != "<EPSILON>":
            fa.add_alphabet(symbol)
        
        if "<EPSILON>" not in fa.alphabet:
            fa.add_alphabet(["<EPSILON>"])
    
    # Add the states
    fa.add_states(fa1.states)
    fa.add_states(fa2.states)
    
    # Set the initial state      
    fa.set_start_state(fa1.start_state)

    # Set the final states
    fa.set_accept_states(fa1.accept_states)
    fa.set_accept_states(fa2.accept_states)
    
    # Add the transitions from the first FA
    fa.add_transition(fa1.transitions)
    
    # Make <EPSILON> transitions from the final states of fa1 to the start state of fa2
    for state in fa1.accept_states:
        fa.add_transition([{"state": state, "input": "<EPSILON>", "next_state": fa2.start_state}])
        if "<EPSILON>" not in fa.alphabet:
            fa.add_alphabet(["<EPSILON>"])
    
    # Add the transitions from the second FA
    fa.add_transition(fa2.transitions)
    
    return fa