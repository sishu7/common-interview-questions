#check whether a string contains a substring

def strstr(substr, str1):
    count = 0
    for i in range(0, len(str1)-len(substr)+1):
        for j in range(0, len(substr)):
            if str1[i+j] == substr[j]:
                count += 1
        if count == len(substr): return True
        count = 0
    return False

print strstr('hav', 'I have pictures')
print strstr('ng', 'walking')
print strstr('abc', 'ananas')

    
