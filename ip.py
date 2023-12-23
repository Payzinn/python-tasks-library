from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.geometry('540x280')
root.resizable(False, False)
root.title('Твой IP')
root.config(bg='#7A97FB')

r = requests.get(r'http://jsonip.com')
# r = requests.get(r'https://ifconfig.co/json')
ip= r.json()['ip']
# print('Your IP is {}'.format(ip))

form_label_new = Label(root, text='Твой публичный IP:{}'.format(ip) , font = ('Jost', 20, 'bold'),bg = ('#7A97FB'))
form_label_new.pack(pady=15)

root.mainloop()

