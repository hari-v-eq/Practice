x = ("apple", "banana", "cherry")

y=list(x)
print(y)

y[2]="Mango"
x=tuple(y)
print(x)

#we cannot update the value for the tuple.
#we need to convert it first in list then update and again convert it using the type function