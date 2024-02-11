# By Santiago Jimenez
# Theory of Automata
# Project 1

import json
from classes import *
from functions import *       
import os


# Command line interface
while True:
    command = input(">> ")
    
    # Parse the command
    if command == "exit":
        break
    
    elif command.startswith("load -input="):
        os.system('cls' if os.name == 'nt' else 'clear')

        file_path = r"" + command.split("=")[1].strip('"')

        try:
            f = open(file_path)
        except:
            print("File not found.")
            continue

        data = json.load(f)

        # Create and configure the DFA from the given file
        fa = FA()
        fa = create_fa_json(data, fa)
        sts = fa.check_fa_consistency()
        if sts:
            print("FA loaded successfully.")
            fa.print_fa()
        else:
            print("Invalid FA.")
        
    elif command.startswith("process -input=") and "-verbose" in command:
        input_string = command.split("=")[1].split(" ")[0].strip('"')
        try:
            status = fa.verbose_mode(fa.start_state,input_string)
            if status:
                print("String accepted")
            else:
                print("String not accepted")
        except:
            print("FA not loaded.")
            
    elif command.startswith("process -input="):
        input_string = command.split("=")[1].strip('"')
        try:
            fa.check_string(fa.start_state, input_string)
        except:
            print("FA not loaded.")
    
    elif command.startswith("regex -input="):
        regex = command.split("=")[1]
        fa = FA()
        #star_fa(regex, fa)
        #plus_fa(regex, fa)
        #question_mark_fa(regex, fa)
        #caret_and_dollar_fa(regex, fa)
        
        fa = fa_from_regex(regex)
        
        sts = fa.check_fa_consistency()
        if sts:
            print("FA loaded successfully.")
            fa.print_fa()
        else:
            print("Invalid FA.")
        
        #fa.print_fa()
    
    elif command == "print":
        try:
            fa.print_fa()
        except:
            print("FA not loaded.")
    
    else:
        print("Invalid command.")