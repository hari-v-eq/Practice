# In the event that you pass arguments like whole numbers, strings or tuples to a function, 
# the passing is like call-by-value
# because you can not change the value of the immutable objects being passed to the function.

#call by value


string="Hariom"

def test(string):
    string="Hariom_Verma"
    print("New String: ",string)

test(string)
print("Outside function: ",string)



name="John"
def id(name):
    name="Karl"
    print("New name:",name)
id(name)
print("Outside name: ",name)