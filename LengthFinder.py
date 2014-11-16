#Find the length of a string without built-ins

string1 = "I love to eat sushi!"

def length_finder(string):
    index = 0
    good = True
    while good == True:
        try: 
            string[index]
            index += 1
        except:
            good = False
    return index

print length_finder(string1)
print len(string1)
