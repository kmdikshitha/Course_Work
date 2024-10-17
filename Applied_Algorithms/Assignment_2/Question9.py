class amor_dict:
    def __init__(self, nums=[]):
        self.levels = {}
        for number in nums:
            self.insert(number)

    def insert(self, newNumber):
        currentLevel = 0
        newList = [newNumber]

        while currentLevel in self.levels and len(self.levels[currentLevel]) == 2 ** currentLevel:
            newList = self.merge(newList, self.levels[currentLevel])
            del self.levels[currentLevel]
            currentLevel += 1

        self.levels[currentLevel] = self.sorted_insert(self.levels.get(currentLevel, []), newList)

    def search(self, targetNumber):
        foundLevel = -1
        for level, elements in self.levels.items():
            if self.binary_search(elements, targetNumber):
                if foundLevel == -1:
                    foundLevel = level
                else:
                    foundLevel = min(foundLevel, level)

        return foundLevel

    def print(self):
        maxLevel = max(self.levels.keys()) if self.levels else 0
        result = []
        for i in range(maxLevel + 1):
            if i in self.levels:
                result.append(self.levels[i])
            else:
                result.append([])
        return result

    def merge(self, list1, list2):
        mergedList = []
        index1 = index2 = 0
        while index1 < len(list1) and index2 < len(list2):
            if list1[index1] < list2[index2]:
                mergedList.append(list1[index1])
                index1 += 1
            else:
                mergedList.append(list2[index2])
                index2 += 1
        mergedList.extend(list1[index1:])
        mergedList.extend(list2[index2:])
        return mergedList

    def binary_search(self, searchList, targetNumber):
        low, high = 0, len(searchList) - 1
        while low <= high:
            mid = (low + high) // 2
            if searchList[mid] == targetNumber:
                return True
            elif searchList[mid] < targetNumber:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def sorted_insert(self, existingList, newList):
        combinedList = self.merge(existingList, newList)
        return combinedList


# Example usage
# ad = amor_dict([23, 12, 24, 42])
# print(ad.printLevels())  # Example output: [[], [], [12, 23, 24, 42]]

# ad.insert(11)
# print(ad.printLevels())  # Example output: [[11], [], [12, 23, 24, 42]]

# ad.insert(74)
# print(ad.printLevels())  # Example output: [[], [11, 74], [12, 23, 24, 42]]

# print(ad.search(74))  # Example output: 1
# print(ad.search(77))  # Example output: -1



# # Example usage
# ad = amor_dict()
# ad.insert(10)
# ad.insert(20)
# ad.insert(30)
# ad.insert(40)
# ad.insert(50)
# ad.insert(60)

# print(ad.print())  # [[[], [50, 60], [10, 20, 30, 40]]]
# print(ad.search(30))  # 2
# print(ad.search(70))  # -1
