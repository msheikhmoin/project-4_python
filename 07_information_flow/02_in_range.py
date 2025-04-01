# Question 02====

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, # low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """


def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

def main():
    message = input("Please type a message: ")
    
    while True:
        try:
            repeats = int(input("Enter a number of times to repeat your message: "))
            if repeats < 1:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print_multiple(message, repeats)
    num = int(input("Enter a number to check if it's in range: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if in_range(num, low, high):
        print(f"{num} is in the range {low} to {high}.")
    else:
        print(f"{num} is not in the range {low} to {high}.")

if __name__ == "__main__":
    main()