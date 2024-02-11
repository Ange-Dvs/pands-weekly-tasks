# accounts.py
# This program takes in a 10 character bank account number (Assumption - program should not accept string less than 10 digits).
# The first 6 characters are replaced with X's.
# Last last 4 characters are diplayed

user_account_no = input('Please enter a 10 digit account number:')
user_account_length = len(user_account_no) #counts length of string

if user_account_length == 10:  #checks if the string lenght is equal to 10
    last_4_nos = (user_account_no[-4:]) #slices the last 4 digits of the account number
    print(f'XXXXXX{last_4_nos}') 

elif user_account_length != 10: #checks if the string lenght is not equal to 10
    print(f'You have entered an account number with {user_account_length} digits.\nThe account number must be 10.')
    user_account_no = input('\nPlease enter a 10 digit account number:')

# This next section is for the extra part of weekly task 03
# Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
    
# My assumptions:
#       1- The last four characters of the string should be able to be identified dynamically (cannot use a static starting position to slice from).
#           len() could be used to create a dynamic value for the starting position to slice the last four digits regardless of how long the string is.

#       2- The number of Xs should match number of characters that are before the last 4 characters of the string. 
#           Counting the length of the string using len(), getting that value -4 and printing that many Xs.

#       3- The number of characters printed at the end "Xs + displayed characters" should match the length of the string originally entered by the user.

dynamic_user_account = input('Please enter an account number:')
dynamic_last_4_nos = (dynamic_user_account[(len(dynamic_user_account))-4:]) #slicing the last four characters of the string entered regardless of lenght

no_of_characters = (len(dynamic_user_account)-4) #getting the length of the string entered by the user and minusing 4
no_of_Xs = ('X'*no_of_characters) #multiplying Xs by number in the no_of_characters variable to create the required number of Xs needed

print(f'{no_of_Xs}{dynamic_last_4_nos}')