# By Santiago Jimenez
# Theory of Automata
# Project 1

# Array with the regex types
regex_types = ["*", "+", "?", "^", "$", "(", ")"]

# Class for the Finite Automaton
class FA:
    def __init__(self):
        # Initialize the FA
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.start_state = ""
        self.accept_states = []

    # Add states to the FA
    def add_states(self, states):
        for state in states:
            self.states.append(state)
            
    # Add symbols to the alphabet of the FA
    def add_alphabet(self, alphabet):
        for symbol in alphabet:
            self.alphabet.append(symbol)

    # Add transitions to the FA
    def add_transition(self, delta):
        for transition in delta:
            self.transitions.append(transition)
          
    # Set the start state of the FA  
    def set_start_state(self, state):
        self.start_state = state

    # Set the accept states of the FA
    def set_accept_states(self, state):
        for state in state:
            self.accept_states.append(state)
    
    # Make a copy from another FA
    def copy_fa(self, fa):
        self.states = fa.states
        self.alphabet = fa.alphabet
        self.transitions = fa.transitions
        self.start_state = fa.start_state
        self.accept_states = fa.accept_states
    
    # Check if the FA is consistent/valid
    # This method checks if the start state, the states, the transitions and the accept states are consistent
    def check_fa_consistency(self):
        if self.start_state not in self.states:
            return False
        
        for transition in self.transitions:
            if transition["state"] not in self.states or transition["next_state"] not in self.states:
                return False
            if transition["input"] not in self.alphabet:
                return False
            
        for state in self.accept_states:
            if isinstance(state, list):
                for s in state:
                    if s not in self.states:
                        return False
            else:
                if state not in self.states:
                    return False
        
        return True

    # Check if the input string is accepted by the FA in memory
    def check_string(self, current_state, input_string):
        
        # Do not check transitions if the input string is empty
        if input_string == "":
            pass
        else:    
            for symbol in input_string:
                
                # Check that the string only contains symbols from the alphabet
                if symbol not in self.alphabet:
                    print("Symbol " + symbol + " is not in the alphabet")
                    return False
                
                # Set next_state and new_input (next input string to check after the current symbol is processed)
                next_state = ""
                new_input = input_string[input_string.index(symbol)+1:]
                
                # Go through the transitions to find the next state
                for transition in self.transitions:
                    
                    # If the current state and the current symbol are in the transition, set next_state to the next state ("take the transition" and move to the next state)
                    if transition["state"] == current_state and transition["input"] == symbol:
                        next_state = transition["next_state"]
                        status = self.check_string(next_state, new_input)
                        if status:
                            return True
                        else:
                            # Clear next_state if new_input is not accepted
                            next_state = ""
                    
                    # Check for epsilon transitions
                    if transition["state"] == current_state and transition["input"] == "<EPSILON>":
                        next_state = transition["next_state"]
                        status = self.check_string(next_state, input_string)
                        if status:
                            return True
                        else:
                            return False
            
                if next_state == "":
                    return False
                current_state = next_state
            
   
        if current_state in self.accept_states:
            return True
        else:
            # Check for epsilon transitions before returning False
            for transition in self.transitions:
                if transition["state"] == current_state and transition["input"] == "<EPSILON>":
                    next_state = transition["next_state"]
                    status = self.check_string(next_state, input_string)
                    if status:
                        return True
            return False
            
    def verbose_mode(self, current_state, input_string):
        if input_string == "":
            pass
        else:        
            # Check if the input string is accepted by the FA and print the transitions
            for symbol in input_string:
                if symbol not in self.alphabet:
                    print("Symbol " + symbol + " is not in the alphabet")
                    return False
                next_state = ""
                new_input = input_string[input_string.index(symbol)+1:]
                
                
                for transition in self.transitions:
                        
                    if transition["state"] == current_state and transition["input"] == symbol:
                        next_state = transition["next_state"]
                        print(current_state + " -- " + symbol + " --> " + next_state)
                        status = self.verbose_mode(next_state, new_input)
                        if status:
                            return True
                        else:
                            next_state = ""
                    if transition["state"] == current_state and transition["input"] == "<EPSILON>":
                        next_state = transition["next_state"]
                        print(current_state + " -- " + "<EPSILON>" + " --> " + next_state)
                        status = self.verbose_mode(next_state, input_string)
                        if status:
                            return True
                        else:
                            return False
            
                if next_state == "":
                    return False
                current_state = next_state
            
        if current_state in self.accept_states:
            return True
        else:
            for transition in self.transitions:
                if transition["state"] == current_state and transition["input"] == "<EPSILON>":
                    next_state = transition["next_state"]
                    print(current_state + " -- " + "<EPSILON>" + " --> " + next_state)
                    status = self.verbose_mode(next_state, input_string)
                    if status:
                        return True
            return False

    def print_fa(self):
        # Print the DFA
        print("Q = {", end="")
        for i, state in enumerate(self.states):
            if i != 0:
                print(", ", end="")
            print(state, end="")
        print("}\n")
        
        print("Sigma = {", end="")
        for i, symbol in enumerate(self.alphabet):
            if i != 0:
                print(", ", end="")
            print(symbol, end="")
        print("}\n")
        
        print("delta = {")
        for transition in self.transitions:
            print("    (" + transition["state"] + ", " + transition["input"] + ") -> ", end="")
            if isinstance(transition["next_state"], list):
                print(", ".join(transition["next_state"]))
            else:
                print(transition["next_state"])
        print("}\n")
        
        print("Initial state = " + self.start_state)
        
        print("F = {", end="")
        for i, state in enumerate(self.accept_states):
            if i != 0:
                print(", ", end="")
            print(state, end="")
        print("}")


class star_fa:
    def __init__(self, regex, fa):
        # Initialize the FA
        state = 0
        if regex == "":
            return
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in fa.alphabet):
                fa.add_alphabet(symbol)
        
        for i in regex:
            if i in regex_types:
                regex = regex.replace(i, "")
        
        fa.add_states(["q0"])
        fa.set_start_state("q0")
        
        if len(regex) <= 1:
            fa.add_transition([{"state": "q" + str(state), "input": fa.alphabet[state], "next_state": "q" + str(state)}])
            fa.set_accept_states(["q" + str(state)])
        else:
            for i, symbol in enumerate(regex):
                if i == len(regex) - 1:
                    fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": str(fa.start_state)}])
                
                else:
                    fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
                    state += 1
                    fa.add_states(["q" + str(state)])
                
            fa.set_accept_states([fa.start_state])
            
            
class plus_fa:
    def __init__(self, regex, fa):
        # Initialize the FA
        state = 0
        if regex == "":
            return
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in fa.alphabet):
                fa.add_alphabet(symbol)
                
        for i in regex:
            if i in regex_types:
                regex = regex.replace(i, "")
                
        fa.add_states(["q0"])
        fa.set_start_state("q0")
        

            
        for symbol in regex:
            fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
            state += 1
            fa.add_states(["q" + str(state)])
            
        if len(regex) <= 1:
            fa.add_transition([{"state": "q" + str(state), "input": fa.alphabet[0], "next_state": "q" + str(state)}])
        else:
            fa.add_transition([{"state": "q" + str(state), "input": fa.alphabet[0], "next_state": str(fa.states[1])}])
        
        fa.set_accept_states(["q" + str(state)])

# Accepts if there is 0 or 1 of the previous symbol        
class question_mark_fa:
    def __init__(self, regex, fa):
        # Initialize the FA
        state = 0
        if regex == "":
            return
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in fa.alphabet):
                fa.add_alphabet(symbol)
                
        for i in regex:
            if i in regex_types:
                regex = regex.replace(i, "")
                
        fa.add_states(["q0"])
        fa.set_start_state("q0")
        fa.set_accept_states(["q0"])
        
        
        for i, symbol in enumerate(regex):
            if i == len(fa.alphabet) - 1:
                fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
                state += 1
                fa.add_states(["q" + str(state)])
                fa.set_accept_states(["q" + str(state)])
            
            else:
                fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])  
                state += 1 

class caret_and_dollar_fa:
    def __init__(self, regex, fa):
        # Initialize the FA
        state = 0
        if regex == "":
            return
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in fa.alphabet):
                fa.add_alphabet(symbol)
                
        for i in regex:
            if i in regex_types:
                regex = regex.replace(i, "")
                
        fa.add_states(["q0"])
        fa.set_start_state("q0")
        
        for symbol in regex:
            fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
            state += 1
            fa.add_states(["q" + str(state)])
            
        fa.set_accept_states(["q" + str(state)])