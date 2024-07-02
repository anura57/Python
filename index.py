#print("Hello World!")

# a=9
#if a==1:
    #print("a is 1")
#else:
    #print("This is error.")
from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry('37x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation=StringVar()
        self.entry_value=''
        Entry(width=18,bg='#fff', font=('Poppins', 28))

    root=Tk()
    root.mainloop()
