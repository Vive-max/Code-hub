from tkinter import *
from tkinter import Entry

root = Tk()
root.title('guru')
root.geometry('600x300')

entry1 = Entry(root,bg='green')
entry1.pack()
#entry2 = Entry(root,bg='green')
#entry2 = pack()

button = Button(root,text='okk',bg='red')

button.pack()

root.mainloop()