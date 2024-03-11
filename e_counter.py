# e_counter.py
# Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line.
# Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.
# Author: Angela Davis
#------------------------------------------------------------------------------------------------------------------------#
# Assumptions starting: 
# As starting point - Have multiple text files w/ various numbers of e characters already existing to test with > done
# Create a function for counting the e's in the chosen file > done
# Assuming the file will be in the current directory/folder, input is used to take in the filename from the user > done
# create error catching for:
        # 1. blank feedback from user > started
        # 2. incorrect/non existing filename > started
        # 3. asked for a file which is not a text file > to be started
#------------------------------------------------------------------------------------------------------------------------#
# Need to check: 
        # need to check how to determine file type (or are we just expecting user to enter .txt at end) 
        # can we read in a file from a user that is located in a different folder/directory
#------------------------------------------------------------------------------------------------------------------------#

# first version with counting e's in a file already created w/ static file name not taken in from user

import os.path
FILENAME = input("Please enter the filename: ") # this sentences takes the filename in from the user and assigns it to FILENAME

def count_E(): # this fuction takes in the file defined as the FILENAME above. Reads the content and counts the e's in the file.
    try: 
        with open(FILENAME) as f: # file is first attemped to be opened as "f" using the input from the user
            full_file = f.read()  # the content of the file is set as variable full_file
            number_of_E = full_file.count("e") # the count method is used to scan the text and count each e
            return number_of_E # the number of es are then returned from the function
        
    except IOError: # if the file cannot be opened using the input from the user 
        if FILENAME == "": # first we check if the feedback from the user was blank
            print("You have not entered any filename.")

        else: 
            print("Filename provided does not exist.") # else we assume the users input was not matching a filename that exists  

num_of_E = count_E() # function is called and output set to num_of_E

print (f"There were {num_of_E} e's") # The number of Es are printed for the user
