import copy


# Create 8 number puzzle from input
def Gen_Puz():
    #Variables to handle input checking
    contentCheck = 0
    A = input()
    A_copy = copy.deepcopy(A)
    A_list = A_copy.split(" ")

    print("Enter the puzzle as a row")
    print("e.g 1 2 3 0 4 5 8 6 7 results in:")
    print("1 2 3")
    print("0 4 5")
    print("8 6 7")

    #loop to itterate through the list and ensure that it is all numbers from 0-8
    for i in range(0, len(A_list)):
        if A_list[i] == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            contentCheck = contentCheck + 1

    #Check that the approptiate number of entries were provided
    if contentCheck == 9:
        B = [int(i) for i in A.split()]
        return B
    else:
        print("Invalid puzzle please restart and try again")



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
def AddNode(Parent, Pf, iteration, child, j):
    Pdir = Pf[9:len(Pf)]
    c = 0
    b = StartLocation(Parent)
    U = Up(b, Parent)
    D = Down(b, Parent)
    L = Left(b, Parent)
    R = Right(b, Parent)
    if Parent != U:  # Check if node is new or same
        child = child + U + Pdir  # Append new node and its action set
        child.append("U")
        c = c + 1
    if Parent != D:
        child = child + D + Pdir
        child.append("D")
        c = c + 1
    if Parent != L:
        child = child + L + Pdir
        child.append("L")
        c = c + 1
    if Parent != R:
        child = child + R + Pdir
        child.append("R")
        c = c + 1
    return c + j, child, c  # Return total child nodes, nodes, nodes per parent



# BFS algorithm to reach goal node
def BFS(N):
    inv = 0

    explored = []  # Intialize variables
    Parent = N
    child = []
    num_parents = 1
    num_child = 0
    node_per_p = 0
    iteration = 0
    f = 0
    while f == 0:  # Loop to evaluate tree levels
        child.clear()
        for c in range(num_parents):  # Loop to access different node in a particular level
            p_list = Parent[(0 + c * (9 + iteration)):(iteration + 9 + c * (9 + iteration))]
            p_slice = p_list[0:9]
            if p_slice == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                f = 1
                explored.append(p_slice)
                break
            if not p_slice in explored:  # Check for child node if parent not in explored
                num_child, child, node_per_p = AddNode(p_slice, p_list, iteration, child, num_child)
                explored.append(p_slice)
        iteration += 1
        num_parents = int(len(child) / (9 + iteration))
        Parent = copy.deepcopy(child)
        print(" Explored Nodes", len(explored))

    print(" Solution Found.")


A = Gen_Puz()  # Prompting user to provide puzzle input
BFS(A)  # Passing the puzzle to BFS Algorithm
