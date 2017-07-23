#!/usr/bin/env python3
import tkinter
import numpy as np
import random,time,math
grid_arr=np.array([[2,2,32,16],[0,0,64,16],[512,32,16,8],[2,256,1024,4]])
class GridView:
    def __init__(self):
        self.top=tkinter.Tk()
        self.color_dict={
            2:"bisque",
            4:"bisque",
            8:"yellow",
            16:"light pink",
            32:"red",
            64:"orange red",
            128:"gold",
            256:"gold",
            512:"gold",
            1024:"light cyan",
            2048:"medium purple",
            4096:"plum1",
            8192:"RoyalBlue1"    
        }
#         self.top.geometry(size)
        self.score=0
        self.tiles=list(([],[],[],[]))
        for r in range(4):
            for c in range(4):
                self.tiles[r].append(tkinter.Label(self.top,text="%s" %1024,font=("Times", 36),\
                width=4,height=2,bg=self.color_dict[2048],fg='gray5'))
                self.tiles[r][c].grid(row=r,column=c,ipadx=5,ipady=5,padx=1,pady=1)
        self.scoreView=tkinter.Label(self.top,text="Score: %s" %self.score,font=("Times", 12),bg='green')
        self.scoreView.grid(row=5,column=0,columnspan=2,sticky=tkinter.W)
        self.loseView=tkinter.Label(self.top,text="",font=("Times", 12),bg='red')
        self.loseView.grid(row=6,column=0,columnspan=2,sticky=tkinter.W)
        tkinter.Button(self.top,text="quit",\
        command=self.quitGrid,bg='red',fg='white').grid(row=5,column=3,sticky=tkinter.E)
        tkinter.Button(self.top,text="restart",\
        command=self.initGame,bg='blue',fg='white').grid(row=6,column=3,sticky=tkinter.E)
        self.top.bind("<Up>", self.moveUP)
        self.top.bind("<Down>", self.moveDOWN)
        self.top.bind("<Left>", self.moveLEFT)
        self.top.bind("<Right>", self.moveRIGHT)
        self.lose=False
    
    def randomInsert(self):
        available_length=0
        available_cells=[]
        for r in range(4):
            for c in range(4):
                if self.grid_array[r,c]==0:
                    available_length+=1
                    available_cells.append({"r":r,"c":c})
        if available_length>0:
            insertCell=math.floor(random.random()*available_length)
        self.grid_array[available_cells[insertCell]["r"],available_cells[insertCell]["c"]]\
        =2 if random.random()<0.9 else 4
        self.updateDisplay()
    
    def initGame(self):
        self.grid_array=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.score=0
        self.lose=False
        self.randomInsert()
        self.randomInsert()
        self.grid_History=[self.grid_array.copy()]
        self.updateDisplay()
#         print(self.grid_History)
    
    def ifLose(self):
        for r in range(4):
            for c in range(4):
                if self.grid_array[r,c]==0:
                    return False
        for r in range(3):
            for c in range(4):
                if self.grid_array[r,c]==self.grid_array[r+1,c]:
                    return False
        for r in range(4):
            for c in range(3):
                if self.grid_array[r,c]==self.grid_array[r,c+1]:
                    return False
        return True
                    
    
    def setTest(self,arr):
        self.grid_array=arr
        self.updateDisplay()
        self.grid_History=[self.grid_array]
    
    def updateDisplay(self):
        if self.lose:
            self.loseView.config(text="You Lose!")
        self.scoreView.config(text="Score: %s" %self.score)
        for r in range(4):
            for c in range(4):
                if self.grid_array[r,c]>0:
                    self.tiles[r][c].config(text="%s" %self.grid_array[r,c],bg=self.color_dict[self.grid_array[r,c]],fg='gray5')
                else:
                    self.tiles[r][c].config(text="" %self.grid_array[r,c],bg='gray96',fg='gray96')
    
    def moveUP(self,event):
        for i in range(3):
            for c in range(4):
                for r in range(1,4):
                    if self.grid_array[r-1,c]==0:
                        self.grid_array[r-1,c],self.grid_array[r,c]=self.grid_array[r,c],self.grid_array[r-1,c]
        
        for c in range(4):
            for r in range(1,4):
                if self.grid_array[r-1,c]==self.grid_array[r,c]:
                    self.grid_array[r-1,c]=2*self.grid_array[r-1,c]
                    self.score+=self.grid_array[r,c]
                    self.grid_array[r,c]=0
        
        for c in range(4):
            for r in range(1,4):
                if self.grid_array[r-1,c]==0:
                    self.grid_array[r-1,c],self.grid_array[r,c]=self.grid_array[r,c],self.grid_array[r-1,c]
        if (self.grid_array!=self.grid_History[-1]).any() and not self.lose:
            self.randomInsert()
            self.grid_History.append(self.grid_array.copy())
            self.lose=self.ifLose()
            self.updateDisplay()
            
    
    def moveDOWN(self,event):
        for i in range(3):
            for c in range(4):
                for r in range(2,-1,-1):
                    if self.grid_array[r+1,c]==0:
                        self.grid_array[r+1,c],self.grid_array[r,c]=self.grid_array[r,c],self.grid_array[r+1,c]
        
        for c in range(4):
            for r in range(2,-1,-1):
                if self.grid_array[r+1,c]==self.grid_array[r,c]:
                    self.grid_array[r+1,c]=2*self.grid_array[r+1,c]
                    self.score+=self.grid_array[r,c]
                    self.grid_array[r,c]=0
        
        for c in range(4):
            for r in range(2,-1,-1):
                if self.grid_array[r+1,c]==0:
                    self.grid_array[r+1,c],self.grid_array[r,c]=self.grid_array[r,c],self.grid_array[r+1,c]
        if (self.grid_array!=self.grid_History[-1]).any() and not self.lose:
            self.randomInsert()
            self.grid_History.append(self.grid_array.copy())
            self.lose=self.ifLose()
            self.updateDisplay()
    
    def moveLEFT(self,event):
        for i in range(3):
            for r in range(4):
                for c in range(1,4):
                    if self.grid_array[r,c-1]==0:
                        self.grid_array[r,c-1],self.grid_array[r,c]=self.grid_array[r,c],self.grid_array[r,c-1]
        
        for r in range(4):
            for c in range(1,4):
                if self.grid_array[r,c-1]==self.grid_array[r,c]:
                    self.grid_array[r,c-1]=2*self.grid_array[r,c-1]
                    self.score+=self.grid_array[r,c]
                    self.grid_array[r,c]=0
        
        for r in range(4):
            for c in range(1,4):
                if self.grid_array[r,c-1]==0:
                    self.grid_array[r,c-1],self.grid_array[r,c]=self.grid_array[r,c],self.grid_array[r,c-1]
        if (self.grid_array!=self.grid_History[-1]).any() and not self.lose:
            self.randomInsert()
            self.grid_History.append(self.grid_array.copy())
            self.lose=self.ifLose()
            self.updateDisplay()
        
    def moveRIGHT(self,event):
        for i in range(3):
            for r in range(4):
                for c in range(2,-1,-1):
                    if self.grid_array[r,c+1]==0:
                        self.grid_array[r,c+1],self.grid_array[r,c]=self.grid_array[r,c],self.grid_array[r,c+1]
        
        for r in range(4):
            for c in range(2,-1,-1):
                if self.grid_array[r,c+1]==self.grid_array[r,c]:
                    self.grid_array[r,c+1]=2*self.grid_array[r,c+1]
                    self.score+=self.grid_array[r,c]
                    self.grid_array[r,c]=0
        
        for r in range(4):
            for c in range(2,-1,-1):
                if self.grid_array[r,c+1]==0:
                    self.grid_array[r,c+1],self.grid_array[r,c]=self.grid_array[r,c],self.grid_array[r,c+1]
        if (self.grid_array!=self.grid_History[-1]).any() and not self.lose:
            self.randomInsert()
            self.grid_History.append(self.grid_array.copy())
            self.lose=self.ifLose()
            self.updateDisplay()
    
    def viewGrid(self):
        self.top.mainloop()
    def quitGrid(self):
        self.top.destroy()

if __name__=="__main__":
    a=GridView()
    a.initGame()
    a.viewGrid()