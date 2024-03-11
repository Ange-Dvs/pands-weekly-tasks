# squareroot.py
# This takes a positive floating-point number as input and outputs an approximation of its square root.
# create a function called <tt>sqrt</tt> that does this.
# Author: Angela Davis

def sqrt():
    first_guess = num_from_user / 2 # get the initial guess by dividing the number from the user by 2
    next_guess = (first_guess + (num_from_user / first_guess)) / 2 # calculate the next guess

    while True: 
        guess = (next_guess + (num_from_user / next_guess)) / 2 # repeat the calculation with the next guess replacing the first guess
        if abs(next_guess - guess) == 0:  # Check if the new guess is correct by checking if the old guess and new guess are equal
            return guess # when the two guesses match the value will be returned to the main program
        next_guess = guess # next_guess value is updated if the two guesses do not match

# Get the number from the user
num_from_user = float(input("Please enter a positive number: "))
approx_sqrt = sqrt() # call function to get the square root and set to approx_sqrt variable
print(f"The square root of {num_from_user} is approximately {approx_sqrt}") # print the approximate square root