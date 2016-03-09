
import spot
import tower
import road

class Board(object):
    


    def __init__(self, params):
        self.size=20
        self.board[self.size][self.size]
        for i in 20:
            for j in 20:
                self.board[i][j]=spot()
        self.noroad=True
            
    def add_tower(self,x,y):
        if(self.board[x][y]!=tower and self.board[x][y]!=road):
            self.board[x][y]=tower()
        
    def add_road(self,x,y):
        self.board[x][y]=road()
        if self.noroad:
            self.board[x][y].def_start()
            self.noroad=False
        
        