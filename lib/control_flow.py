#!/usr/bin/env python3

def admin_login(username, password):
    if  username == "ADMIN" or username == "admin" and password== "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >=40 and temperature <=65:
            return "It's a little chilly out there!"
    elif temperature > 85:
                return "It's too dang hot out there!"
    else:
                    return "It's perfect out there!"
    pass

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
    elif num % 3 == 0:
            return "Fizz"
    elif num % 5 == 0:
                return "Buzz"
    else:
                    return num
    pass

def calculator(operation, num1, num2):
     if operation == "+":
             return num1 + num2
     elif operation == "-":
               return num1 - num2
     elif operation == "*":
                return num1 * num2
     elif operation == "/":
                  return num1/ num2
     else:
              print ("Invalid operation!")
              return None
    



# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")
    
# divide(5,10)
# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")
#     finally:
#         print("Isn't division fun?")
# divide(5,10)