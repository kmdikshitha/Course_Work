# Input: words = ["To","be","or","no","question","answer","is","question"], width = 13
#  Output: [
#  "To be or no",
#  "question
def helpElara(words, width):
    output = []
    row = []
    Length = 0

    for word in words:
        if Length + len(word) + len(row) > width:
            spaces = width - Length
            gaps = len(row) - 1
            
            if gaps > 0:
                spaceList = [0] * gaps
                while spaces > 0:
                    for i in range(gaps):
                        if spaces > 0:
                            spaceList[i] += 1
                            spaces -= 1

                line = []
                for i in range(len(row)):
                    line.append(row[i])
                    if i < gaps:
                        line.append(' ' * spaceList[i])
                output.append(''.join(line))
            else:
                output.append(row[0].ljust(width))
            row = []
            Length = 0

        row.append(word)
        Length += len(word)
    output.append(' '.join(row).ljust(width))
    return output

# print(helpElara(["To", "be", "or", "no", "question", "answer", "is", "question"], 13))
output = helpElara(["To", "be", "or", "no", "question", "answer", "is", "question"], 13)
for line in output:
    print(f'"{line}"')
