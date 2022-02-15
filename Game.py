import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

class Game():
    def __init__(self):
        table = np.zeros((6,7),dtype=np.int8)
        self.table = pd.DataFrame(data=table)
        self.cols = [0,0,0,0,0,0,0]

    def check_cols(self,x):
        y = self.cols[x]
        self.cols[x] = y+1
        if y < 6:
            return 5-y
        if y>=5:
            print("Column full")
            return None

    def play(self,x,side):
        sit = False
        if side == "x":
            y = self.check_cols(x)
            if y != None:
                self.table.iloc[y, self.table.columns.get_loc(x)] = "x"
        if side == "y":
            y = self.check_cols(x)
            if y != None:
                self.table.iloc[y, self.table.columns.get_loc(x)] = "y"
        sit = self.check_winner()
        if sit == True:
            self.show()
            return True
        self.show()

    def yatay_sıra_komb(self):
        main = []
        b = []
        for y in range(6): 
            q = -1
            for i in range(4):
                x = q
                for koo in range(4): 
                    x = x+1
                    b.append(self.table.iloc[y, self.table.columns.get_loc(x)])
                q = q+1
                main.append(b)
                b = []
        return self.check(main)
    def dikey_sıra_komb(self):
        main = []
        b = []
        for x in range(7): 
            q = -1
            for aaa in range(3):
                y = q
                for aaaa in range(4): 
                    y = y+1
                    b.append(self.table.iloc[y, self.table.columns.get_loc(x)])
                q = q+1
                main.append(b)
                b = []
        return self.check(main)
    def diagonal_sıra_komb(self):
        main = []
        b = []
        for sat in range(3):
            for sut in range(4):
                x = sut
                y = sat
                for i in range(4):
                    b.append(self.table.iloc[y, self.table.columns.get_loc(x)])
                    x = x+1
                    y = y+1
                main.append(b)
                b = []
        for sat in range(3):
            for sut in range(6,2,-1):
                x = sut
                y = sat
                for i in range(4):
                    b.append(self.table.iloc[y, self.table.columns.get_loc(x)])
                    x = x-1
                    y = y+1
                main.append(b)
                b = []
        return self.check(main)
    def check(self,main):
        numx = 0
        numy = 0
        for cor in main:
            for i in cor:
                if i == "x":
                    numx += 1
                if i == "y":
                    numy += 1
            if numx == 4:
                return (True,False)
                break
            if numy == 4:
                return (False,True)
                break
            else:
                numx = 0
                numy= 0

        return (False,False)
    def check_winner(self):
        x1, y1 = self.yatay_sıra_komb()
        x2, y2 = self.dikey_sıra_komb()
        x3, y3 = self.diagonal_sıra_komb()
        if x1 == True or x2 == True or x3 == True:
            print("Player X has won the game.")
            return True
        if y1 == True or y2 == True or y3 == True:
            print("Player Y has won the game.")
            return True
        else:
            print("Next player")
        
    def show(self):
        print(self.table)
            