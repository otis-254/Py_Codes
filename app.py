# # #Conditional 

# temperature = 22
# if temperature > 30:
#     print("Wah! It is crazy hot today")
# elif temperature > 20:
#     print ("Let's go hiking!")
    
# elif temperature > 15:
#     print ("Yak! Need some coffee!")
# # print("Done")

# # Ternary 
# age = 30
# if age > 18:
#     print("Eligible")
# else: print("Not Eligible")

# # -------------------
# # OR
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)
 




# #Project 
# weight = input ("What is you weight?")
# comparison = input ("In (K)g or (L)bs ")
 
# K = weight
# L = weight
 
# if K == weight:
#     print ("Your weight in Kg is: " + str(weight) + " " "Kg")
# else:
#     print ("Your weight in (L)bs is: " + str(weight) + " " "(L)bs")
 

# #While Loops

#    # i = 1
# # while i<= 10:
# #     print (i)
# #     i = i + 1
# i = 1
# while i <= 1_000:
#     print (i)
#     i = i + 1


#     # Varibles

# # course = "Python Programming"
# # print(len(course))
# # print(course[0])
# # print(course[-1])
# # print(course[3])


# # Escape sequence
# # \'
# # \""
# # \n

# # course = "Python \nLesosn"
# # print(course)

# # String Formatting
# # --------------------
# # import math
# # first = "Mosh"
# # second = "Hamedani"
# # # full = first + " " + second

# # # -------------------
# # # Using formated string function (f)
# # # -------------------

# # full = f"{first} {second}"
# # print(full)


# # # Functions/Methods
# # name = "  Python Programming"
# # print(name.upper())
# # print(name.lower())
# # print(name.strip())
# # print(name.title())
# # print(name.find("Pro"))
# # print(name.replace("Pro", "Jonny"))
# # print("bro" in name)
# # print("bro" not in name)


# # # Numbers
# # print(10 + 2)\


# # print(10 - 2)
# # print(10 * 2)
# # print(10 / 3)
# # print(10 // 3)
# # print(10 % 3)  # Modulus (Shows the remainder, which in this case is 1)
# # print(10 ** 3)  # Riased to the power of ...

# # More functions
# # print(round(2.25))
# # print(abs(-2.25))

# # print(math.ceil(2.2))


# # # Type conversion
# # x = input("x: ")
# # y = int(x) + 1
# # print(f"x: {x}, y{y}")


# # juice = input('Mango')
# # food = input('Chipo')
# # meals = input('Cooked')
# # print(meals)

# # Escape sequence

# # \'
# # \""
# # \n

# # course = "Python \nLesosn"
# # print(course)

# # String Formatting
# # first = "Mosh"
# # second = "Hamedani"
# # full = first + " " + second

# # print(full)


# # Functions/Methods
# # name = "  Python Programming"
# # print(name.upper())
# # print(name.lower())
# # print(name.strip())
# # # print(name.title())
# # print(name.find("Pro"))
# # print(name.replace("Pro", "Jonny"))
# # print("bro" in name)
# # print("bro" not in name)


# # # Numbers
# # print(10 + 2)
# # print(10 - 2)
# # print(10 * 2)
# # print(10 / 3)
# # print(10 // 3)
# # print(10 % 3)  # Modulus (Shows the remainder, which in this case is 1)
# # print(10 ** 3)  # Riased to the power of ...

# # import math
# # More functions
# # print(round(2.25))
# # print(abs(-2.25))

# # print(math.ceil(2.2))


# # # Type conversion/Geeting User's input
# # x = input("x: ")
# # y = int(x) + 1
# # print(f"x: {x}, y{y}")


# # Falsey and Truthy values

# # # Strings by using tripple quotes
# # message = """
# # Hi

# # This is Calvins from Merit Graphics
# # Thanks for joining my waiting  list!
# # Regards,
# # Calvins

# #  """
# # print(message)


# # The lengt (len)  function
# # course_name = "Python \\ Programming Couse"
# # # print(len(course_name))
# # # print(course_name[-4])
# # # print(course_name[0:])
# # # print(course_name[:3])

# # print(course_name)

# high_income = False
# good_credit = True
# student = False
# if  high_income and good_credit:
#     print("Eligible for loan"),
# else:print("Not eligible for loan")


# if (high_income or good_credit) and not student:
#     print("Give Loan")
# else: 
#     print("Do not Give loan")


# passed_exam = True
# has_fees = False

# if passed_exam and has_fees:
#     print("Diren Entry!")
# else:
#     print("Join College")


 
# # If age is between 18 to 65 yearsc
# age = 22
# if age > 18  <65:
#     if 18 <= age < 65:  # SHOTTENED FORM
#     print("Eligible")




# For Loops
# Conditonals 
# Ternary statements
# Logical operators
# Chaining 
# 



# # For loops
# for number in range (3, 10, 2):
#     print(number, + ".")

# For...else loop
# successful = False
# for number in range (3):
#  print("Attempt")
#  if successful:
#    print("Successful!")
#    break
# else:
#     print("Too many attempts but you failed")


#     # Nested Loops
# for x in range (5):
    # for y in range (3):   
    #     print(f"{x}, {y}")


# count  = 0 
# for number in range (1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# else:
#     print(f"We have {count} evens")

# Defining a function
# def greet (first_name, last_name):
#     print(f"Hello!, {first_name} {last_name}")
#     print("Nice to meet you!")
 
 
# greet("Sam", "Kim")

# # Keyword Argument
# def increament (number, by):
#     return number + by

# print(increament (2, 1))


# ------------------------------
# # Default Argument
# def increament (number, by=2):
#     return number + by

# print(increament (2))

# Multiplying Args
# def numbers (*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
 
# print(numbers(2, 3, 4, 5))

# --------------------------------



# # # **args
# def user (**user):
#     print(f"The use name is ", user["name"])
#     print(f"The use age is ", user["age"])

# user(pos=1, name="Mike", age=20)



# FixxBuz Exercise
def fizzBuzz (input):
    if input % 3 ==0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0: 
        return "Buzz"
    else:
        return input
print(fizzBuzz(3))
    

 