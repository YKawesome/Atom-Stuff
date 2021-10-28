#defining operations for simplicity
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

operation = input("Hi! My name is calc-bot. I can perform 4 actions: add, subtract, multiply, or divide.\nWhat mode would you like to set me to? Type +, -, *, or /.\n")


num1 = int(input("First Number? "))
num2 = int(input("Second Number? "))




if operation == "+":
    print("Answer: " + str(add(num1,num2)))
elif operation == "-":
    print("Answer: " + str(subtract(num1,num2)))
elif operation == "*":
    print("Answer: " + str(multiply(num1,num2)))
elif operation == "/":
    print("Answer: " + str(divide(num1,num2)))
