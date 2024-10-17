def magicalScribe(n):
    output="1"
    i=1
    if n==1:
        return output
    else:
        while(i<n):
            newOutput=""
            consecutive=1
            for j in range(1,len(output)):
                if(output[j]==output[j-1]):
                    consecutive=consecutive+1
                else:
                    newOutput += str(consecutive) + output[j - 1]
                    consecutive = 1               
            newOutput += str(consecutive) + output[-1]
            output = newOutput
            i+=1
    return output

# print(magicalScribe(1))
# print(magicalScribe(5))
# print(magicalScribe(6))


        