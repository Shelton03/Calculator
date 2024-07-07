import tkinter, customtkinter

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    result_text.delete(1.0,"end")
    result_text.insert(1.0, calculation)

def evaluate_function():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        result_text.delete(1.0,"end")
        result_text.insert(1.0, result)

    except:
        clear()
        result_text.insert(1.0,"Error")


def clear():
    result_text.delete(1.0,"end")
    

app = tkinter.Tk()
app.geometry("300x300")
result_text = tkinter.Text(app,height=2,width=16,padx=10,pady=8,font=("Arial",24),undo=True)
result_text.grid(columnspan=5)
app.title("Karma's Calculator")


#buttons
btnOne = tkinter.Button(app,text="1",border=3,command = lambda:add_to_calculation(1),width=4,font=("Arial",14))
btnOne.grid(row=2,column=1)

btnTwo = tkinter.Button(app,text="2",border=3,command = lambda:add_to_calculation(2),width=4,font=("Arial",14))
btnTwo.grid(row=2,column=2)


btnThree = tkinter.Button(app,text="3",border=3,command = lambda:add_to_calculation(3),width=4,font=("Arial",14))
btnThree.grid(row=2,column=3)


btnFour = tkinter.Button(app,text="4",border=3,command = lambda:add_to_calculation(4),width=4,font=("Arial",14))
btnFour.grid(row=3,column=1)


btnFive = tkinter.Button(app,text="5",border=3,command = lambda:add_to_calculation(5),width=4,font=("Arial",14))
btnFive.grid(row=3,column=2)


btnSix = tkinter.Button(app,text="6",border=3,command = lambda:add_to_calculation(6),width=4,font=("Arial",14))
btnSix.grid(row=3,column=3)


btnSeven = tkinter.Button(app,text="7",border=3,command = lambda:add_to_calculation(7),width=4,font=("Arial",14))
btnSeven.grid(row=4,column=1)


btnEight = tkinter.Button(app,text="8",border=3,command = lambda:add_to_calculation(8),width=4,font=("Arial",14))
btnEight.grid(row=4,column=2)


btnNine = tkinter.Button(app,text="9",border=3,command = lambda:add_to_calculation(9),width=4,font=("Arial",14))
btnNine.grid(row=4,column=3)


btnZero = tkinter.Button(app,text="0",border=3,command = lambda:add_to_calculation(0),width=4,font=("Arial",14))
btnZero.grid(row=5,column=2)

btnClear = tkinter.Button(app,text="Clear",border=3,command = lambda:clear(),width=4,font=("Arial",14))
btnClear.grid(row=6,column=1)

btnHstry = tkinter.Button(app,text="History",border=3,command = lambda:result_text.edit_undo(),width=5,font=("Arial",14))
btnHstry.grid(row=6,column=3)

btnEquals = tkinter.Button(app,text="=",border=3,command = evaluate_function,width=4,font=("Arial",14))
btnEquals.grid(row=6,column=2)


btnPar1 = tkinter.Button(app,text="(",border=3,command = lambda:add_to_calculation("("),width=4,font=("Arial",14))
btnPar1.grid(row=5,column=1)


btnPar2 = tkinter.Button(app,text=")",border=3,command = lambda:add_to_calculation(")"),width=4,font=("Arial",14))
btnPar2.grid(row=5,column=3)

btnAdd = tkinter.Button(app,text="+",border=3,command = lambda:add_to_calculation("+"),width=4,font=("Arial",14))
btnAdd.grid(row=2,column=4)


btnSub = tkinter.Button(app,text="-",border=3,command = lambda:add_to_calculation("-"),width=4,font=("Arial",14))
btnSub.grid(row=3,column=4)


btnMul = tkinter.Button(app,text="x",border=3,command = lambda:add_to_calculation("*"),width=4,font=("Arial",14))
btnMul.grid(row=4,column=4)


btnDiv = tkinter.Button(app,text=("/"),border=3,command = lambda:add_to_calculation("/"),width=4,font=("Arial",14))
btnDiv.grid(row=5,column=4)

btnDiv = tkinter.Button(app,text=("/"),border=3,command = lambda:add_to_calculation("/"),width=4,font=("Arial",14))
btnDiv.grid(row=5,column=4)

btnMod = tkinter.Button(app,text=("Mod"),border=3,command = lambda:add_to_calculation("%"),width=4,font=("Arial",14))
btnMod.grid(row=6,column=4)


app.maxsize(300,300)


app.mainloop()

