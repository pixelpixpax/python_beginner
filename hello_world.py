print("hello world, my name is PixPAX")

x = 5
y = 10

z = x * y

print(f"5 multiplied by 10 is: {z}")
print(z)

print(x+y)
print(z*3)

a = 1
b=2
c = 3
d = 4
e = 5

cont = True

def say_name_len(name: str):
    """prints 3 lines: greetings to a given name, and length + uppercase of the name

    Args:
        name (str): the name to greet
    """
    print(f"hello {name}, nice to meet you")
    print(f"your name is {len(name)} characters long, nice!")
    print(f"your name in upper case is {name.upper()}")

def introduction():
    print("Hello, I am pixpaxBot")
    name_input = input("what is your name? ")

    if len(name_input) == 0:
        name_input = input("please enter your name!")

    say_name_len(name_input)


def say_name(name:str):
    """praise the given name

    Args:
        name (str): name entered by the user
    """
    print(f"Wow!{name}, thats a wonderfull name! Thank you soooo much!!!")



def new_introduction():
   print("Hello, I am your newest cretion")
   name_input = input("I dont have a name yet.Please enter a name for me: ") 
   say_name(name_input)

   introduction()


new_introduction()
    