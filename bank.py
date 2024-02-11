#bank.py
#This program asks a user to enter two amounts of money in cents, adds the amounths together and prints the answer in Euros
#Author: Angela Davis

amount1 = int(input("Enter amount1(in cents): "))
amount2 = int(input("Enter amount2(in cents): "))

totalCents = (amount1 + amount2)
totalEuro = (totalCents / 100) #using / to divide allows the answer to be in floating number format

print (f"The sum of these is €{totalEuro}")

