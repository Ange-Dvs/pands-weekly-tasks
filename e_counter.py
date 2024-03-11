# e_counter.py
# Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line.
# Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.
# Author: Angela Davis

# Assumptions starting: 
# Pre requisite - Have multiple text files to test with w/ various numbers of e characters
# Create a function for counting the e's in the chosen file
# use input for to take in the file name from the user > might need to look into this further
# create error catching for 
# 1. blank feedback from user
# 2. incorrect/non existing filename 
# 3. asked for a file which is not a text file

import os.path
FILENAME = 'countE5s.txt' # this file contains 5 es

#def count_E(number_of_Es): 
with open(FILENAME, 'r') as f:
    file_text = f.read()
    number_of_Es = 0
    e = "e"
    for e in file_text: 
            number_of_Es += 1
#return number_of_Es # the function then returns the number

# output
#final_num_of_E = count_E(number_of_Es)
print(f"The letter E appears in this file {final_num_of_E} time.)")