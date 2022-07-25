def isPal(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
result = isPal(s)
 
if result:
    print("Yes")
else:
    print("No")
