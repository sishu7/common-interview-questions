#reverse a list without using the built-in method

def reverse(l):
    new_list = [];
    for i in range(0, len(l)): new_list.append(l[len(l)-i-1])
    return new_list

print reverse([1, 2, 3, 4, 5, 6])

#do the same thing using recursion

def rec_reverse(l, i, new_list):
    if i < len(l):
        new_list += [l[len(l)-i-1]]
        i += 1
        return rec_reverse(l, i, new_list)
    else: return new_list

print rec_reverse([1, 2, 3, 4, 5, 6], 0, []) 
