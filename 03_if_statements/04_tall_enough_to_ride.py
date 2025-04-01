# Question 04====

# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this?
 # See the function tall_enough_extension() in the solution code!)



MINIMUM_HEIGHT : int = 50 

def main():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
if __name__ == '__main__':
    main()