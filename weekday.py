# weekday.py
# This program will tell the user if it is a weekday or weekend. 
# Author: Angela Davis

import datetime # datetime module is imported which contains useful functions to help work with dates and times

current_date = datetime.date.today() # here the current date is dertermined
day_of_week = current_date.strftime("%A") # here the strftime() function formats the current date and pulls information for the day of the week from it.
# %A indicates that the full name of the day of the week should be returned 
# the day of the week is then sent to the variable name day_of_week

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] # next the weekdays as stored as strings in the list called weekdays
weekend_days = ["Saturday", "Sunday"] # here the weekend days are stored as strings in a list called weekend_days

if day_of_week in weekdays: 
    print ('Yes, unfortunately toady is a weekday') # if the value of day_of_week variable is present in the weekdays list the program prints this string for the user 

else: # if it is not in the weekdays list (which means day_of_week contains a weekend day) the below is printed
    print ('It is the weekend, yay!') 
