# By Santiago Jimenez
# Theory of Automata
# Project 1

from classes import *
from functions import *       
import os

# Clear the console
#os.system('cls' if os.name == 'nt' else 'clear')

# Command line interface
while True:

    command = input(">> ")
    
    # Parse the command

    # Exit the program
    if command == "exit":
        break
    
    # Load a FA from a json
    elif command.startswith("load -input="):

        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Read file and store its data
        data = get_data(command)

        # Create and configure the DFA
        fa = FA()
        fa = create_fa_json(data, fa)

        # Check if the FA is consistent
        sts = fa.check_fa_consistency()
        if sts:
            print("FA loaded successfully.")

            # Print the FA if it is valid
            fa.print_fa()

        else:
            print("Invalid FA.")
    
    # Process a string in verbose mode
    elif command.startswith("process -input=") and "-verbose" in command:

        # Parse the input string
        input_string = command.split("=")[1].split(" ")[0].strip('"')

        try:
            # Check if the string is accepted
            sts = fa.verbose_mode(fa.start_state,input_string)
            if sts:
                print("String accepted")
            else:
                print("String not accepted")
        
        # Error handling
        except:
            print("FA not loaded.")

    # Process a string        
    elif command.startswith("process -input="):

        # Parse the input string
        input_string = command.split("=")[1].strip('"')

        try:
            # Check if the string is accepted
            sts = fa.check_string(fa.start_state, input_string)
            if sts:
                print("String accepted")
            else:
                print("String not accepted")

        # Error handling
        except:
            print("FA not loaded.")
    
    # Create a FA from a regex
    elif command.startswith("regex -input="):

        # Get the input regex
        regex = command.split("=")[1]

        # Create and configure the FA from the given regex
        fa = FA()
        fa = fa_from_regex(regex)
        
        # Check if the FA is consistent
        sts = fa.check_fa_consistency()
        if sts:
            print("FA loaded successfully.")

            # Print the FA if it is valid
            fa.print_fa()
        else:
            print("Invalid FA.")

    # Print the FA
    elif command == "print":
        try:
            fa.print_fa()
        except:
            print("FA not loaded.")
    
    else:
        print("Invalid command.")