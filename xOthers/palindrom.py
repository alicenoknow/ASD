def palindrom(s):
    i = 0
    while i <= len(s)-1-i:
        if s[i] == s[len(s)-1-i]:
            i += 1
        else:
            return False
    return True

def palindrom2(s):
    if len(s) < 2 :
        return True
    if s[0] != s[len(s)-1]:
        return False
    return palindrom2(s[1:len(s)-1])


s = "abaeba"
res = palindrom2(s)
print(res)