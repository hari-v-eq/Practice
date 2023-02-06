#call by reference


def add_list(list):
    list.append(50)
    print("Inside function : ", list)

new_list=[10,20,30,40]

add_list(new_list)

print("Outside Function: ",new_list)