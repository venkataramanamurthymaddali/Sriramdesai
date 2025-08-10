# name = 'Amit'
# age = 21
# is_student = True
# scores =[80, 85, 90]
# info = {"branch": "Mechanical", "college": "IIT Patna"}
#print(name, age, is_student, scores, info)

#Inpudt/Output

# user_name = input("Enter your name: ")
# print("Welcome, " + user_name)

#Conditional Statements
# marks = int(input("Enter your marks: "))
# if marks >= 90:
   
#    print("Excellent!")
# elif marks >= 75:
#     print("Good Job")
# else:
#     print("Keep practising")      

#     numbers = [1, 2, 3, 4]
#     for num in numbers:
#         print(num * num)

#Defining Functions

# def greet(n):
#     print("Hello,",n)
# greet("NTR")

#Exercises

1#Changing Data:
#Write a script that asks the user for their favorite number, doubles it, and prints the result.

# fav_num = int(input("Enter your favorite number: "))
# dub_fav_num = fav_num * 2
# print(f"Double of favourite number of user is, {dub_fav_num}") 

#2.	Lists Practice:
#	Create a list of three of your hobbies. Loop through the list, printing "I enjoy ".

#my_hobbies = ['cricket', 'basketball', 'vollybally']
#for hobby in my_hobbies:
#  #print(f"I enjoy {hobby}")

#3.Basic Calculator:
#•	Write a function add(a, b) that returns their sum.
#•	Call this with two numbers and print the result.

#def add(a, b):
    #return a + b

# Example usage
# result = add(10, 5)
# print("The sum is:", result)
 

#4.	Conditional Logic:
#	Ask the user what year they were born, calculate their age, and print “You are an adult” if over 18.
# from datetime import datetime
# # Ask the user for their birth year.
# birth_year = int(input("What year were you born: "))
# # Get the current year
# current_year = datetime.now().year
# #calculate age
# age = current_year - birth_year
# #Print age and check if the user is an adult
# print(f"You are of {age} years old")
# if age > 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

#5.	Mixing It Up:
#•	Write aWrit function that takes a list of numbers and returns the largest one.

# def find_largest(numbers):
#     if not numbers:
#         return None  # Handle empty list
#     largest = numbers[0]
#     for num in numbers[1:]:
#         if num > largest:
#             largest = num
#     return largest

# my_list = [3, 7, 2, 9, 5]
# print(find_largest(my_list))



# def find_largest(numbers):
#     print("Input list:", numbers)  # Debug print
#     if not numbers:
#         return None
#     largest = numbers[0]
#     for num in numbers:
#         print(f"Comparing {num} with current largest {largest}")  # Debug print
#         if num > largest:
#             largest = num
#             print(f"Updated largest to {largest}")  # Debug print
#     return largest

# # Test case
# my_list = [3, 7, 2, 9, 5]
# result = find_largest(my_list)
# print("Final result:", result)
 

#6.	Array Manipulation:
#•	Write a function add(arr, x) that takes an array arr and add x to every element in that array

# def add(arr, x):
#     return [element + x for element in arr]

# numbers = [1, 2, 3, 4, 5]
# result = add(numbers, 5)
# print(result)


# def add(arr, x):
#     return [element + x for element in arr]

# numbers = [1, 2, 3, 4]
# result = add(numbers, 5)
# print(result)

# Write a function equal(arr, x) that takes an array arr and returns all the elements in that array that are equal to x

def equal(arr, x):
    return[element for element in arr if element == x]
data = [3, 5, 2, 5, 7, 5]
result = equal(data,5)
print(result)