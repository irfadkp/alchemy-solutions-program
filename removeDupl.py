def rmDup(str, n):
    s = set()
    for i in str:
        s.add(i)
    temp_st = ""
    for i in s:
        temp_st = temp_st+i
    return temp_st
 
 
str = "elephant is large"
n = len(str)
print(rmDup(list(str), n))