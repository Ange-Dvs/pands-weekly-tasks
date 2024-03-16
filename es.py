# es.py
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.

# Assumptions:
# User can use the relative path (if referencing file in same directory as the program) or full path name (if file is located somewhere else), program should be able to handle both 
# The command line prompt from the user should only contain the prompt to run the python code (i.e. "python es.py") followed the filename or path for the file
# E should be counted regardless of the case
# Error handling should end the program without retry and print a human readable error for the user 

# Author: Angela Davis
#------------------------------------------------------------------------------------------------------------------------#

import os.path # os.path module is imported to read and split the filename
import sys # sys module is imported since it is required to read a filename from the command line

def count_E(): # this fuction reads the content from the filename provided by the user and counts the e's in the specified file.
    if file_extension == ".txt": # first the function checks if the file extension is .txt
        try: #provided the extention is .txt
            with open(filename) as f: # file is first attemped to be opened as "f"
                full_file = f.read()  # the content of the file is set as variable full_file
                number_of_E = full_file.lower().count("e") # lower() is used to convert the file to all lowercase and then count the e's to ensure no uppercase E's are left out of the count
                print (f"Number of e's in file: {number_of_E}") # The number of Es are printed for the user
            
        except FileNotFoundError: # if there is an error thrown that the file is not found the program prints the below error for the user 
            print("Filename provided does not exist.\nProgram exited.\n")  
    
    elif file_extension == "": # if no file extension has been entered we assume the filename is incomplete an remind the user that the program only accepts text files
        print ("The filename/path appears to be incomplete, no filetype is specified.\nThis program only accepts text files, filename/path for text files should end in '.txt' extension.\nProgram exited.\n")

    elif file_extension != ".txt": # if the filename does not end in .txt we tell the user the file type of the entered file and remind them the program only accepts .txt files
        print(f"The filename entered indicates the file is a '{file_extension}' file.\nThis program only accepts '.txt' files.\nProgram exited.\n")

try: # first program tries to read in the file name the user has entered providing the user has not entered a blank value 
    filename = sys.argv[1] # first the sys module is used to get the filename entered from the command line
    file_title, file_extension = os.path.splitext(filename.lower()) # .lower() is used in case the user types the filetype in all caps to convert to lower case for the error handling below
    count_E() # the function count_E() is triggered
    
except IndexError: # if nothing has been entered by the user the following is error is shown to the user.
    print("No filename has been entered.\nProgram exited.\n")