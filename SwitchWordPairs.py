#switches pairs of words within a string

string = "ab cd ef gh ij kl"
string2 = "ab cd ef gh ij"

#leaves the last word alone, rather than switching things around a center point

def switch_pairs(string):
    words = string.split()
    new_words = []
    for i in range(1, len(words), 2):
        new_words.append(words[i])
        new_words.append(words[i-1])
    #deals with the odd case
    if len(words) % 2 == 1:
        new_words.append(words[len(words)-1])
    return ' '.join(new_words)

print switch_pairs(string)
print switch_pairs(string2)

#alternative solution switches things around a center point

def switch_pairs2(string):
    words = string.split()
    new_words = []
    #deals with the even case
    if len(words) % 2 == 0:
        for i in range(1, len(words), 2):
            new_words.append(words[i])
            new_words.append(words[i-1])
    else:
        for i in range(1, len(words)/2, 2):
            new_words.append(words[i])
            new_words.append(words[i-1])
        new_words.append(words[len(words)/2])
        for i in range(len(words)/2 + 2, len(words), 2):
            new_words.append(words[i])
            new_words.append(words[i-1])
    return ' '.join(new_words)

print switch_pairs2(string)
print switch_pairs2(string2)
