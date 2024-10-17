from datetime import datetime

def processOperations(n, operations):
    hardDrive=dict()
    output=[]
    accessCount=dict()
    timeStamp=dict()
    for i in range(len(operations)):
        # print("iteration: ",i)
        operation=operations[i]
        if(operation[0]==1):
                count=accessCount.get(operation[1],0)
                Value=hardDrive.get(operation[1])
                if  Value is not None:
                    output.append(Value)
                    accessCount[operation[1]]=count+1
                else:
                    output.append(-1)
        else:
            Rating=hardDrive.get(operation[1][0],0)
            count=accessCount.get(operation[1][0],0)
            if len(hardDrive)<n:
                # if Rating == 0:
                hardDrive[operation[1][0]] = operation[1][1]
                accessCount[operation[1][0]]=count+1
                timeStamp[operation[1][0]]=datetime.now()
                # else:
                #     hardDrive.update(hardDrive[operation[1][0]],operation[1][1])
                #     accessCount[operation[1][0]]=count+1
                #     timeStamp[operation[1][0]]=datetime.now()
            else:
                minValue= min(accessCount.values())
                movieName=[key for key, value in accessCount.items() if value == minValue]
                if(len(movieName)>1):
                    longestUpdated=min(movieName, key=lambda k: timeStamp[k])
                    hardDrive.pop(longestUpdated)
                    accessCount.pop(longestUpdated)
                    timeStamp.pop(longestUpdated)
                else:
                    hardDrive.pop(movieName[0])
                    accessCount.pop(movieName[0])
                    timeStamp.pop(movieName[0])
                hardDrive[operation[1][0]] = operation[1][1]
                accessCount[operation[1][0]]=count+1
                timeStamp[operation[1][0]]=datetime.now()
                
    return output

# print(processOperations(2, [(1, "GOT"), (2, ("GOT", 9)), (1, "GOT"), (2, ("NARUT", 10)), (1, "NARUT"), (2, ("BARUT", 6)), (1, "GOT"), (1, "BARUT")]))
# print(processOperations(2, [(2, ("GOT", 9)), # Add "GOT" with rating 9
#  (2, ("NARUT", 10)), # Add "NARUT" with rating 8
#  (1, "GOT"), # Check if "GOT" is present (increases access count)
#  (2, ("BARUT", 6)), # Add "BARUT" with rating 6
#  (1, "NARUT"), # Check if "NARUT" is present
#  (2, ("GOT", 7)), # Update rating of "GOT" (increases access count)
#  (2, ("BBAD", 9)), # Add "BBAD" with rating 9
#  (1, "BARUT"), # Check if "BARUT" is present
#  (1, "GOT"), # Check if "GOT" is present
#  (1, "BBAD"), # Check if "BBAD" is present))
# ]))     

                


