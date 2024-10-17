from collections import deque

def  checkout_counter_times(arrivalTimes, actions):
    n = len(arrivalTimes)
    completionTimes = [0] * n
    checkoutQueue = deque()
    returnQueue = deque()
    
    currentTime = 0
    lastAction = -1
    customerIndex = 0
    
    while customerIndex < n or checkoutQueue or returnQueue:
        if not checkoutQueue and not returnQueue:
            if customerIndex < n and currentTime < arrivalTimes[customerIndex]:
                currentTime = arrivalTimes[customerIndex]  
                lastAction = -1
        
        while customerIndex < n and arrivalTimes[customerIndex] <= currentTime:
            if actions[customerIndex] == 0:
                checkoutQueue.append(customerIndex)
            else:
                returnQueue.append(customerIndex)
            customerIndex += 1
        
        if lastAction == 0:
            if checkoutQueue:
                processCustomer(checkoutQueue, currentTime, completionTimes)
            else:
                lastAction=-1
                if returnQueue:
                    processCustomer(returnQueue, currentTime, completionTimes)
        else:
            if returnQueue:
                    processCustomer(returnQueue, currentTime, completionTimes)
            else:
                lastAction=0
                if checkoutQueue:
                    processCustomer(checkoutQueue, currentTime, completionTimes)
        currentTime+=1
 
    return completionTimes

def processCustomer(queue, currentTime, completionTimes):
    customer = queue.popleft()
    completionTimes[customer] = currentTime

# arrivalTimes = [0, 1, 1, 2, 4]
# actions = [0, 1, 0, 0, 1]
# print(checkout_counter_times(arrivalTimes, actions))
