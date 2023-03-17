import math
import random

##########################################################################################################
#  Driver Part
##########################################################################################################

def DriverFor_1stQ():
    wordsArray1 = ["programmable", "programming", "programmer", "programmatic", "programmability", "programmabfnfdmsöaç"]
    wordsArray2 = ["compute", "compatible", "computer", "compare", "compactness"]
    print("Input: ", wordsArray1)
    print("Output: ", longestMatch(wordsArray1))
    print("Input: ", wordsArray2)
    print("Output: ", longestMatch(wordsArray2))

def DriverFor_2ndQ():
    Array1 = [10, 11, 10, 9, 8, 7, 9, 11]
    Array2 = [100, 110, 80, 90, 110, 70, 80, 80, 90]
    print("\nSolution for divide and conquer: ")
    print("Input: ", Array2)
    min_val, max_val, diff = maxProfitA(Array2, 0, len(Array2) - 1)
    print(f"Buy on Day {Array2.index(min_val) } for {min_val} and sell on Day {Array2.index(max_val) } for {max_val}") 
    print("\nSolution for another approach: ")   
    print("that part doesn't work correct I don't solve why :(")
    # print("Input: ", Array2)
    #print("Output: ", maxProfitB(Array2, 0, len(Array2) - 1, len(Array2) - 1))
    
def DriverFor_3rdQ(): 
    Array1 = [1, 4, 5, 2, 4, 3, 6, 7, 1, 2, 3, 4, 7]
    Array2 = [1, 2, 3, 4, 1, 2, 3, 5, 2, 3, 4]
    print("Input: ", Array1)
    print("Output: ", lenOfIncreasingArr(Array1))
    print("Input: ", Array2)
    print("Output: ", lenOfIncreasingArr(Array2))

def DriverFor_4rdQ(): 
    map = [[25, 30, 25],
       [45, 15, 11],
       [1, 88, 15],
       [9, 4, 23],
       [1, 1, 1]]
    print("Map:")
    for i in map:
        for j in i:
            print(j, end="\t")
        print()
    print("\nSolution with dynamic approach: ")
    maxScoreA(map, len(map), len(map[0]))
    print("\nSolution with greedy approach: ")
    maxScoreB(map, len(map), len(map[0]))

##########################################################################################################
#  CustomInput Part
##########################################################################################################

def CustomInputFor_1stQ():
    input_string = input('Enter elements of array separated by space ')
    print("\n")
    user_list = input_string.split()
    print("Input: ", user_list)
    print("Output: ", longestMatch(user_list))
    
def CustomInputFor_2ndQ(): 
    arrSize = int(input("Size of the array: "))
    Array2 = [0] * arrSize
    for i in range(0, arrSize):
        Array2[i] = int(input("Enter value for element:"))
    print("\nSolution for divide and conquer: ")
    print("Input: ", Array2)
    min_val, max_val, diff = maxProfitA(Array2, 0, len(Array2) - 1)
    print(f"Buy on Day {Array2.index(min_val) } for {min_val} and sell on Day {Array2.index(max_val) } for {max_val}") 
    print("\nSolution for another approach: ")   
    print("Input: ", Array2)
    print("Output: ", maxProfitB(Array2, 0, len(Array2) - 1, len(Array2) - 1))

    
    
def CustomInputFor_3rdQ():
    arrSize = int(input("Size of the array: "))
    Array1 = [0] * arrSize
    for i in range(0, arrSize):
        Array1[i] = int(input("Enter value for element:"))
    print("Input: ", Array1)
    print("Output: ", lenOfIncreasingArr(Array1))


def CustomInputFor_4rdQ():
    rowA = int(input("size of the rowA: "))
    rowB = int(input("size of the rowB: "))
    map = generateBoardCustom(rowA, rowB)
    print("Map:")
    for i in map:
        for j in i:
            print(j, end="\t")
        print()
    print("\nSolution with dynamic approach: ")
    maxScoreA(map, len(map), len(map[0]))
    print("\nSolution with greedy approach: ")
    maxScoreB(map, len(map), len(map[0]))


##########################################################################################################
#  Functions Part
##########################################################################################################
    
# Question-1 Functions ##############################

def longestMatch(arrA):
    longestMarchString = ""
    if len(arrA) > 1:
        arrB = createSubArray(0, math.floor(len(arrA) / 2), arrA)
        arrC = createSubArray(math.floor(len(arrA) / 2), len(arrA), arrA)
        longestMatch(arrB)
        longestMatch(arrC)
        mergedArr = []
        longestMarchString = Merge(arrB, arrC, mergedArr)
    return longestMarchString
        
def createSubArray(startIndex, endIndex, mainArray):
    return mainArray[startIndex: endIndex]

def Merge(subArr1, subArr2, mainArr):
    i = 0
    j = 0
    commonStr = ""
    while i < len(subArr1) and j < len(subArr2):
        # Compare the characters in the two strings until a non-matching character is found
        ch = 0
        tempStr = ""
        while ch < len(subArr1[i]) and ch < len(subArr2[j]) and subArr1[i][ch] == subArr2[j][ch]:
            tempStr = (tempStr + subArr1[i][ch])
            ch += 1
        if i == 0:
            mainArr.append(tempStr)
        else:
            if len(tempStr) < len(mainArr[0]):
                mainArr.append(tempStr)
        i += 1
        j += 1
    return longestSubstringFinder(str(mainArr[0]), str(mainArr.pop()))

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(min(len1, len2)):
        if string1[i] == string2[i]:
            answer = answer + string1[i]
    return answer

# End of the Question-1 Functions ##############################

# Question-2 Functions ##############################

# similar to quick sort approach, by selecting partition element
def maxProfitB(Arr, l, r, constR):
    r = int(r)
    smallest = min(Arr[l:r-1], default=0)
    if Arr[r] == smallest:
        return r
    else:
        splitPosition = partition(Arr, l, r, constR)
        maxProfitB(Arr, l, splitPosition, constR)

def partition(Arr, l, r, constR):
    pivot = min(Arr[l:r-1], default=0)
    pivotIndex = int(Arr.index(pivot))
    maxElement = max(Arr[pivotIndex: constR-1], default=0)
    diff = maxElement - pivot
    index = 0
    for i in range(pivotIndex+1, constR-1):
        if(Arr[i] - pivot > diff):
            diff = Arr[i] - pivot
            maxElement = Arr[i]
    print("maxElement: ", maxElement, "pivot", pivot)
    print("diff: ", diff)
    return int(pivotIndex)

# divide and conquer approach
def maxProfitA(Arr, l, r):
    if l >= r:
        return None, None, 0

    mid = l + (r - l) // 2
    left_min, left_max, left_diff = maxProfitA(Arr, l, mid)
    right_min, right_max, right_diff = maxProfitA(Arr, mid+1, r)

    smallest = min(Arr[l:mid+1])
    smallestIndex = int(Arr.index(smallest))
    biggest = max(Arr[mid:r+1])
    biggestIndex = int(Arr.index(biggest))
    diff = biggest - smallest

    if left_diff >= right_diff and left_diff >= diff and Arr.index(left_max) >= smallestIndex:
        return left_min, left_max, left_diff
    elif right_diff >= left_diff and right_diff >= diff and Arr.index(right_min) >= biggestIndex:
        return right_min, right_max, right_diff
    else:
        return smallest, biggest, diff

# End of the Question-2 Functions ##############################

# Question-3 Functions ##############################

def lenOfIncreasingArr(arr):
    # updating the lis will be after passing next i value. That causes in case the last element is bigger.
    # So that I add a definitely small value then last element
    arr.append(-463215585675)   
    # at the beginning, no comparison made, so that all indexes are 0
    lis = [1]* len(arr)
 
    maxVal = 0
    # Compute optimized LIS values in bottom up manner
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j]:
                lis[i] = lis[j]+1
            # when an elements become smaller than previous, hold the continiously increased count value
            # and store it either array is end or bigger one comes.
            else:
                if(max(lis) > maxVal):
                    maxVal = max(lis)
                    # print("maxVal becomes: ", maxVal )
                if arr[i] < arr[i-1]:
                    lis = [1]* len(arr)
    return maxVal

# End of the Question-3 Functions ##############################

# Question-4 Functions ##############################

def maxScoreA(board, n, m):
    # Initialize the maximum score array
    F = [[0] * m for _ in range(n)]
    F[0][0] = board[0][0]

    # Construct the F 
    for j in range(1, m):
        F[0][j] = F[0][j-1] + board[0][j]
    for i in range(1, n):
        F[i][0] = F[i-1][0] + board[i][0]
    for i in range(1, n):
        for j in range(1, m):
          F[i][j] = max(F[i-1][j], F[i][j-1]) + board[i][j]

    printRoute(n-1, m-1, F, board)
    print("Max possible score is: ", F[n-1][m-1])
    return F[n-1][m-1]

def maxScoreB(board, n, m):
    score = board[0][0]
    i = 0
    j = 0
    while i < n-1 or j < m-1:
        # perform possible movements 
        if i < n-1 and (j == m-1 or board[i+1][j] > board[i][j+1]):
            i += 1
        else:
            j += 1
        score += board[i][j]

    print("Max possible score is: ", score)
    return score

def printRoute(i, j, F, points):
    path = []
    while i > 0 or j > 0:
        path.append((i+1, j+1))
        if i == 0:
          j -= 1
        elif j == 0:
          i -= 1
        elif F[i][j-1] > F[i-1][j]:
          j -= 1
        else:
          i -= 1
    path.append((1, 1))
    path.reverse()
    for x, y in path:
        print(f"A{x}B{y} = {points[x-1][y-1]}")

def generateBoardCustom(rowA, rowB):
    rowArr = [[0 for x in range(rowB)] for y in range(rowA)] 
    for i in range(0, rowA):
        for j in range(0, rowB):
            cell = int(input("Enter value:"))
            rowArr[i][j] = cell
    print(rowArr)
    return rowArr

# End of the Question-4 Functions ##############################


def main():
    choose = input("Choose the option you want to perform\n"
          "1- Run Driver function for all 3 question\n"
          "2- Test functions with custom input\n:")
    print("choose: ", choose)
    if choose == '1':
        print("\n********************* Question - 1 ********************* ")
        DriverFor_1stQ()
        print("\n********************* Question - 2 ********************* ")
        DriverFor_2ndQ()
        print("\n********************* Question - 3 ********************* ")
        DriverFor_3rdQ()
        print("\n********************* Question - 4 ********************* ")
        DriverFor_4rdQ()

    if choose == '2':
        print("\n********************* Question - 1 ********************* ")
        CustomInputFor_1stQ()
        print("\n********************* Question - 2 ********************* ")
        CustomInputFor_2ndQ()
        print("\n********************* Question - 3 ********************* ")
        CustomInputFor_3rdQ()
        print("\n********************* Question - 4 ********************* ")
        CustomInputFor_4rdQ()

main()


