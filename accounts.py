# accounts.py
# This program prompts a user to take in a 10 character bank account number replacing the first 6 characters with X and displaying the last 4 characters.
# Author: Angela Davis

user_account_no = input('Please enter a 10 digit account number:')
last_4_nos = (user_account_no[-4:]) #slices the last 4 digits of the account number
print(f'XXXXXX{last_4_nos}') 

# This next section is for the extra part of weekly task 03
# Extra: "Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)"
    
# My assumptions:
#       1- The number of Xs should match number of characters that are before the last 4 characters of the string. 
#           Counting the length of the string using len(), getting that value -4 and printing that many Xs.

#       2- The number of characters printed at the end "Xs + 4 displayed characters" should match the length of the string originally entered by the user.

dynamic_user_account = input('Please enter an account number:')
dynamic_last_4_nos = (dynamic_user_account[-4:]) #takes the last four digits of the account inputted by the user

no_of_characters = (len(dynamic_user_account)-4) #getting the length of the string entered by the user and minusing 4
no_of_Xs = ('X'*no_of_characters) #multiples Xs by number in the no_of_characters variable to create string with the required number

print(f'{no_of_Xs}{dynamic_last_4_nos}')