import math
import random

class NodeLL:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        # Set the list's head to None at the beginning.
        self.head = None
        self.length = 0
    
    def add_at_index(self, data, index):
        # Make a new node using the provided data.
        new_node = NodeLL(data, None)

        # Make the new node the list's head and set it to point to itself if the list is empty.
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        # Navigate the list until the node at the index preceding the requested index is located if the list is not empty.
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
                # If the head is reached before the specified index, the index is out of range
                if curr == self.head:
                    raise IndexError("Index out of range")
            # Now we can insert the new node 
            new_node.next = curr.next
            curr.next = new_node
        # Increment the length of the list
        self.length += 1


##########################################################################################################
#  Driver Part
##########################################################################################################

def DriverFor_1stQ():
    # To easy-follow the result, I use a small-sized board. It starts from 1, due to board size cannot be 0.
    # Generate "a" random integer between 1-10
    rowA = random.randint(1,10)
    rowB = random.randint(1,10)
    # board = generateBoard(rowA, rowB)
    points = useGeneratedBoard()
    # traversePaths(board)
    maximum_possible_score_tree(points)
    

def DriverFor_2ndQ():
    arr = [4, 1, 10, 8, 7, 12, 9, 2, 15]
    print("Array: ", arr, "\nlow: 0\nhigh: ", len(arr), "\nk: ", math.ceil(len(arr) / 2), "\n")
    Quickselect(arr, 0, len(arr), math.ceil(len(arr) / 2))
    
def DriverFor_3rdQ(): 
    playerNum = 7
    c_llist = CircularLinkedList()

    # assign all player with 0, at the beginning
    for i in range(playerNum):
        c_llist.add_at_index(0, i)
    print("PART A:")
    eliminatePlayerGame(c_llist)
    print("\nPART B:")
    eliminatePlayerGame_recursion(c_llist, None, 0)


##########################################################################################################
#  CustomInput Part
##########################################################################################################

def CustomInputFor_1stQ():
    rowA = int(input("size of the rowA: "))
    rowB = int(input("size of the rowB: "))
    board = generateBoardCustom(rowA, rowB)
    maximum_possible_score_tree(board)


def CustomInputFor_2ndQ(): 
    arrSize = int(input("Size of the array: "))
    arr = [0] * arrSize
    for i in range(0, arrSize):
        arr[i] = int(input("Enter value for element:"))
    print("Array: ", arr, "\nlow: 0\nhigh: ", len(arr), "\nk: ", math.ceil(len(arr) / 2), "\n")
    Quickselect(arr, 0, len(arr), math.ceil(len(arr) / 2))
    
def CustomInputFor_3rdQ():
    playerNum = int(input("How many player are there? "))
    c_llist = CircularLinkedList()

    # assign all player with 0, at the beginning
    for i in range(playerNum):
        c_llist.add_at_index(0, i)

    print("PART A:")
    eliminatePlayerGame(c_llist)
    print("\nPART B:")
    eliminatePlayerGame_recursion(c_llist, None, 0)


##########################################################################################################
#  Functions Part
##########################################################################################################
    
# Question-1 Functions ##############################
def LomutoPartition(A, low, high):
    # Partitions subarray by Lomuto’s algorithm using ﬁrst element as pivot
    # Input: A subarray A[l..r] of array A[0..n − 1], deﬁned by its left and right indices l and r (l ≤ r)
    # Output: Partition of A[l..r] and the new position of the pivot

    p = A[low]
    s = low
    for i in range(low+1, high):
        # print("\ns: ", s, "  i: ", i)
        if A[i] < p:
            s = s + 1 
            A[i], A[s] = A[s], A[i]
    A[low], A[s] = A[s], A[low]
    return s

def Quickselect(A, low, high, k):
# Solves the selection problem by recursive partition-based algorithm
# Input: Subarray A[l..r] of array A[0..n − 1] of orderable elements and integer k (1 ≤ k ≤ r − l + 1)
# Output: The value of the kth smallest element in A[l..r]
    #print("Arr: ", A, "\nlow: ", low, "\nhigh: ", high, "\nk: ", k, "\n")
    s = LomutoPartition(A, low, high) 
    #print("\nsQ: ", s, "\nk= ", k)
    if s == (k - 1): 
        print("Median for array ", A, " is: ", A[s])
        return A[s]
    elif s > (low + k - 1): 
        Quickselect(A, low, s-1, k)
    else: 
        Quickselect(A, s+1, high, k)
# End of the Question-1 Functions ##############################

# Question-2 Functions ##############################

def generateBoard(rowA, rowB):
    rowArr = [[0 for x in range(rowB)] for y in range(rowA)] 
    for i in range(0, rowA):
        for j in range(0, rowB):
            cell = random.randint(1,100)
            rowArr[i][j] = cell
    print(rowArr)
    return rowArr

def generateBoardCustom(rowA, rowB):
    rowArr = [[0 for x in range(rowB)] for y in range(rowA)] 
    for i in range(0, rowA):
        for j in range(0, rowB):
            cell = int(input("Enter value:"))
            rowArr[i][j] = cell
    print(rowArr)
    return rowArr

def useGeneratedBoard():
    T = [[25, 30, 25], [45, 15, 11], [1, 88, 15], [9,4, 23]]
    for r in T:
        for c in r:
            print(c,end = " ")
        print()
    return T

# def traversePaths(board):
 
def maximum_possible_score(points):
  # Get the dimensions of the points array
  n = len(points)
  m = len(points[0])

  # Initialize the 2D array to store the maximum possible scores
  dp = [[0 for _ in range(m)] for _ in range(n)]

  # Initialize the first element of the array to the value at coordinate A1B1
  dp[0][0] = points[0][0]

  # Initialize a 2D array to store the path taken
  path = [[None for _ in range(m)] for _ in range(n)]

  # Iterate through the array from left to right and top to bottom
  for i in range(n):
    for j in range(m):
      # Calculate the maximum possible score by taking the maximum of the two
      # possible moves from the current coordinate
      if i > 0 and j > 0:
        if dp[i][j-1] > dp[i-1][j]:
          dp[i][j] = dp[i][j-1] + points[i][j]
          path[i][j] = (i, j-1)
        else:
          dp[i][j] = dp[i-1][j] + points[i][j]
          path[i][j] = (i-1, j)
      elif i > 0:
        dp[i][j] = dp[i-1][j] + points[i][j]
        path[i][j] = (i-1, j)
      elif j > 0:
        dp[i][j] = dp[i][j-1] + points[i][j]
        path[i][j] = (i, j-1)

  # Initialize a list to store the coordinates of the path taken
  coordinates = [(n-1, m-1)]

  # Follow the path taken from the final position back to the starting position
  x, y = n-1, m-1
  while path[x][y] is not None:
    x, y = path[x][y]
    coordinates.append((x, y))

  # Reverse the list of coordinates to get the path taken from the starting position
  # to the final position
  coordinates = coordinates[::-1]

  # Print the path taken
  print("Path taken:")
  for i, j in coordinates:
    print(f"({i}, {j})")

  # Return the final element of the array as the maximum possible score
  print("res: ",dp[n-1][m-1])
  return dp[n-1][m-1]



from collections import deque

class Node:
  def __init__(self, x, y, value):
    self.x = x
    self.y = y
    self.value = value
    self.left = None # left child is considered as down
    self.right = None

def maximum_possible_score_tree(points):
  # Get the dimensions of the points array
  n = len(points)
  m = len(points[0])

  # Create a tree to represent the possible paths through the map
  root = Node(0, 0, points[0][0])
  queue = deque([root])

  # Use breadth-first search to traverse the tree and populate it with the possible paths
  while queue:
    node = queue.popleft()

    # Check if we can move to the right
    if node.y < m-1:
      # Create a new node for the right position and add it to the tree
      right = Node(node.x, node.y+1, node.value + points[node.x][node.y+1])
      node.right = right
      queue.append(right)

    # Check if we can move down
    if node.x < n-1:
      # Create a new node for the down position and add it to the tree
      down = Node(node.x+1, node.y, node.value + points[node.x+1][node.y])
      node.left = down
      queue.append(down)

  # Use depth-first search to find the maximum value in the tree
  stack = [root]
  max_value = root.value
  while stack:
    node = stack.pop()

    # Update the maximum value if necessary
    max_value = max(max_value, node.value)

    # Add the right and down children to the stack if they exist
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)

  # Return the maximum value found
  print("max_value: ", max_value)
  return max_value

# End of the Question-2 Functions ##############################

# Question-3 Functions ##############################

def eliminatePlayerGame(players):
    # Check if the list is empty
    if not players.head:
        return

    # Start at the head of the list
    curr = players.head
    index = 0

    # Continue until only one element with a value of 0 is left

    while count_ones(players) != (players.length-1):
        # If the current element is 0, set the next non-zero element to 1
        if curr.data == 0:
            next_zero = curr.next
            next_index = (index + 1) % players.length
            while next_zero.data == 1:
                next_zero = next_zero.next
                next_index = (next_index + 1) % players.length
            next_zero.data = 1
            # Print the statement
            print(f"P{index+1} eliminates P{next_index+1}\n")
            #curr.next = next_non_zero
            curr = curr.next
        # If the current element is 1, move to the next element
        else:
            curr = curr.next
        index = (index + 1) % players.length

    if index == 0:
        index = players.length
    print(f"P{index} is the winner\n")

def eliminatePlayerGame_linear(players):
    # Check if the list is empty
    if not players.head:
        return

    # use a dictionary to store the number of 1s in the list, to make complexity O(n)
    # Create a dictionary to store the count of 1s in the list
    ones_count = {}

    # Start at the head of the list
    curr = players.head
    index = 0

    # Continue until only one element with a value of 0 is left
    while sum(ones_count.values()) < players.length - 1:
        # If the current element is 0, set the next non-zero element to 1
        if curr.data == 0:
            next_zero = curr.next
            next_index = (index + 1) % players.length
            find_first_zero(ones_count, next_zero, next_index, players.length)

            next_zero.data = 1

            # Update the count of 1s in the dictionary
            if next_index in ones_count:    # check if next_index variable is in the dictionary
                ones_count[next_index] += 1
            else:
                ones_count[next_index] = 1

            print(f"P{index+1} eliminates P{next_index+1}\n")
            #curr.next = next_non_zero
            curr = curr.next
        # If the current element is 1, move to the next element
        else:
            curr = curr.next
        index = (index + 1) % players.length

    if index == 0:
        index = players.length
    print(f"P{index} is the winner\n")

def find_first_zero(ones_count, next_zero, next_index, mod):
    i = 0
    for i, value in ones_count.items():
        if value == 0:
            return i
        else:
            find_first_zero(ones_count, next_zero.next, (next_index + 1) % mod, mod)


def count_ones(clist):
    # Check if the list is empty
    if not clist.head:
        return 0

    # Start at the head of the list
    curr = clist.head
    count = 0

    # Count the number of nodes with a value of 1
    while curr.next != clist.head:
        if curr.data == 1:
            count += 1
        curr = curr.next

    # Check the last node
    if curr.data == 1:
        count += 1

    return count

def eliminatePlayerGame_recursion(players, curr, index):
    # Check if the list is empty
    if not players.head:
        return

    # Initialize the current node and index if they are not provided
    if curr is None:
        curr = players.head
    if index == 0:
        index = 0

    # Continue until only one element with a value of 0 is left
    if count_ones(players) != (players.length-1):
        # If the current element is 0, set the next non-zero element to 1
        if curr.data == 0:
            next_zero = curr.next
            next_index = (index + 1) % players.length
            while next_zero.data == 1:
                next_zero = next_zero.next
                next_index = (next_index + 1) % players.length
            next_zero.data = 1
            # Print the statement
            print(f"P{index+1} eliminates P{next_index+1}\n")
            #curr.next = next_non_zero
            curr = curr.next
        # If the current element is 1, move to the next element
        else:
            curr = curr.next
        index = (index + 1) % players.length

        # Recursively call the function with the updated values of curr and index
        eliminatePlayerGame_recursion(players, None, 0)
    else:
        if index == 0:
            index = players.length
        print(f"P{index} is the winner\n")

# End of the Question-3 Functions ##############################


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

    if choose == '2':
        print("\n********************* Question - 1 ********************* ")
        CustomInputFor_1stQ()
        print("\n********************* Question - 2 ********************* ")
        CustomInputFor_2ndQ()
        print("\n********************* Question - 3 ********************* ")
        CustomInputFor_3rdQ()

main()