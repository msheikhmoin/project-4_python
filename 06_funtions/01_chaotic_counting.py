# Question 01=====

# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10,
#  but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each
#  number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Here's a sample run of this program:

# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.

import random


DONE_LIKELIHOOD = 0.3

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):  
        if done():  
            return  
        print(i, end=" ")  

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.", end=" ")
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()