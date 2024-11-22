import copy

# Create 8 number puzzle from input
def Gen_Puz():
    checkA = []
    while checkA != [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print("Enter the puzzle as a row")
        print("e.g 1 2 3 0 4 5 8 6 7 results in:")
        print("1 2 3")
        print("0 4 5")
        print("8 6 7")
        try:
            A = [int(i) for i in input().split()]
            checkA = sorted(A)
            if checkA != [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                print("Invalid input")
        except:
            print("Invalid input")

    return A

# Find the movable tile
def StartLocation(N):
    for i in range(9):
        if N[i] == 0:
            return i  # Return Starting position in list

# Move up function that creates a new node
def Up(b, N):
    U = copy.deepcopy(N)
    if b > 2:
        U[b] = U[b - 3]  # Swap Tiles
        U[b - 3] = 0
    return U  # Return New Node

# Move down function that creates a new node
def Down(b, N):
    D = copy.deepcopy(N)
    if b < 6:
        D[b] = D[b + 3]  # Swap Tiles
        D[b + 3] = 0
    return D  # Return New Node

# Move left function that creates a new node
def Left(b, N):
    L = copy.deepcopy(N)
    if b != 0 and b != 3 and b != 6:
        L[b] = L[b - 1]  # Swap Tiles
        L[b - 1] = 0
    return L  # Return New Node

# Move right function that creates a new node
def Right(b, N):
    R = copy.deepcopy(N)
    if b != 2 and b != 5 and b != 8:
        R[b] = R[b + 1]  # Swap Tiles
        R[b + 1] = 0
    return R  # Return New Node

# Add Node to Child list and find number of childs per parent
def AddNode(Parent, stack):
    b = StartLocation(Parent)
    U = Up(b, Parent) #Check possible moves
    D = Down(b, Parent)
    L = Left(b, Parent)
    R = Right(b, Parent)

    if Parent != U:  # Check if node is new or same
        stack.append(U) # Push into stack
    if Parent != D:
        stack.append(D)
    if Parent != L:
        stack.append(L)
    if Parent != R:
        stack.append(R)
    return stack  # Return the stack with new nodes

# DFS algorithm to reach goal node
def DFS(N):
    stack = [N] # Initialize stack
    explored = []  # Initialize explored
    f = 0 # Flag for goal node
    while stack and f == 0:  # Loop to evaluate nodes
        currentNode = stack.pop()  # Pop the last node from the stack
        if currentNode == [0, 1, 2, 3, 4, 5, 6, 7, 8]: #Check goal node
            f = 1
            explored.append(currentNode)
            break
        if not currentNode in explored:  # Check for child node if parent not in explored
            stack = AddNode(currentNode, stack) #Add new node
            explored.append(currentNode)
        print("Explored Nodes:", len(explored))
    
    if f == 1:
        print("Solution Found.")
    else:
        print("No Solution.")

A = Gen_Puz()  # Prompting user to provide puzzle input
DFS(A)  # Passing the puzzle to DFS Algorithm
