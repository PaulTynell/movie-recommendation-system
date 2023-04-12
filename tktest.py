#File: tktest.py
#Author: Jani Nurmi
#Desc: Testing for tkinter functions

from tkinter import *
import main

#Setup
master = Tk()
master.title("Movie recommendations")

#Size
master.geometry("500x400")


#Widgets
def myClick():
    clickLabel = Label(master, text="These are your movie recommendations:", font=("Arial", 14))
    clickLabel.grid(row=3, column=0)
    output = main.main()
    text = Text(master, height=13, width=61, font=("Arial", 10))
    text.insert(END, str(output))
    text.grid(row=4, column=0, sticky="nsew", pady=1)
    scrollbar = Scrollbar(master, command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

Label1 = Label(master, text="Movie recommendations", font=("Arial", 15))
Button1 = Button(master, text="Get my recommendation!", command=myClick, font=("Arial", 14))
Quit_Button = Button(master, text="Exit", font=("Arial", 10), command=master.quit)


#Inserts
Label1.grid(row=0, column=0, sticky="nsew", pady=3)
Button1.grid(row=2, column=0, pady=3)
Quit_Button.grid(row=5, column=0, pady=10)


#Configure the grid to center widgets
master.grid_rowconfigure(0, weight=0)
master.grid_rowconfigure(1, weight=0)
master.grid_columnconfigure(0, weight=1)



master.mainloop()