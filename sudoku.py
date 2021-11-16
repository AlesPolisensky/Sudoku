
playground = [
    [0,0,0,0,7,0,0,9,0],
    [0,0,9,0,0,0,8,0,2],
    [0,6,5,8,9,0,0,4,0],
    [0,0,3,5,0,0,0,0,0],
    [5,0,1,0,0,0,2,0,7],
    [0,0,0,0,0,1,6,0,0],
    [0,4,0,0,3,2,0,1,0],
    [1,5,7,0,0,0,9,0,0],
    [0,3,0,0,5,0,0,0,0]
]

def solver(pg):
    find = empty_pos(pg)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10): #looping through values 1-10
        if is_valid(pg, i, (row, col)): # if the values are valid add them to playground
            pg[row][col] = i
            
            if solver(pg):
                return True
            
            pg[row][col] = 0
            
    return False
                

def is_valid(pg, num, position): #funtion to check if our board position is valid
    for i in range(len(pg[0])): #checks if row is valid
        if pg[position[0]][i] == num and position[1] != i:
            return False
        
    for i in range(len(pg)): #checks if column is valid
        if pg[i][position[1]] == num and position[0] != i:
            return False
        
    # checks if box is valid
    box_x = position[1] // 3
    box_y = position[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if pg[i][j] == num and (i, j) != position:
                return False
    
    return True
    

def print_playground(pg):
    for i in range(len(pg)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(pg[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(pg[i][j])
            else:
                print(str(pg[i][j]) + " ", end="")

def empty_pos(pg): #returns coordinates (row and column) of first empty position
    for row in range(len(pg)):
        for col in range(len(pg[0])):
            if pg[row][col] == 0:
                return row, col
            
    return None
    

solver(playground)
print("______________________________________")
print_playground(playground)
