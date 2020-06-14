from tkinter import *

root = Tk()
root.geometry("1350x750+0+0")
root.title("Morski Shah")
root.configure(background = "olivedrab")

Tops = Frame (root, bg = "darkorange", pady = 2, width = 1350, height = 100, relief = RIDGE) 
Tops.grid(row = 0, column = 0)

lblTitle = Label (Tops, font = ("black",50, "bold"), text = "Morski Shah", bd = 21, bg = "olivedrab", fg = "white", justify=CENTER) 
lblTitle.grid(row = 0, column = 0)

MainFrame = Frame (root, bg = "darkorange", bd = 10, width = 1350, height = 600, relief = RIDGE) 
MainFrame.grid(row = 1, column = 0)

LeftFrame = Frame(MainFrame, bd = 10, width = 750, height = 500, pady = 2, padx = 10, bg = "olivedrab", relief=RIDGE) 
LeftFrame.pack(side = LEFT)

RightFrame = Frame(MainFrame, bd = 10, width = 560, height = 500, padx = 10, pady = 2, bg = "olivedrab", relief=RIDGE) 
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd = 10, width = 560, height = 200, padx = 10, pady = 2, bg = "olivedrab" , relief=RIDGE) 
RightFrame1.grid(row = 0, column = 0)

RightFrame2 = Frame(RightFrame, bd = 10, width = 560, height = 200, padx = 10, pady = 2, bg = "darkorange", relief=RIDGE) 
RightFrame2.grid (row = 1, column = 0)

PlayerX=IntVar() 
PlayerO=IntVar()

PlayerX.set(0) 
PlayerO.set(0)

buttons = StringVar ()
click = True

def igra (buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        logic()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        logic()


def logic():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="red")
        button2.configure(background="red")
        button3.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="red")
        button5.configure(background="red")
        button6.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="red")
        button8.configure(background="red")
        button9.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="red")
        button5.configure(background="red")
        button9.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="red")
        button5.configure(background="red")
        button7.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="red")
        button4.configure(background="red")
        button7.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="red")
        button5.configure(background="red")
        button8.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        
    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="red")
        button6.configure(background="red")
        button9.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="red")
        button2.configure(background="red")
        button3.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="red")
        button5.configure(background="red")
        button6.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="red")
        button8.configure(background="red")
        button9.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="red")
        button5.configure(background="red")
        button9.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="red")
        button5.configure(background="red")
        button7.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="red")
        button4.configure(background="red")
        button7.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)

    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="red")
        button5.configure(background="red")
        button8.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        
    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="red")
        button6.configure(background="red")
        button9.configure(background="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)


def iztrii():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background="white")
    button2.configure(background="white")
    button3.configure(background="white")
    button4.configure(background="white")
    button5.configure(background="white")
    button6.configure(background="white")
    button7.configure(background="white")
    button8.configure(background="white")
    button9.configure(background="white")

    

def NI():
    iztrii()
    PlayerX.set (0) 
    PlayerO.set (0)      






lblPlayerX = Label(RightFrame1, font=("black", 40, "bold"), text="Igrach 1:", padx=2, pady=2, bg="olivedrab")
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX=Entry(RightFrame1, font=("black",40, "bold"), bd=2, fg="black", textvariable = PlayerX, width=14, justify=LEFT).grid(row=0, column=1)


lblPlayerO = Label(RightFrame1, font=("black", 40, "bold"), text = "Igrach 2: ", padx = 2, pady = 2, bg = "olivedrab")
lblPlayerO.grid(row = 1, column = 0, sticky=W)
txtPlayerO=Entry(RightFrame1, font=("black",40, "bold"), bd = 2, fg = "black", textvariable = PlayerO, width = 14, justify=LEFT).grid(row = 1, column = 1)


btnReset = Button(RightFrame2, text="Iztrii", font=("Times 26 bold"), height = 3, width=8, bg = "white", command = iztrii) 
btnReset.grid (row = 0, column = 0)

btnNewgame = Button(RightFrame2, text="Nova Igra", font=("Times 26 bold"), height = 3, width=8, bg = "white", command = NI) 
btnNewgame.grid (row = 0, column = 1)








button1 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height = 3, width=8, bg = "white", command=lambda:igra(button1)) 
button1.grid (row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height = 3, width=8, bg = "white", command=lambda:igra(button2)) 
button2.grid (row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height = 3, width=8, bg ="white", command=lambda:igra(button3)) 
button3.grid (row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height = 3, width=8, bg ="white", command=lambda:igra(button4))  
button4.grid (row = 2, column = 0, sticky = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height = 3, width=8, bg ="white", command=lambda:igra(button5)) 
button5.grid (row = 2, column = 1, sticky = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height = 3, width=8, bg = "white", command=lambda:igra(button6)) 
button6.grid (row = 2, column = 2, sticky = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=("times 26 bold"), height = 3, width=8, bg="white", command=lambda:igra(button7)) 
button7.grid (row = 3, column = 0, sticky = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height = 3, width=8, bg="white", command=lambda:igra(button8)) 
button8.grid (row = 3, column = 1, sticky = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height = 3, width=8, bg="white", command=lambda:igra(button9)) 
button9.grid (row = 3, column = 2, sticky = S+N+E+W)



root.mainloop()

