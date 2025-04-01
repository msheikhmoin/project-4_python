# Question 05======

#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. 
# The list is guaranteed to be non-empty, but there are no guarantees on its length.


def get_last_element(lst):
    print("Last element:", lst[-1])  


n = int(input("Enter number of elements in the list: ")) 
user_list = []

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)
get_last_element(user_list)
