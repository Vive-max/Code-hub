#tkinter is module name
#pip install tk
from tkinter import *
#from PIL import ImageTK,Image
#from tkinter import ttk
root = Tk()
root.geometry('600x300')
#canvas=Canvas(root,width=300,height=100)
#image = ImageTK.photoImage(Image.open('C:\\Users\\admin\\pytho.png'))
#canvas.create_image(0,0,anchor=NW,image=Image)
#canvas.pack()

#show the title
label = Label(root,font=('calibri',31),text ='Wellcome in speakword App',bg='yellow')
label.pack()

#root1 = root(font=('calibri',32),text ='wellcome in speakword App',bg='yellow')
#root1.pack()
print('hello')

#win32 is a module names
from win32com.client import Dispatch
#functin define
def speak(user):
    user =User_input.get()
    speak = Dispatch('SAPI.Spvoice')
    speak.Speak(user)
    
#take input from user
User_input =Entry(root,font=('calibri',40),bg='pink')
User_input.pack()
c = Label(root,font=('calibri',20), text='Plz Enter a text',bg='magenta')
c.pack()
#answer=Text.print(user)
#answer.pack()
#if __name__ == '__main__':


#create a ok button
button = Button(root,text='Speak',font=('calibri',20),bg='cyan',command=lambda:speak(User_input))
button.pack(side=LEFT, fill=Y)

#create a exit button
button2=Button(root,text='Exit',font=('calibri',33),bg='red', command=quit)
button2.pack(side=RIGHT, fill=X )

root.mainloop()



