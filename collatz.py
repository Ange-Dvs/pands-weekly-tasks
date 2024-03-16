# collatz.py
# This program asks a user to input any positive integer and outputs the successive values of the following calculation.
# At each step of the calcutions: 
#   - If the value is even it is divided by two
#   - If the value is odd it is multiplied by three and one is added.
# The program ends when the current value is one and the results of each step of the calcutions is shown to the user
# Author: Angela Davis

collatz_list = [] # defining an empty list to use later to store the values from the calculation after each loop

number = int(input("Please enter a positive integer: ")) # integer is taken in from the user

while number <= 0: # checks to ensure the value entered by the user is a positive integer and not a negative value or 0
    print ("You have not entered a positive integer.") 
    # if it is a negative value or 0, the user is informed and prompted again. The negative number is not saved to the list.
    number = int(input("Please try again and enter a postive integer:")) 

collatz_list.append(number) # providing the value is a positive integer it is written as the first number to the list

while number != 1: # this while loop then checks to ensure the number is not equal to 1
    # providing the number is not equal to 1 it is then checked if the number is even or odd
    if (number % 2) == 0: #if even the program follows this flow
        number = (number//2) # the number is devided by 2. // is used to ensure the result is an integer  
    else: # all other numbers pass through the else condition, we know this will not be even numbers, 0 or 1 due to the checks already carried out by the code
        number = int((number * 3) + 1) # for the odd number the number is multiplied by 3 and 1 is added
    collatz_list.append(number) # when the iteration of the WHILE loop is completed the latest number is added to list
    # The while loop will repeat  until the value for number is 1
    

for numbers in collatz_list: # using a FOR loop we can print the numbers stored in the list
    print (numbers, end=" ") # here end=" " is used to place a single space inbetween each value printed from the list
    