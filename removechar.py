def removeChar(s, c) :
    char_count= s.count(c)
    s = list(s)
    while char_count:     
        s.remove(c)
        char_count -= 1
    s = '' . join(s)
    print(s)
     
s = "google"
removeChar(s,'g')