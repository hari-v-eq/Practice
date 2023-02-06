#1st method
thislist = [100, 50, 65, 82, 23]
car=[1,2,3]

l3=thislist + car
print(l3)


#2nd method

thislist = [100, 50, 65, 82, 23]
car=[1,2,3]
for i in car:
    thislist.append(i)

print(thislist)


#3rd Method
thislist = [100, 50, 65, 82, 23]
car=[1,2,3]

thislist.extend(car)
print(thislist)