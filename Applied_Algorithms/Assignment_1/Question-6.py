from collections import Counter
def decrypt(s):
    if len(s) % 2 != 0:
        return -1
    halfLength=(int)(len(s)/2)
    count=0
    firstHalf=s[:halfLength]
    secondHalf=s[halfLength:len(s)]
    # print(firstHalf)
    # print(secondHalf)
    freqFirst=Counter(firstHalf)
    freqsecond=Counter(secondHalf)
    for char in freqFirst:
        if freqFirst[char] > freqsecond[char]:
            count += freqFirst[char] - freqsecond[char]
    
    return count
# print(decrypt("aabbccddeeffgghh"))
# print(decrypt("abcabczxyzxyz"))
# print(decrypt("abcdabcdk"))
# print(decrypt("aaaaaabbbbbb"))



        
