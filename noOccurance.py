def findCount(s, c) :
    found = 0
     
    for i in range(len(s)) :
        if (s[i] == c):
            found = found + 1
    return found
str= "make me good"
c = 'e'
print(findCount(str, c))