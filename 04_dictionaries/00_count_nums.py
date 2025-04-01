# Question 00====

# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number:
# 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times.
# 12 appears 1 times.

numbers_count = {}

while True:
    num = input("Enter a number (or 'q' to quit): ")
    if num.lower() == 'q':
        break
    
    num = int(num)
    numbers_count[num] = numbers_count.get(num, 0) + 1

for num, count in numbers_count.items():
    print(f"{num} appears {count} times.")
