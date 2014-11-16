#compares strings character by characters

def compare(str1, str2):
    if len(str1) == len(str2):
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                return False
    else:
        return False
    return True

print compare('abc', 'abc')
print compare('abd', 'abc')
print compare(' love you', 'I love you')
print compare('I love you', 'I love you')
