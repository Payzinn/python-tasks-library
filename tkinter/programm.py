from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('MyWindow')
root.geometry('600x400')

def changecolor(*args):
    color = []
    for var in (str_var1, str_var2, str_var3):
        value = var.get().strip()
        if value:
            if value.isdigit() and int(value) >= 0 and int(value) <= 255:
                color.append(int(value))
            else:
                messagebox.showinfo('Ошибка', 'Значение должно быть числом от 0 до 255')
        else:
            color.append(0)
    root.configure(bg= from_rgb(tuple(color)))
            
def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

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
