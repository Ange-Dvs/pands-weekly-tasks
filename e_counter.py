# e_counter.py
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author: Angela Davis

#------------------------------------------------------------------------------------------------------------------------#
# Brainstorming: 
# As starting point - Have multiple text files w/ various numbers of e characters already existing to test with > done
# Create a function for counting the e's in the chosen file > done
# Assuming the file will be in the current directory/folder, input is used to take in the filename from the user > done
# create error catching for:
        # 1. blank feedback from user > done
        # 2. incorrect/non existing filename > done
        # 3. asked for a file which is not a text file > done
#------------------------------------------------------------------------------------------------------------------------#

# Assumptions: 
# File the user will enter is using the relative path name if the same directory as the program or full path name if the file exists in another location, program should be able to handle both 
# E should be counted whether it is uppercase or lowercase
# Since the file is being entered in the command line when the user is triggering the program it is assumed that error handly should end the program without retry and print a human readable error for the user 

#------------------------------------------------------------------------------------------------------------------------#


import os.path
import sys 

FILENAME = sys.argv[1]
file_title, file_extension = os.path.splitext(FILENAME.lower()) # .lower() is used in case the user types the filetype in all caps to convert to lower case for the error handling below

def count_E(): # this fuction takes in the file defined as the FILENAME above. Reads the content and counts the e's in the file.
    try: 
        with open(FILENAME) as f: # file is first attemped to be opened as "f" using the input from the user
            full_file = f.read()  # the content of the file is set as variable full_file
            number_of_E = full_file.lower().count("e") # lower() is used to convert the file to all lowercase and then count the e's to ensure no uppercase e's are left out
            print (f"There were {number_of_E} e's") # The number of Es are printed for the user
        
    except: # if the file cannot be opened using the input from the user 
        if FILENAME == "": # first we check if the feedback from the user was blank
            print("No filename has been entered.\nProgram exited.")

        elif file_extension != ".txt":
            print(f"The filename you have entered indicates your file is a {file_extension} file.\n This program only accepts .txt files.\nProgram exited.")
            
        else: 
            print("Filename provided does not exist.\nProgram exited.") # else we assume the users input was not matching a filename that exists  

count_E() # function is called