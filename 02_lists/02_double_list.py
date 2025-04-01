# question 02=====

# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

#numbers = [1, 2, 3, 4]
#You should end with this list:
#numbers = [2, 4, 6, 8]

def double_numbers(numbers):
    return [num * 2 for num in numbers]


numbers = [1, 2, 3, 4]
numbers = double_numbers(numbers)

print("Doubled list:", numbers)
