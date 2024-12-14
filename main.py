from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from time import strftime
# from datatime import datatime
from face_attendance import Attendance
from train import Train 
from face_detection  import Face_Detection_System
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root;
        self.root.geometry('1200x600')
        self.root.title("Face Recognition System")
        # IMg1
        img=Image.open(r"IMAGE/concept-face-recognition-software-hardware-concept-face-recognition-software-hardware-131454378.jpg")
        img=img.resize((450,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=100)

        # img2
        img1=Image.open(r"IMAGE/images (1).jpg")
        img1=img1.resize((450,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=100)
        # img3

        img2=Image.open(r"IMAGE/images (2).jpg")
        img2=img2.resize((450,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=100)

        # bgImage

        img3=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\pngtree-blue-face-recognition-technology-design-poster-background-image_195905.jpg")
        img3=img3.resize((1300,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1300,height=600)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE " ,font=('time new roman',28,'bold'),bg='white',fg='red');
        title_lbl.place(x=0,y=0,width=1300,height=40);

        # ------Time--------

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()







        # student Button
        img4=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\images (3).jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor='hand2')
        b1.place(x=130,y=70,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=('times new roman',12,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=130,y=255,width=207,height=38)

        # detect face button

        img5=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\1_DPNoWJ3Au35Fw58Sn2oj1w.png")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor='hand2',command=self.face_data)
        b1.place(x=430,y=70,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=('times new roman',12,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=430,y=255,width=207,height=38)

        # attendance face button
        img6=Image.open(r"IMAGE/face-recognition-personal-identification-collage.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor='hand2',command=self.attendance_data)
        b1.place(x=700,y=70,height=200)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=('times new roman',12,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=700,y=255,width=207,height=38)

        # help desk button

        img7=Image.open(r"IMAGE/7758834.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor='hand2',command=self.Help_data)
        b1.place(x=950,y=70,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.Help_data,font=('times new roman',12,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=950,y=255,width=207,height=38)

         # Train data
        img8=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\images (5).jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor='hand2')
        b1.place(x=130,y=315,height=200)

        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=('times new roman',12,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=130,y=500,width=207,height=38)

        # photo Face button

        img9=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\download (1).jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor='hand2',command=self.open_img)
        b1.place(x=430,y=315,height=200)

        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=('times new roman',12,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=430,y=500,width=207,height=38)

        # developer
        img10=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\images (6).jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor='hand2',command=self.devloper_data)
        b1.place(x=700,y=315,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.devloper_data,font=('times new roman',12,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=700,y=500,width=207,height=38)

        # Exit face button
        img11=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\download (2).jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor='hand2',command=self.ClickExit)
        b1.place(x=950,y=315,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.ClickExit,font=('times new roman',12,'bold'),bg='darkblue',fg='white')
        b1_1.place(x=950,y=500,width=207,height=38)

       
    #    ---------functions buttons-----------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window);




    # -----open img -------
    def open_img(self):
     os.startfile("data")

    # Exit 

    def ClickExit(self):

        self.ClickExit=tkinter.messagebox.askyesno("Face Recognition ","Are your sure exits this system",parent=self.root)
        if self.ClickExit>0:
            self.root.destroy()
        else:
            return 

    
    # ---train data buttton--------
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window);


    # ---Face Recognition System buttton--------
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Detection_System(self.new_window);

    # attendance sheet

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window);


    def devloper_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window);


    # help desk

    def Help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window);


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()