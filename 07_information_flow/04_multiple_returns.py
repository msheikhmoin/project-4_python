# Question 04=====

# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# Asks the user for their email address and stores it in a variable

#What is your email address?: janestanford@stanford.edu

# Received the following user data: ('Jane', 'Stanford', 'janestanford@stanford.edu')

# (Note. This idea is called tuple packing/unpacking. We "pack" our return values into a single data structure called a tuple. We can then "unpack" these values back into our original values or leave them as a tuple.)



def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    
    return first_name, last_name, email
user_data = get_user_data()
print("Received the following user data:", user_data)

     