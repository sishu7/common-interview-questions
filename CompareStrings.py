#returns all shared letters

def shared_letters(str1, str2):
    dict1 = {}
    answers = []
    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else: dict1[char] = 1
    for char in str2:
        if char not in answers:
            if char in dict1:
                if dict1[char] >= 1:
                    answers.append(char) 
    return answers

print shared_letters('Ilana', 'banana')

#returns only shared letters in same position, in same order (incl. duplicates)

def letters_same_pos(str1, str2):
    answers = []
    top = min(len(str1), len(str2))
    for i in range(0, top):
        if str1[i] == str2[i]:
            answers.append(str1[i])
    return answers

print letters_same_pos('I mike sushi', 'I like soy')
            
