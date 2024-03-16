#bank.py
#This program asks a user to enter two amounts of money in cents, adds the amounths together and prints the answer in Euros
#Author: Angela Davis

# User is asked to input the two figure in cents to be used in the calculation
# This is pre-defined as an integer as this is the type of number desired to be entered by the user
# if a user enters a float there will be an error thrown
amount1 = int(input("Enter amount1(in cents): ")) 
amount2 = int(input("Enter amount2(in cents): "))

totalCents = (amount1 + amount2) # total amount of cents is calculated by adding the two values inputted by the user together
totalEuro = (totalCents / 100) # the cents are converted to Euro by dividing by 100. Here / is used to divide to allow the answer to be in floating number format.

print (f"The sum of these is €{totalEuro}") # the result in euros is printed for the user

