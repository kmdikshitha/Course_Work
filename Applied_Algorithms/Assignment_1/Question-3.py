def numberOfTeams(rating):
    count = 0
    for middle in range(len(rating)):
        Lsmall = 0
        Lbig = 0
        Rsmall = 0
        Rbig = 0
        for left in range(middle):
            if rating[left] < rating[middle]:
                Lsmall = Lsmall+1
            else:
                Lbig = Lbig+1
        for right in range(middle + 1, len(rating)):
            if rating[right] > rating[middle]:
                Rbig = Rbig+1
            else:
                Rsmall = Rsmall+1

        count += Lsmall * Rbig + Lbig * Rsmall

    return count

# print(countTeams([2, 5, 3, 4, 1]))
# print(countTeams([2, 1, 3]))        
