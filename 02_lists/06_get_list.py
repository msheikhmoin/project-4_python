# Question 06====

#Write a program which continuously asks the user to enter values which are added one by one into a list. 
# When the user presses enter without typing anything, print the list.
#'s a sample run (user input is in blue):
#Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


user_list = []  # Empty list start mein

while True:
    value = input("Enter a value: ")
    if value == "":  # Agar input blank ho to loop break kar do
        break
    user_list.append(value)  # List mein value add karo

print("Here's the list:", user_list)  # Yeh list print karega

