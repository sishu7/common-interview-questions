#zeroes duplicates in a list, after first instance

def zero_duplicates(l):
    dict1 = {}
    for i in range(0, len(l)):
        if l[i] in dict1: l[i] = 0
        else: dict1[l[i]] = 1
    return l

print zero_duplicates([1, 2, 2, 3, 4, 4, 5, 5, 6, 6])

#zeroes all duplicates in a list

def zero_duplicates2(l):
    dict1 = {}
    for i in range(0, len(l)):
        if l[i] not in dict1: dict1[l[i]] = 1
        else: dict1[l[i]] += 1
    for j in range(0, len(l)):
        if dict1[l[j]] > 1: l[j] = 0
    return l

print zero_duplicates2([1, 2, 2, 3, 4, 4, 5, 5, 6, 6])
