from classes import *

def create_fa_json(data, fa):

    fa.add_states(data["states"])
    fa.add_alphabet(data["alphabet"])
    fa.add_transition(data["delta"])
    fa.set_start_state(data["start_state"])
    fa.set_accept_states(data["accept_states"])
    return fa
    
    

def fa_from_regex(regex, fa):
    # Create and configure the FA from the given regex
    num_states = 0
    
    print("Regex: " + regex)

    #fix, it is adding algo symbols (star, dollar sign....)
    #dfa.add_alphabet(regex)
    fa.add_states(["q" + str(num_states)])
    fa.set_start_state("q" + str(num_states))
    
    
    for i in regex:
        if i == "*":
            print("Star")
            
        elif i == "+":
            print("Plus")
        elif i == "?":
            print("Question mark")
        elif i == "^":
            print("Caret")
        elif i == "$":
            print("Dollar sign")
        elif i == "(":
            print("parenthesis")
        else:
            if regex.index(i)+1 < len(regex) and regex[regex.index(i)+1] == "*":
                fa.add_transition([{"state": "q" + str(num_states), "input": i, "next_state": "q" + str(num_states)}])
                
            else:
                num_states += 1
                fa.add_states(["q" + str(num_states)])
                fa.add_transition([{"state": "q" + str(num_states - 1), "input": i, "next_state": "q" + str(num_states)}])
                
    fa.set_accept_states(["q" + str(num_states)])
    
    return fa