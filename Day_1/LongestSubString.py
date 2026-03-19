s = "abcabcbb"
maxe = 0 
for  i  in  range(len(s)):
    hash = [0] * 256 
    for j in  range( i , len(s)):
        aValue = ord(s[j])
        if hash[aValue] == 1 :break
        length = j - i + 1 
        maxe = max(length , maxe)
        hash[aValue] = 1
print(f"The ANswer : {maxe}")