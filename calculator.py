# this is a simple calculator with addition, subtraction, multiplication and division
# uses input from commandline

def add(x,y):
    return (x+y)

def sub(x, y):
    return x-y

def mult(x,y):
    return x * y

def div(x,y):
    if y==0:
        return "can not divide by 0!"
    return x/y 

def calculator():
    print("choose a function:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")

    selection = input("choose one option (1,2,3 or 4)")

    if selection in ["1","2","3","4"]:
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))

        if selection=="1":
            print(f"{num1} + {num2} = {add(num1,num2)}")
        if selection=="2":
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        if selection=="3":
            print(f"{num1} * {num2} = {mult(num1,num2)}")
        if selection=="4":
            print(f"{num1} / {num2} = {div(num1,num2)}")
    else:
        print("Unknown option, please choose only 1-4")


calculator()