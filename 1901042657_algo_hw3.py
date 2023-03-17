# Variables for 1st question
graphAdjList = {}
visited = {} # boolean list, 0: Unvisited, 1: Visited
finishingTime = {}
stack = []

import copy
import math
import sys
sys.setrecursionlimit(1500)

##########################################################################################################
#  Driver Part
##########################################################################################################

def DriverFor_1stQ():
    # First generate a graph
    # We can use dictionary to represent a graph 
    graph = {
        'CSE102': ['CSE241'],
        'CSE241': ['CSE222'],
        'CSE222': ['CSE321'],
        'CSE211': ['CSE321'],
        'CSE321': ['CSE422'],
        'CSE422': []
    }

    # Print the graph as list format
    print("\nYour graph is: \n")
    for key, val in graph.items():
        graphAdjList[key] = val
        print(f"{key}-->{val}")

    # Add graph to the list and
    # set all nodes as unvisited
    for key, val in graph.items():
        graphAdjList[key] = val
        visited[key] = 0 # mark them all as unvisited at the beginning

def DriverFor_1stQ_a():
    print("\nConstructed DFS-BASED algorithm to obtain topological ordering for DAG\n")
    # Hold how many node are there at total
    totalNode = len(graphAdjList)
    # Send generated graph to topologicalSort() function, as adj list
    topologicalSort(graphAdjList, totalNode)
    #printing the -stack
    reverse = stack[::-1] #reversing using list slicing
    print("Ordering : ")
    for i in reverse:
        print(i, "->", end = ' ') 

def DriverFor_1stQ_b():
    print("\n\nConstructed NON-DFS-BASED algorithm to obtain topological ordering for DAG\n")
    # Hold how many node are there at total
    totalNode = len(graphAdjList)
    # Create an queue and enqueue all vertices with indegree 0
    q=[]
    order = []
    # in degree: number of incoming edges
    in_degree = {u : 0 for u in graphAdjList}
   
    setIndegree(in_degree)
    addIndegree(in_degree, q)

    # until queue has elements do the following...
    dequeue(q, order, in_degree)

    # Be sure it is DAG
    if len(order) != len(in_degree):
        print("\nNot a DAG\n")
    else:
        print("Ordering : ")
        for i in order:
            print(i, "->", end = ' ')

def DriverFor_2ndQ():
    a = 5
    n = 13
    print("\nCalculating ", a, "^", n, ":\n")
    logResult = logarithmicPow(a, n)
    print(logResult)
    
def DriverFor_3rdQ():
    # Prepare a sudoku board that is properly generated
    board = [
    "6..874.1.",
     "..9.36...",
     "...19.8..",
     "7946.....",
     "..1.894..",
     "...41..69",
     ".7..5..9.",
     ".539.76..",
     "9.2.61.47"
    ]
    print("Coming board is: ")
    printBoard(board)
    for index,line in enumerate(board):
        board[index] = list(line)
    isAlreadyDone(board)
    sudoku(board)
    print("\n\nSOLVED SUDOKU\n")
    printBoard(board)    

##########################################################################################################
#  CustomInput Part
##########################################################################################################

def CustomInputFor_1stQ():
    # First generate a graph
    # We can use dictionary to represent a graph 
    graph = { }
    vertexNum = input("How many vertex are there in your graph?")
    for i in range(int(vertexNum)):
        key_ = input("vertex: ")
        val_ = input("edge: ")
        graph[key_] = val_
       
    # Print the graph as list format
    print("\nYour graph is: \n")
    for key, val in graph.items():
        graphAdjList[key] = val
        print(f"{key}-->{val}")

    # Add graph to the list and
    # set all nodes as unvisited
    for key, val in graph.items():
        graphAdjList[key] = val
        visited[key] = 0 # mark them all as unvisited at the beginning
    DriverFor_1stQ_a()
    DriverFor_1stQ_b()

def CustomInputFor_2ndQ():
    a = input("Base: ")
    a = int(a)
    n = input("Exponent: ")
    n = int(n)
    print("\nCalculating ", a, "^", n, ":\n")
    logResult = logarithmicPow(a, n)
    print(logResult)
    
def CustomInputFor_3rdQ():
    # Prepare a sudoku board that is properly generated
    board = [ ]
    for i in range(9):
        print("Type the ", i, "th row")
        row = input()
        board.append(row)
        
    print("Coming board is: ")
    printBoard(board)
    for index,line in enumerate(board):
        board[index] = list(line)
    isAlreadyDone(board)
    sudoku(board)
    print("\n\nSOLVED SUDOKU\n")
    printBoard(board)

##########################################################################################################
#  Functions Part
##########################################################################################################
    
# Question-1 Functions ##############################

def dfs(g, s, totalNode):
    visited[s] = 1
    for v in g[s]:
        if not visited[v]:
            dfs(g, v, totalNode)
    finishingTime[s] = totalNode
    totalNode = totalNode - 1
    stack.append(s)

def topologicalSort(g, totalNode):
    for v in g:
        if not visited[v]:
            dfs(g, v, totalNode)

def addIndegree(in_degree, q):
    for v in in_degree.keys():
        if in_degree[v]==0:
            q.append(v)

def setIndegree(in_degree):
    for v, neigh in graphAdjList.items():
        in_degree.setdefault(v, 0)
        for n in neigh:
            in_degree[n] = in_degree.get(n, 0) + 1

def dequeue(q, order, in_degree):
    # until queue has elements do the following...
    while q:
        vertex = q.pop()
        order.append(vertex)
        for n in graphAdjList.get(vertex, []):
            in_degree[n] = in_degree[n] - 1
            if in_degree[n] == 0:
                q.append(n)

# End of the Question-1 Functions ##############################

# Question-2 Functions ##############################

def logarithmicPow(a, n):
    # reaching 0 in the exponent is the base case of our recursive function
    if n == 0:
        return 1
    # After dividing the exponent by 2, if it still can be divided into 2, continue dividing.
    logarithmic_pow = logarithmicPow(a, int(n/2))
    if (int(n) % 2) == 0:
        return logarithmic_pow * logarithmic_pow
    return logarithmic_pow * logarithmic_pow * a 

# End of the Question-2 Functions ##############################

# Question-3 Functions ##############################

def isAlreadyDone(board):
    easyFill(board)    
    if isComplete(board):
        return True   

def sudoku(board):
    i = 0
    j = 0
    # Starting from (0,0) traverse the board and find unfilled cells
    for index_row,row in enumerate(board):
        for index_col,col in enumerate(row):
            if col == ".":
                i = index_row
                j = index_col
                
    # We're trying a number each time, until a proper one is find.
    # But while doing that, we shouldn't change the previous version of the board, in case we want to undo changes
    # = is not made copies, so that something like .clone() in the Java is needed, which is deepcopy() in Python
    possibilities = getPossibilities(i,j, board)
    # if there is no possibility, getPossibilities() func will return false
    # and false is not iterable. To prevent this, before iterate on, control it is not false
    if possibilities != False:
        for number in possibilities:
            boardCopy = copy.deepcopy(board)
            board[i][j] = number
            result = sudoku(board)
            if result == True:
                return True
            else:
                board = copy.deepcopy(boardCopy)
    return False

def easyFill(board):
    while True:
        flag = False
        for i in range(0,9):
            for j in range(0,9):
                possibilities = getPossibilities(i,j, board)
                if possibilities != False:
                    if len(possibilities) == 0:
                        print("All possible moves are done")
                    if len(possibilities) == 1:
                        board[i][j] = possibilities[0]
                        flag = True        
        if flag == False:
            return
                
def getPossibilities(i,j, board):
    # Be sure a non-dot variable didn't come
    if board[i][j] != ".":
        return False
        
    # "possibilities" are a set. If value is possible, add the element to the set. If not, remove element from the set. 
    possibilities = {str(n) for n in range(1,10)}
    for val in board[i]:
        possibilities = possibilities - set(val)
    for idx in range(0,9):
        possibilities = possibilities - set( board[idx][j] )
    # reach one of the mini boards inside sudoku
    mini_i_index = int(i / 3) 
    mini_i_index = mini_i_index * 3
    mini_j_index = int(j / 3) 
    mini_j_index = mini_j_index * 3
    
    miniBoard = board[mini_i_index:mini_i_index+3]
    for idx,row in enumerate(miniBoard):
        miniBoard[idx] = row[mini_j_index:mini_j_index+3]
    for row in miniBoard:
        for col in row:
            possibilities = possibilities - set(col)
    return list(possibilities)

def printBoard(board):
    for row in board:
        for col in row:
            print(col, end="")
        print("")
        
def isComplete(board):
    for row in board:
        for col in row:
            # Any . must be filled to complete the game. Otherwise, game will be continue
            if (col == "."):
                return False   
    # If no . remains, that means game is completed.
    return True

# End of the Question-3 Functions ##############################


def main():
    choose = input("Choose the option you want to perform\n"
          "1- Run Driver function for all 3 question\n"
          "2- Test functions with custom input\n:")
    print("choose: ", choose)
    if choose == '1':
        DriverFor_1stQ()
        print("\n********************* Question - 1a ********************* ")
        DriverFor_1stQ_a()
        print("\n********************* Question - 1b ********************* ")        
        DriverFor_1stQ_b()
        print("\n********************* Question - 2 ********************* ")
        DriverFor_2ndQ()
        print("\n********************* Question - 3 ********************* ")
        DriverFor_3rdQ()

    if choose == '2':
        print("\n********************* Question - 1 ********************* ")
        CustomInputFor_1stQ()
        print("\n********************* Question - 2 ********************* ")
        CustomInputFor_2ndQ()
        print("\n********************* Question - 3 ********************* ")
        CustomInputFor_3rdQ()

main()