import string
def sortVowels(code):
    result=list(code)
    vowels=['A','E','I','O','U','a','e','i','o','u']
    arr=[]
    for char in code:
        if char in vowels:
            arr.append(char)
    sortArr=sorted(arr)
    j=0
    for i in range(len(result)):
        char=result[i]
        if char in vowels:
            result[i]=sortArr[j]
            j+=1
    return ''.join(result)

# print(sortVowels("BAtmAnCavE"))
# print(sortVowels("bRucEwaYne"))