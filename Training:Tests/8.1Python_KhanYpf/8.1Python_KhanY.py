#defining operations for simplicity
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("Hi! My name is calc-bot. I can perform 4 actions: add, subtract, multiply, or divide.")

while(True):
    operation = input("\nWhat mode would you like to set me to? Type +, -, *, or /.\n")
    if (operation == "+" or operation == "-" or operation == "*" or operation == "/") == False:
        print("That's not one of my modes!")
        again = input("Would you like to restart? y/n ")
        if again == "y":
            continue
        else:
            break
    try:
        num1 = int(input("First Number? "))
        num2 = int(input("Second Number? "))
    except:
        print("One of your numbers was typed wrong.")
        again = input("Would you like to restart? y/n ")
        if again == "y":
            continue
        else:
            break

    if operation == "+":
        print("Answer: " + str(add(num1,num2)))
    elif operation == "-":
        print("Answer: " + str(subtract(num1,num2)))
    elif operation == "*":
        print("Answer: " + str(multiply(num1,num2)))
    elif operation == "/":
        print("Answer: " + str(divide(num1,num2)))
    else:
        print("You did not type in a number, or you made a typo!")

    again = input("Would you like to make another calculation? y/n ")
    if again == "y":
        continue
    else:
        print("Goodbye!")
        break
