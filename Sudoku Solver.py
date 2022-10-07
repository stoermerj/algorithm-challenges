"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
#https://leetcode.com/problems/sudoku-solver/https://github.com/stoermerj/algorithms-Sudoku-Solver.git

Input: listArray = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]
Explanation: The input listArray is shown above and the only valid solution is shown below:
"""

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],]


board2 = [
    [".",".",".","2","6",".","7",".","1"],
    ["6","8",".",".","7",".",".","9","."],
    ["1","9",".",".",".","4","5",".","."],
    ["8","2",".","1",".",".",".","4","."],
    [".",".","4","6",".","2","9",".","."],
    [".","5",".",".",".","3",".","2","8"],
    [".",".","9","3",".",".",".","7","4"],
    [".","4",".",".","5",".",".","3","6"],
    ["7",".","3",".","1","8",".",".","."],]

#this algorithm only solves easy sudokus
intermediateBoard = [
    [".","2",".","6",".","8",".",".","."],
    ["5","8",".",".",".","9","7",".","."],
    [".",".",".",".","4",".",".",".","."],
    ["3","7",".",".",".",".","5",".","."],
    ["6",".",".",".",".",".",".",".","4"],
    [".",".","8",".",".",".",".","1","3"],
    [".",".",".",".","2",".",".",".","."],
    [".",".","9","8",".",".",".","3","6"],
    [".",".",".","3",".","6",".","9","."],]

def column(arr):
    columnArr = [[],[],[],[],[],[],[],[],[]]
    for list in arr:
        for index, value in enumerate(list):
            if index == 0:
                columnArr[0].append(value)
            if index == 1:
                columnArr[1].append(value)
            if index == 2:
                columnArr[2].append(value)
            if index == 3:
                columnArr[3].append(value)
            if index == 4:
                columnArr[4].append(value)
            if index == 5:
                columnArr[5].append(value)
            if index == 6:
                columnArr[6].append(value)
            if index == 7:
                columnArr[7].append(value)
            if index == 8:
                columnArr[8].append(value)
    return columnArr

def subBox(arr):
    subBoxArr = [[],[],[],[],[],[],[],[],[]]
    for list in arr:
        for index, value in enumerate(list):
            if (index == 0 or index == 1 or index == 2) and (list == arr[0] or list == arr[1] or list == arr[2]):
                subBoxArr[0].append(value)
            if (index == 3 or index == 4 or index == 5) and (list == arr[0] or list == arr[1] or list == arr[2]):
                subBoxArr[1].append(value)
            if (index == 6 or index == 7 or index == 8) and (list == arr[0] or list == arr[1] or list == arr[2]):
                subBoxArr[2].append(value)
            if (index == 0 or index == 1 or index == 2) and (list == arr[3] or list == arr[4] or list == arr[5]):
                subBoxArr[3].append(value)
            if (index == 3 or index == 4 or index == 5) and (list == arr[3] or list == arr[4] or list == arr[5]):
                subBoxArr[4].append(value)
            if (index == 6 or index == 7 or index == 8) and (list == arr[3] or list == arr[4] or list == arr[5]):
                subBoxArr[5].append(value)
            if (index == 0 or index == 1 or index == 2) and (list == arr[6] or list == arr[7] or list == arr[8]):
                subBoxArr[6].append(value)
            if (index == 3 or index == 4 or index == 5) and (list == arr[6] or list == arr[7] or list == arr[8]):
                subBoxArr[7].append(value)
            if (index == 6 or index == 7 or index == 8) and (list == arr[6] or list == arr[7] or list == arr[8]):
                subBoxArr[8].append(value)    
    return subBoxArr

#checks if the values in three arrays have intersecting values
def sameValue(horizontal, vertical, subBox):
    my_s1 = set(horizontal)
    my_s2 = set(vertical)
    my_s3 = set(subBox)
    my_set1 = my_s1.intersection(my_s2)
    output_set = my_set1.intersection(my_s3)
    output_list = list(output_set)
    if "." in output_list:
        output_list.remove(".") #removes the fields that are not yet filled with numbers
    return output_list

def executer(sudokuBoard):
    
    def filler(arrayType):
        row = 0 #counts the row
        for arr in arrayType: 
            for index, value in enumerate(arr):
                if value == ".":
                    horizontalValues = horizontalCrawlCheck(arr)
                    if len(horizontalValues) == 1:
                        arr[index] = str(horizontalValues[0])
                        
                    verticalValues = verticalCrawlCheck(index)
                    if len(verticalValues) == 1 and len(horizontalValues) != 1:
                        arr[index] = str(verticalValues[0])
                        
                    subBoxValues = subBoxCrawlCheck(row, index)
                    if len(subBoxValues) == 1:
                        if len(horizontalValues) != 1:
                            if len(verticalValues) != 1:
                                arr[index] = str(subBoxValues[0])            
                                
                    intersectingValues = sameValue(horizontalValues, verticalValues, subBoxValues)
                    if len(intersectingValues) == 1 and (len(subBoxValues) != 1 or len(verticalValues) != 1 or len(horizontalValues) != 1):
                        arr[index] = str(intersectingValues[0])
                    
            row = row + 1          
        return arrayType
    
    #returns current values NOT in horizontal Arr
    def horizontalCrawlCheck(arr):
        rangeTen = list(range(1,10))
        valueArr = []
        for value in arr:
            if value != '.' and len(value) == 1:
                    valueArr.append(int(value))
        valueArr = set(rangeTen).difference(set(valueArr)) # find values that are NOT in valueArr
        valueArr = list(valueArr) #turn back to list
        return valueArr
    
    #returns current values NOT in vertical Arr
    def verticalCrawlCheck(ind):
        rangeTen = list(range(1,10))
        valueArr = []
        for value in columnArray[ind]:
            if value != '.':
                    valueArr.append(int(value))
        valueArr = set(rangeTen).difference(set(valueArr)) # find values that are NOT in valueArr
        valueArr = list(valueArr) #turn back to list
        return valueArr
    
    #returns current values NOT in subBox Arr. Works for horizontal and vertical arrs alike
    def subBoxCrawlCheck(row, ind): 
        rangeTen = list(range(1,10))
        valueArr = []
        if row == 0 or row == 1 or row == 2:
            row = [0,1,2]
            for arrays in row:
                for index, value in enumerate(listArray[arrays]):
                    if ind < 3:
                        if value != '.' and (index ==0 or index == 1 or index == 2):
                            valueArr.append(int(value))
                    if 2 < ind < 6:
                        if value != '.' and (index ==3 or index == 4 or index == 5):
                            valueArr.append(int(value))
                    if 5 < ind < 9:
                        if value != '.' and (index ==6 or index == 7 or index == 8):
                            valueArr.append(int(value))
                        
        if row == 3 or row == 4 or row == 5:
            row = [3,4,5]
            for arrays in row:
                for index, value in enumerate(listArray[arrays]):
                    if ind < 3:
                        if value != '.' and (index ==0 or index == 1 or index == 2):
                            valueArr.append(int(value))
                    if 2 < ind < 6:
                        if value != '.' and (index ==3 or index == 4 or index == 5):
                            valueArr.append(int(value))
                    if 5 < ind < 9:
                        if value != '.' and (index ==6 or index == 7 or index == 8):
                            valueArr.append(int(value))
        
        if row == 6 or row == 7 or row == 8:
            row = [6,7,8]
            for arrays in row:
                for index, value in enumerate(listArray[arrays]):
                    if ind < 3:
                        if value != '.' and (index ==0 or index == 1 or index == 2):
                            valueArr.append(int(value))
                    if 2 < ind < 6:
                        if value != '.' and (index ==3 or index == 4 or index == 5):
                            valueArr.append(int(value))
                    if 5 < ind < 9:
                        if value != '.' and (index ==6 or index == 7 or index == 8):
                            valueArr.append(int(value))   
                        
        valueArr = set(rangeTen).difference(set(valueArr)) # find values that are NOT in valueArr
        valueArr = list(valueArr) #turn back to list                
        return valueArr
    
    listArray = sudokuBoard
    columnArray = column(listArray)
    subBoxArray = subBox(listArray)
    
    finalSudokuBoard = []
    checker = 1
    while len(finalSudokuBoard) != 9:
        listArray = filler(listArray)
        columnArray = column(listArray)
        subBoxArray = subBox(listArray)
        listArray = filler(listArray)
        
        for arr in listArray:
            if "." not in arr:
                finalSudokuBoard.append(arr)
        
        checker = checker + 1
        if checker == 10: #safety measure
            break
    return listArray
    
finalBoard = executer(board)
print(finalBoard)


Output = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]

if finalBoard == Output:
    print("SUCCESS")