from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root;
        self.root.geometry('1200x600')
        self.root.title("Developer ")

       
        # image
        img1=Image.open(r"IMAGE/representation-user-experience-interface-design.jpg")
        img1=img1.resize((1295,645),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=2,y=0,width=1295,height=645)


        title_lbl=Label(self.root,text="Developer" ,font=('time new roman',20,'bold'),bg='white',fg='blue');
        title_lbl.place(x=0,y=0,width=1300,height=25);




        # main frame

         # main frame
        main_frame=Frame(f_lbl,bd=2,bg='skyBlue')
        main_frame.place(x=700,y=30,width=450,height=500)

        img2=Image.open(r"c:\Users\PARTAEK YADAV\Downloads\pexels-thirdman-5060556.jpg")
        img2=img2.resize((400,650),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=100,y=40,width=300,height=300)

        # develo info

        dev_label=Label(main_frame,text="hello my name ,John",font=("times new roman",20,"bold"),fg='green',bg="white")
        dev_label.place(x=0,y=350)

        # dev_label=Label(main_frame,text="I am full stack Developer",font=("times new roman",20,"bold"),fg='green',bg="white")
        # dev_label.place(x=0,y=40)






if __name__=="__main__":
      root=Tk()
      obj=Developer(root)
      root.mainloop()