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

    def set_accept_states(self, states):
        # Set the accept states of the FA
        self.accept_states = states

    def check_string(self, input_string):
        if input_string == "":
            print("\nProcessing string: <EMPTY>\n")
        else:
            print("\nProcessing string: " + input_string + "\n")
            
        # Check if the input string is accepted by the FA
        current_state = self.start_state
        for symbol in input_string:
            next_state = ""
            new_input = ""
            for transition in self.transitions:
                if transition["state"] == current_state and transition["input"] == symbol:
                    next_state = transition["next_state"]
                    break
            if next_state is None:
                return False
            current_state = next_state
            
        if current_state in self.accept_states:
            print("String accepted")
        else:
            print("String not accepted")
            
    def verbose_mode(self, current_state, input_string):
        #ADD <EPSILON> SUPPORT
        if input_string == "":
            #print("\nProcessing string: <EMPTY>\n")
            pass
        else:
            #print("\nProcessing string: " + input_string + "\n")
        
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
                    if transition["state"] == current_state and transition["input"] == "<EPSILON>":
                        next_state = transition["next_state"]
                        print(current_state + " -- " + "<EPSILON>" + " --> " + next_state)
                        status = self.verbose_mode(next_state, input_string)
                        if status:
                            return True
            
                if next_state is None:
                    return False
                current_state = next_state
            
        if current_state in self.accept_states:
            return True
        else:
            #print("String not accepted\n")
            #FINISH IMPLEMENTING EPSILON
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
        symbols = []
        state = 0
        print("Regex: " + regex)
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in symbols):
                fa.add_alphabet(symbol)
                symbols.append(symbol)
                
        fa.add_states(["q0"])
        fa.set_start_state("q0")
        
        #FIX
        if len(symbols) <= 1:
            fa.add_transition([{"state": "q" + str(state), "input": symbols[state], "next_state": "q" + str(state)}])
            fa.set_accept_states(["q" + str(state)])
        else:
            for symbol in symbols:
                fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
            fa.set_accept_states(["q" + str(state-len(symbols))])
            
            
class plus_fa:
    def __init__(self, regex, fa):
        # Initialize the FA
        symbols = []
        state = 0
        print("Regex: " + regex)
        
        # Create and configure the FA from the given regex
        for symbol in regex:
            if (symbol not in regex_types) and (symbol not in symbols):
                fa.add_alphabet(symbol)
                symbols.append(symbol)
                
        fa.add_states(["q0, q1"])
        fa.set_start_state("q0")
        fa.set_accept_states(["q1"])
        
        for symbol in symbols:
            fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state+1)}])
            states += 1
            fa.add_transition([{"state": "q" + str(state), "input": symbol, "next_state": "q" + str(state)}])