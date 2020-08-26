from tkinter import* # Importing Tkinter

def ButtonClick(numbers):  # funtion for the Button clicks
    global operator   # naming 'operator' a global variable
    operator = operator +str(numbers) # converting number 
    text_input.set(operator)
    

def BtnClearDisplay(): 
    global operator
    operator = ""
    text_input.set("")

def BtnEqualsInput():
    global operator
    Sumup = str(eval(operator))
    text_input.set(Sumup)
    operator = ""
    
              
                                

calc = Tk()
calc.title("Simple Calculator")
operator = ""
text_input =StringVar()

textDisplay = Entry(calc,font=("gandugi",20, "bold"), textvariable=text_input, bd=30, insertwidth=4,
                                 bg="thistle", justify="right").grid(columnspan=4)


Button_7=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "7",command=lambda:ButtonClick(7)).grid(row=1,column=0)
            
Button_8=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "8",command=lambda:ButttonClick(8)).grid(row=1,column=1)

Button_9=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "9", command=lambda:ButttonClick(9)).grid(row=1,column=2)

Button_Addition=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "+",command=lambda:ButttonClick("+")).grid(row=1,column=3)

#==================================================================
Btn4=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "4",command=lambda:ButttonClick(4)).grid(row=2,column=0)

Btn5=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "5",command=lambda:ButttonClick(5)).grid(row=2,column=1)

Btn=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "6",command=lambda:ButttonClick(6)).grid(row=2,column=2)

Subtraction=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "-",command=lambda:ButttonClick("-")).grid(row=2,column=3)

#====================================================================
Btn1=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "1",command=lambda:ButttonClick(1)).grid(row=3,column=0)

Btn2=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "2",command=lambda:ButttonClick(2)).grid(row=3,column=1)

Btn3=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "3",command=lambda:ButttonClick(3)).grid(row=3,column=2)

Multiplication=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "*",command=lambda:ButttonClick("*")).grid(row=3,column=3)

#======================================================================
Btn0=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "0",command=lambda:ButttonClick(0)).grid(row=4,column=0)

BtnClear=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "C",command=ClearDisplayButton).grid(row=4,column=1)

BtnEquals=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "=",command=EqualsInputButton).grid(row=4,column=2)

BtnDivision=Button(calc,padx=16,bd=8, fg="black",font=("arial",20, "bold"),
            text = "/",command=lambda:BtnClick("/")).grid(row=4,column=3)



calc.mainloop()
