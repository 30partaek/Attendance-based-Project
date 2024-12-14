from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root;
        self.root.geometry('1200x600')
        self.root.title("Help Desk ")

       
        # image
        img1=Image.open(r"IMAGE/3659197.jpg")
        img1=img1.resize((1295,645),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=2,y=0,width=1295,height=645)


        title_lbl=Label(self.root,text="Help Desk " ,font=('time new roman',20,'bold'),bg='lightGreen',fg='blue');
        title_lbl.place(x=0,y=0,width=1300,height=25);

        dev_label=Label(f_lbl,text="Email:devHelp@gmail.com",font=("times new roman",20,"bold"),fg='green',bg="white")
        dev_label.place(x=480,y=200)

        




      





if __name__=="__main__":
      root=Tk()
      obj=Help(root)
      root.mainloop()