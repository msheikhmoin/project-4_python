# Question 10=====

# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2

import random


DONE_LIKELIHOOD = 0.3

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):  
        if done():  
            return  
        print(i, end=" ") 

def print_ones_digit(num):
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.", end=" ")
    chaotic_counting()
    print("I'm done.")
    
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()
