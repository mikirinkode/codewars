def is_solved(board):
    
    for row in board:
        zero = row.count(0)
        one = row.count(1)
        if (one == 3):
            return 1
        elif (zero == 3):
            return 0
        
        cols = {1: [], 0: []}
        for i in range(3):
            
            
            
        
        
    return -1