#find duplicates in an array

array = [1, 2, 3, 4, 2, 5, 7, 8, 9, 9, 8, 1, 1, 1, 0]

def f_duplicates(array):
    dictionary = {}
    answers = []
    for i in range(0, len(array) - 1):
        key = array[i]
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    for key in dictionary:
        if dictionary[key] > 1:
            answers.append(key)
    return answers

print f_duplicates(array)
