#find all pairs in a list that add up to a target
#does not eliminate duplicates

def adding_pairs(l, target):
    answers = []
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == target:
                answers.append((l[i], l[j]))
    return answers

print adding_pairs([1, 2, 3, 4, 5, 6, 2, 3, 8, 6, 5], 10)
            
#removes duplicates

def adding_pairs2(l, target):
    answers = []
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == target:
                if (l[i], l[j]) not in answers and (l[j], l[i]) not in answers:
                    answers.append((l[i], l[j]))
    return answers

print adding_pairs2([1, 2, 3, 4, 5, 6, 2, 3, 8, 6, 5], 10)
