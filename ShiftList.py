#shifts a list by a specified amount

def shift_list(l, n):
    return l[n:] + l[:n]

print shift_list(['a', 'b', 'c', 'd', 'e', 'f'], -2)
