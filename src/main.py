import json


class DFA:
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
        # Set the start state of the DFA
        self.start_state = state

    def set_accept_states(self, states):
        # Set the accept states of the DFA
        self.accept_states = states

    def check_string(self, input_string):
        # Check if the input string is accepted by the DFA
        current_state = self.start_state
        for symbol in input_string:
            next_state = ""
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
            
class NFA:
    def __init__(self):
        # Initialize the NFA
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.start_state = ""
        self.accept_states = []

    def add_states(self, states):
        # Add the states to the NFA
        for state in states:
            self.states.append(state)
            
    def add_alphabet(self, alphabet):
        # Add the alphabet to the NFA
        for symbol in alphabet:
            self.alphabet.append(symbol)

    def add_transition(self, delta):
        # Add the transitions to the NFA
        for transition in delta:
            self.transitions.append(transition)
            
    def set_start_state(self, state):
        # Set the start state of the NFA
        self.start_state = state

    def set_accept_states(self, states):
        # Set the accept states of the NFA
        self.accept_states = states

    # PENDING IMPLEMENTATION
    def check_string(self, input_string):
        # Check if the input string is accepted by the NFA
        current_state = self.start_state
        for symbol in input_string:
            next_state = ""
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
            
def create_fa_json(data):

    fa.add_states(data["states"])
    fa.add_alphabet(data["alphabet"])
    fa.add_transition(data["delta"])
    fa.set_start_state(data["start_state"])
    fa.set_accept_states(data["accept_states"])
    return fa

def print_fa(fa):
    # Print the DFA
    print("Q = {", end="")
    for i, state in enumerate(fa.states):
        if i != 0:
            print(", ", end="")
        print(state, end="")
    print("}\n")
    
    print("Sigma = {", end="")
    for i, symbol in enumerate(fa.alphabet):
        if i != 0:
            print(", ", end="")
        print(symbol, end="")
    print("}\n")
    
    print("delta = {")
    for transition in fa.transitions:
        print("    (" + transition["state"] + ", " + transition["input"] + ") -> ", end="")
        if isinstance(transition["next_state"], list):
            print(", ".join(transition["next_state"]))
        else:
            print(transition["next_state"])
    print("}\n")
    
    print("Initial state = " + fa.start_state)
    
    print("F = {", end="")
    for i, state in enumerate(fa.accept_states):
        if i != 0:
            print(", ", end="")
        print(state, end="")
    print("}")

# Create and configure the DFA from the given file
#dfa = create_dfa(r"C:\Users\Casas\OneDrive - Texas Tech University\Documents\Texas Tech\Spring 2024\CS-3383\Projects\Project 1\src\input1.json")

# Command line interface
while True:
    command = input(">> ")
    
    # Parse the command
    if command == "exit":
        break
    
    elif command.startswith("load -input="):
        file_path = r"" + command.split("=")[1].strip('"')
        
        f = open(file_path)
        data = json.load(f)
        
        type = 0
        
        # Accessing the 'delta' array and checking if 'next_state' is a list
        for transition in data['delta']:
            if isinstance(transition['next_state'], list) or transition["input"] == "<EPSILON>":
                type = 1
                break
                
        
        if type == 1:
            # Create and configure the NFA from the given file
            fa = NFA()
            fa = create_fa_json(data)
            print("NFA loaded successfully.")
            
            
        else:
            # Create and configure the DFA from the given file
            fa = DFA()
            fa = create_fa_json(data)
            print("DFA loaded successfully.")
    
    elif command.startswith("process -input="):
        input_string = command.split("=")[1].strip('"')
        try:
            fa.check_string(input_string)
        except:
            print("DFA not loaded.")
    
    elif command.startswith("process -input=") and "-verbose" in command:
        input_string = command.split("=")[1].split(" ")[0]
        try:
            fa.check_string(input_string)
            print("Verbose mode enabled.")
        except:
            print("DFA not loaded.")
    
    elif command.startswith("regex -input="):
        regex = command.split("=")[1]
        # Perform regex matching here
        print("Regex matching not implemented yet.")
    
    elif command == "print":
        try:
            print_fa(fa)
        except:
            print("FA not loaded.")
    
    else:
        print("Invalid command.")
    
    
    
    

# Check if the input string is accepted by the DFA
#dfa.check_string("10101")
