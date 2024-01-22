from tkinter import *

root = Tk()
root.title('MyWindow')
root.geometry('600x400')

def changecolor(*args):
    val1 = int(str_var1.get())
    val2 = int(str_var2.get())
    val3 = int(str_var3.get())
    if isinstance(val1, int):
        print(val1)
    if isinstance(val2, int):
        print(val2)
    if isinstance(val3, int):
        print(val3)
        
        


str_var1 = StringVar()
str_var1.trace_add('write', changecolor)

str_var2 = StringVar()
str_var2.trace_add('write', changecolor)

str_var3 = StringVar()
str_var3.trace_add('write', changecolor)

red = Entry(root, textvariable=str_var1)
green = Entry(root, textvariable=str_var2)
blue = Entry(root, textvariable=str_var3)

red.pack()
green.pack()
blue.pack()

root.mainloop()