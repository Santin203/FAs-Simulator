# By Santiago Jimenez
# Theory of Automata
# Project 1

import json
from classes import *
from functions import *       


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
        
        #type = 0
        
        # Accessing the 'delta' array and checking if 'next_state' is a list
        # for transition in data['delta']:
        #     if isinstance(transition['next_state'], list) or transition["input"] == "<EPSILON>":
        #         type = 1
        #         break

        # Create and configure the DFA from the given file
        fa = FA()
        fa = create_fa_json(data, fa)
        print("FA loaded successfully.")
        fa.print_fa()
        
    elif command.startswith("process -input=") and "-verbose" in command:
        input_string = command.split("=")[1].split(" ")[0].strip('"')
        try:
            fa.verbose_mode(input_string)
        except:
            print("FA not loaded.")
            
    elif command.startswith("process -input="):
        input_string = command.split("=")[1].strip('"')
        try:
            fa.check_string(input_string)
        except:
            print("FA not loaded.")
    
    elif command.startswith("regex -input="):
        regex = command.split("=")[1]
        fa = FA()
        star_fa(regex, fa)
        #plus_fa(regex, fa)
        #fa_from_regex(regex, fa)
        
        fa.print_fa()
    
    elif command == "print":
        try:
            fa.print_fa()
        except:
            print("FA not loaded.")
    
    else:
        print("Invalid command.")