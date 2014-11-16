#Reverse the order of words in a string

string = "I love to eat sushi, especially in Seattle!"

def reverse_word_ord(string):
    words = string.split()
    new_words = []
    for i in range(1, len(words) + 1):
        new_words.append(words[len(words) - i])
    return ' '.join(new_words)

print reverse_word_ord(string)
