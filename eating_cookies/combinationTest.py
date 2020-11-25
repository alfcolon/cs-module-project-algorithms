functionCount = 0
def getCombinations(n, arr, index):
    global functionCount
    functionCount += 1
    
    if arr[index] == 9:
        arr[index] = 0
        return 0
    sum = arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
    if sum > 5:
        arr[index] = 0
        return 0
    arr[index] += 1
    print(arr)

    if index == 4:
        getCombinations(n, arr, index)
    else:
        getCombinations(n, arr, index + 1)
        getCombinations(n, arr, index)

#def getCombinations(n, arr, index):
#    global functionCount
#    functionCount += 1
#
##    if arr[0] > 3 or arr[1] > 3:
##        arr[index] = 0
##        return
#
#    if index == n:
#        return 0
#
#    if arr[index] > 3:
#        arr[index] = 0
#        return 0
#
#    arr[index] += 1
##    print(arr)
#
#    sum = arr[0] + arr[1]
#    if sum == n:
#        if arr[0] == 4 or arr[1] == 4:
#            return 0
##        print(arr)
#        return 1
#    if sum > n:
#        arr[index] = 0
#        return 0
#    if sum < n:
#        i = getCombinations(n, arr, index + 1)
#        arr[index] += 1
#        j = getCombinations(n, arr, index + 1)
#        arr[index] -= 1
#        k = getCombinations(n, arr, index)
#        return i + j + k
#

        

        
def combination(n):
    arr = [0] * 250
    return getCombinations(n, arr, 0)
    # get the number of combinations of 123 with a length value of upto the input n
    # print 1 1 1 1 1
    # have a array that holds 5 values
    
    
    



def CombinationRepetitionUtil(combination, arr, index, length, start, end):
    if index == length:
        total = 0
        for j in range(length):
            total += combination[j]
        print(total)
        if total == 5:
            print(combination)
            for j in range(length):
                print(combination[j], end = " ")
            print()
        return
    if start > n:
        return
    combination[index] = arr[start]
    CombinationRepetitionUtil(combination, arr, index + 1, length, start, end)
    CombinationRepetitionUtil(combination, arr, index, length, start + 1, end)


#def CombinationRepetitionUtil(combination, arr, index, length, start, end):
#    global functionCount
#    functionCount += 1
#    # Current combination is ready, print it
#    if index == length:
#        total = 0
#        for j in range(length):
#            print(combination[j], end = " ")
#        print()
#        return
#
#    # When no more elements are there to put in chosen[]
#    if start > n:
#        return
#
#    # Current is included, put next at next location
#    combination[index] = arr[start]
#
#    # Current is excluded, replace it with next (Note that i+1 is passed, but index is not changed)
#    CombinationRepetitionUtil(combination, arr, index + 1, length, start, end)
#    CombinationRepetitionUtil(combination, arr, index, length, start + 1, end)

# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# CombinationRepetitionUtil()
def CombinationRepetition(arr, n, length):

    # A temporary array to store
    # all combination one by one
    combination = [0] * length
    index = 0
    start = 0

    # Print all combination using
    # temprary array 'chosen[]'
    CombinationRepetitionUtil(combination, arr, index, length, start, n)

# Driver code
arr = [ 1, 2, 3]
r = 2
n = len(arr) - 1

#CombinationRepetition(arr, n, 5)
#CombinationRepetition(arr, n, 4)
#CombinationRepetition(arr, n, 3)
#CombinationRepetition(arr, n, 2)
#CombinationRepetition(arr, n, 1)
#print(functionCount)
combination(50)
print(functionCount)

# This code is contributed by Vaibhav Kumar 12.
#def getCombinations(n, arr, index, sum):
#    if arr[index] == 9:
#        return
#    arr[index] += 1
##    sum += arr[index]
#    print(arr)
##    sum += arr[
##    if sum > 5:
##        sum -= arr[index]
##        arr[index] -= 0
##        return 0
##    if sum == n:
##        return 1
#    if index == 4:
##        sum -= arr[index]
##        arr[index] -= 0
#        return
#    # recur and add one to the next
#
#    getCombinations(n, arr, index + 1, sum)
#    getCombinations(n, arr, index, sum)
##    arr[index + 1] -= 1
#
##    if index == len - 1:
#

# Prints 11111...99999
#def getCombinations(n, arr, index, sum):
#
#    if arr[index] == 9:
#        arr[index] = 0
#        return
#    arr[index] += 1
#    print(arr)
#
#    if index == 4:
#        getCombinations(n, arr, index, sum)
#    else:
#        getCombinations(n, arr, index + 1, sum)
#        getCombinations(n, arr, index, sum)


#getting sum working
#def getCombinations(n, arr, index, sum):
#    if arr[index] == 9:
#        arr[index] = 0
#        return
#    sum = arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
#    if sum > 5:
#        arr[index] = 0
#        return
#    arr[index] += 1
#    print(arr)
#
#    if index == 4:
#        getCombinations(n, arr, index, sum)
#    else:
#        getCombinations(n, arr, index + 1, sum)
#        getCombinations(n, arr, index, sum)

