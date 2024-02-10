regex_types = ["*", "+", "?", "^", "$", "(", ")"]

class FA:
    def __init__(self):
        # Initialize the DFA
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.start_state = ""
        self.accept_states = []

    def add_states(self, states):
        # Add the states to the DFA
        for state in states:
            self.states.append(state)
            
    def add_alphabet(self, alphabet):
        # Add the alphabet to the DFA
        for symbol in alphabet:
            self.alphabet.append(symbol)

    def add_transition(self, delta):
        # Add the transitions to the DFA
        for transition in delta:
            self.transitions.append(transition)
            
    def set_start_state(self, state):
        # Set the start state of the FA
        self.start_state = state

    def set_accept_states(self, state):
        # append the accept state of the FA
        self.accept_states.append(state)
        #self.accept_states = states
    
    def copy_fa(self, fa):
        self.states = fa.states
        self.alphabet = fa.alphabet
        self.transitions = fa.transitions
        self.start_state = fa.start_state
        self.accept_states = fa.accept_states
    
    def check_fa_consistency(self):
        # Check if the FA is consistent
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

    def check_string(self, input_string):
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
                        status = self.check_string(next_state, new_input)
                        if status:
                            return True
                        else:
                            next_state = ""
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
        print("Regex: " + regex)
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in fa.alphabet):
                fa.add_alphabet(symbol)
                
        fa.add_states(["q0"])
        fa.set_start_state("q0")
        
        if len(regex) <= 1:
            fa.add_transition([{"state": "q" + str(state), "input": fa.alphabet[state], "next_state": "q" + str(state)}])
            fa.set_accept_states("q" + str(state))
        else:
            for i, symbol in enumerate(regex):
                if i == len(regex) - 1:
                    fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": str(fa.start_state)}])
                
                else:
                    fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
                    state += 1
                    fa.add_states(["q" + str(state)])
                
            fa.set_accept_states(fa.start_state)
            
            
class plus_fa:
    def __init__(self, regex, fa):
        # Initialize the FA
        state = 0
        print("Regex: " + regex)
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in fa.alphabet):
                fa.add_alphabet(symbol)
                
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
        
        fa.set_accept_states("q" + str(state))

# Accepts if there is 0 or 1 of the previous symbol        
class question_mark_fa:
    def __init__(self, regex, fa):
        # Initialize the FA
        state = 0
        print("Regex: " + regex)
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in fa.alphabet):
                fa.add_alphabet(symbol)
                
        fa.add_states(["q0"])
        fa.set_start_state("q0")
        fa.set_accept_states("q0")
        
        
        for i, symbol in enumerate(regex):
            if i == len(fa.alphabet) - 1:
                fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
                state += 1
                fa.add_states(["q" + str(state)])
                fa.set_accept_states("q" + str(state))
            
            else:
                fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])  
                state += 1 

class caret_and_dollar_fa:
    def __init__(self, regex, fa):
        # Initialize the FA
        state = 0
        print("Regex: " + regex)
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in fa.alphabet):
                fa.add_alphabet(symbol)
                
        fa.add_states(["q0"])
        fa.set_start_state("q0")
        
        for symbol in regex:
            fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
            state += 1
            fa.add_states(["q" + str(state)])
            
        fa.set_accept_states("q" + str(state))