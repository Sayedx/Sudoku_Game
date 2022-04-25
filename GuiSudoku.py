import tkinter as tk
from Algorithm import solver

root=tk.Tk()
root.title("Sudoku")
root.geometry("450x500")


label=tk.Label(root,text='Fill in the numbers and click solve please').grid(row=0,column=1,columnspan=10)

errLabel=tk.Label(root,text="",fg="red")
errLabel.grid(row=15,column=1,columnspan=10,pady=5)

solvLabel=tk.Label(root,text="",fg="green")
solvLabel.grid(row=15,column=1,columnspan=10,pady=5)

cells={}

def validate(P):
    out=(P.isdigit() or P=="")and len(P)<2
    return out

reg=root.register(validate)

def drawGrid3(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e= tk.Entry(root,width=5,bg=bgcolor,justify='center',validate="key",validatecommand=(reg,"%P"))
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(row+i+1,column+j+1)]=e
def drawGrid9():
    color="#d8edf7"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            drawGrid3(rowNo,colNo,color)
            if color=="#d8edf7":
                color="#dbfdf5"
            else:
                color="#d8edf7"

def clearV():
    errLabel.configure(text="")
    solvLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell=cells[(row,col)]
            cell.delete(0,"end")

def getV():
    board=[]
    errLabel.configure(text="")
    solvLabel.configure(text="")
    for row in range(2,11):
        rows=[]
        for col in range(1,10):
            val=cells[(row,col)].get()
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateV(board)
btn=tk.Button(root,command=getV,text="Solve",width=10)
btn.grid(row=20,column=1,columnspan=5,pady=20)


btn=tk.Button(root,command=clearV,text="Clear",width=10)
btn.grid(row=20,column=5,columnspan=5,pady=20)


def updateV(s):
    sol=solver(s)
    if sol !="no":
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")
                cells[(rows,col)].insert(0,sol[rows-2][col -1])
        solvLabel.configure(text="Sudoku Solved!")
    else:
        errLabel.configure(text="No solution exists for this sudoku")



drawGrid9()
root.mainloop()