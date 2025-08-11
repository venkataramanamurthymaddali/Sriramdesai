# numbers = [1, 2, 3, 4] 
# numbers.append(5)
# print(numbers)


# numbers = [1, 2, 3]
# new_numbers = numbers.copy()
# new_numbers.append(4)
# print(new_numbers)

# name  = "Venkata Ramana Murthy Maddali"                          #string     
# age = 66                                                         #Intiger                                           #Intiger
# weight_in_kgs = 106.6                                            #float
# is_he_retired = True                                             #boolean
# print(type (name))
# print(type (age))
# print(type (weight_in_kgs))       
# print(type (is_he_retired))

#rice_bag_weight_in_kgs = 70.56
#print(type(rice_bag_weight_in_kgs))                      #<class 'float'>
#rice_bag_weight_in_kgs = int(rice_bag_weight_in_kgs)      #<class 'int'>     
#print(rice_bag_weight_in_kgs)                             #70  output
#rice_bag_weight_in_kgs = str(rice_bag_weight_in_kgs)
#print(type(rice_bag_weight_in_kgs))                        #<class 'str'>
#print(rice_bag_weight_in_kgs)                              #70.56    output


# name = input("What is your name= ")
# age = int(input("What is your age= ") )
# print(f"Hello! {name}, you are {age} years of old.")

# mixed_list = ["Venkat", 66, 106.6, True, None]
#              #  str     int  float  bool None type

   
# print(mixed_list[1])          #66  output

# squares = [1, 4, 9, 16]
# squares.append(25)
# print(squares)                          #[1, 4, 9, 16, 25]     output
# #squares.pop(4)
# #print(squares)                         #[1, 4, 9, 16]        output 

# list = [1, 2, 3, 4, 5]
# list.reverse()
# print(list)                                #[5, 4, 3, 2, 1]   output

# my_dict = {
#     "name": "Venkata",
#     "language": "Python",
#     "location": "India"
# }


# print(my_dict.keys())               #dict_keys(['name', 'language', 'location'])   output
# print(list(my_dict.keys()))          #['name', 'language', 'location']    output

# # Define the lists
# keys = ["id", "name", "age"]
# values = [101, "Aman", 25]

# # Create the dictionary using zip()
# person_dict = dict(zip(keys, values))

# # Print the dictionary
# print(person_dict)                  #{'id': 101, 'name': 'Aman', 'age': 25}       output


# # Get input from the user
# num = int(input("Enter a number: "))

# # Check the condition
# if num > 100:
#     print("The number is greater than 100.")        #Enter a number: 101    The number is greater than 100.
# elif num == 100:
#     print("The number is equal to 100.")             #Enter a number: 100     The number is equal to 100. 
# else:
#     print("The number is less than 100.")             #Enter a number: 85   The number is less than 100.   

# # Get two numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Check the conditions
# if num1 > 10 and num2 > 10:
#     print("Both numbers are greater than 10.")
# elif num1 > 10 or num2 > 10:
#     print("At least one number is greater than 10.")
# else:
#     print("Neither number is greater than 10.")
# #output
# #Enter the first number: 8
# #Enter the second number: 15
# #At least one number is greater than 10.
# #Enter the first number: 12                        
# #Enter the second number: 17                        
# #Both numbers are greater than 10.
# #Enter the first number: 5     
# #Enter the second number: 8                          
# #Neither number is greater than 10.

# # Sample list
# items = ["apple", "banana", "cherry", "date"]

# # Print each item with its index
# for index, value in enumerate(items):
#     print(f"Index {index}: {value}")

# #output
# #Index 0: apple
# #Index 1: banana
# #Index 2: cherry
# #Index 3: date

# # Initialize the counter
# num = 1

# # Loop from 1 to 10
# while num <= 10:
#     if num == 5:
#         num += 1
#         continue
#     print(num)
#     num += 1

#     # output
# # 1  
# # 2
# # 3
# # 4
# # 6
# # 7
# # 8
# # 9
# # 10


# # Define two lists
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# # Pair and print elements using zip()
# for name, score in zip(names, scores):
#     print(f"{name} scored {score}")

# #output
# #Alice scored 85
# #Bob scored 92
# #Charlie scored 78

# for num in range(1, 21):
#     if num == 15:
#         break
#     print(num)

# # output
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
# # 10
# # 11
# # 12
# # 13
# # 14


# def square(num):
#     return num ** 2
# print(square(5))                                #output   25
# print(square(8))                                #output   64
# print(square(-3))                               #output    9

# def check_even(num):
#     return num % 2 == 0
# print(check_even(8))                                     #output       True
# print(check_even(7))                                     #output       False

# print(check_even(16))                                     #output        True
# print(check_even(11))                                     #output        False


# def greet_user(name):
#     return f"Hello, {name}! Welcome aboard."

# print(greet_user("Venkata"))  # Output: Hello, Venkata! Welcome aboard.
# print(greet_user("Aman"))     # Output: Hello, Aman! Welcome aboard.
