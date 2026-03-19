s = "abcabcbb"
# Brute Force 
maxe = 0 
for  i  in  range(len(s)):
    hash = [0] * 256 
    for j in  range( i , len(s)):
        aValue = ord(s[j])
        if hash[aValue] == 1 :break
        length = j - i + 1 
        maxe = max(length , maxe)
        hash[aValue] = 1
print(f"The Answer : {maxe}")

# optimal Solution 
left = 0
right = 0
max = 0
sum = 0
hash = [0] * 256
while right < len(s) :
    value = ord(s[right])
    if hash[value] == 1 :
        while hash[ord(s[left])] != hash[ord(s[right])] and left <= right :
            hash[left] = 0
            left += 1
        left += 1
    hash[value] = 1
    right += 1
    max = right - left 
    if max < sum :
        max = sum
print(f"The Optimal Soultion :  {max}")
