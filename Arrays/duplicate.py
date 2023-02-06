def duplicates(num):
    num_set=set()

    no_dup=-1

    for i in range(len(num)):
        if num[i] in num_set:
            return num[i]
        else:
            num_set.add(num[i])

    return no_dup

print(duplicates([1,2,3,4,5]))
