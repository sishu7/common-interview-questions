#Despite the misleading file title, this reverses each word in a string

string = "I like to eat sushi, especially in Seattle!"

def reverse_str_words(string):
    words = string.split()
    new_words = []
    for w in words:
        rev_word = ''
        for c in range(1, len(w)+1):
            rev_word += (w[len(w)-c])
        new_words.append(rev_word)
    return ' '.join(new_words)

print reverse_str_words(string)
