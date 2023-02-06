#Create a variable inside a function, with the same name as the global variable
x='awesome'


def myfun():
    x="Fantastic"
    print("Python is " + x)

myfun()


print("Python is " + x)

