class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #validate the rows:
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s: 
                    return False 
                elif item != ".":
                    s.add(item) 

        #validate the columns:
        for x in range(9):
            z = set()
            for y in range(9):
                item = board[y][x]
                if item in z: 
                    return False 
                elif item != ".":
                    z.add(item)

        #validate the boxes:
        x = 0
        y = 0
        for w in range(9): 
            q = set()
            y += 3

            if w == 3 or w == 6: 
                x += 3
            
            if y >= 7: 
                y = 0 

            for a in range(3): #rows

                for s in range(3): #columns 
                    item = board[a+x][s+y]
                    if item in q:
                        return False 
                    elif item != ".":
                        q.add(item)
        
        return True 



        