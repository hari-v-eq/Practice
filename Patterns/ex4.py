#inverted pyramid of same number

rows=5
b=rows


for i in range(rows, 0, -1):
    b+=0
    for j in range(1,i+1):
        print(b, end=" ")
    print(" ")