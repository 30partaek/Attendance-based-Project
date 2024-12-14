from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x625')
        self.root.title("Attendance")


        # ---variables----

        self.var_atten_id=StringVar();
        self.var_atten_roll=StringVar();
        self.var_atten_name=StringVar();
        self.var_atten_dep=StringVar();
        self.var_atten_time=StringVar();
        self.var_atten_date=StringVar();
        
        self.var_atten_attendance=StringVar();


         # img1
        img=Image.open(r"IMAGE/pexels-pavel-danilyuk-8423046.jpg")
        img=img.resize((636,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=4,y=0,width=636,height=150)

        #img2
        img_1=Image.open(r"IMAGE/pexels-pavel-danilyuk-8423092.jpg")
        img_1=img_1.resize((636,150),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        f_lbl=Label(self.root,image=self.photoimg_1)
        f_lbl.place(x=643,y=0,width=636,height=150)


        img3=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\pngtree-blue-face-recognition-technology-design-poster-background-image_195905.jpg")
        img3=img3.resize((1276,496),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=1,y=152,width=1276,height=495)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM " ,font=('time new roman',20,'bold'),bg='ghostwhite',fg='blue');
        title_lbl.place(x=1,y=0,width=1276,height=20);

        # main frame
        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=2,y=23,width=1268,height=465)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance",font=("times new roman",12,"bold"))
        Left_frame.place(x=2,y=3,width=636,height=450)



        # Add image left

        img_left=Image.open(r"IMAGE/istockphoto-2075585830-1024x1024.jpg")
        img_left=img_left.resize((308,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=7,y=0,width=308,height=120)


        img_left_1=Image.open(r"IMAGE/istockphoto-1555679895-1024x1024.jpg")
        img_left_1=img_left_1.resize((308,120),Image.ANTIALIAS)
        self.photoimg_left_1=ImageTk.PhotoImage(img_left_1)

        f_lbl=Label(Left_frame,image=self.photoimg_left_1)
        f_lbl.place(x=320,y=0,width=308,height=120)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg='white')
        left_inside_frame.place(x=2,y=124,width=630,height=400)

        # label and Entry


        #attendance Id

        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",11,"bold"),bg='white')
        attendanceId_label.grid(row=0,column=0,padx=8,pady=8,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",11,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=8,sticky=W);

        # Name
        name_label=Label(left_inside_frame,text="Name:",font=("comicsansns",11,"bold"),bg='white')
        name_label.grid(row=0,column=2,padx=8,pady=8,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("comicsansns",11,"bold"))
        name_entry.grid(row=0,column=3,padx=5,pady=8,sticky=W);


        #ROll

        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",11,"bold"),bg='white')
        roll_label.grid(row=1,column=0,padx=8,pady=8,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",11,"bold"))
        roll_entry.grid(row=1,column=1,padx=5,pady=8,sticky=W);

        # Department
        Department_label=Label(left_inside_frame,text="Department:",font=("comicsansns",11,"bold"),bg='white')
        Department_label.grid(row=1,column=2,padx=8,pady=8,sticky=W)

        Department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("comicsansns",11,"bold"))
        Department_entry.grid(row=1,column=3,padx=5,pady=8,sticky=W);

        #Time

        Time_label=Label(left_inside_frame,text="Time:",font=("times new roman",11,"bold"),bg='white')
        Time_label.grid(row=2,column=0,padx=8,pady=8,sticky=W)

        Time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",11,"bold"))
        Time_entry.grid(row=2,column=1,padx=5,pady=8,sticky=W);

        # Date
        Date_label=Label(left_inside_frame,text="Date:",font=("comicsansns",11,"bold"),bg='white')
        Date_label.grid(row=2,column=2,padx=8,pady=8,sticky=W)

        Date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("comicsansns",11,"bold"))
        Date_entry.grid(row=2,column=3,padx=5,pady=8,sticky=W);
        

        #Attendance Status
        Attendance_status_label=Label(left_inside_frame,text="Attendance_status:",font=("times new roman",11,"bold"),bg='white')
        Attendance_status_label.grid(row=3,column=0,padx=8,sticky=W)
        
        Attendance_status_combo=ttk.Combobox(left_inside_frame,font=("times new roman",11,"bold"),textvariable=self.var_atten_attendance,width=21,state="read only")
        Attendance_status_combo['values']=("status","Present","Absent")
        Attendance_status_combo.current(0);
        Attendance_status_combo.grid(row=3,column=1,padx=2,pady=8,sticky=W)


        # bbuttons Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=1,y=240,width=620,height=40)
        # save button
        save_btn=Button(btn_frame,text="Import csv",command=self.ImportCSV,font=("times new roman",12,"bold"),bg='blue',fg='white',width=16)
        save_btn.grid(row=0,column=0)
        # update button
        update_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,font=("times new roman",12,"bold"),bg='blue',fg='white',width=16)
        update_btn.grid(row=0,column=1)
        # delete button
        Delete_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg='blue',fg='white',width=16)
        Delete_btn.grid(row=0,column=2)
        # reset button
        Reset_btn=Button(btn_frame,text="Reset",font=("times new roman",12,"bold"),command=self.reset_fields,bg='blue',fg='white',width=16)
        Reset_btn.grid(row=0,column=3)

        # right frame

        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance",font=("times new roman",12,"bold"))
        right_frame.place(x=638,y=3,width=618,height=430)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=615,height=400)


        # scroll bar---
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")


        self.AttendanceReportTable["show"]="headings"
        


        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column('date',width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        
   


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



        # fetch data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=1)
    


    # def ImportCSV(self):
    #     global mydata
    #     fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)

    #     with open(fln,'r') as myfile:
    #         csvread=csv.reader(myfile,delimiter=",")
    #         for i  in csvread:
    #             mydata.append(i)

    #         self.fetchData(mydata)

    def  ImportCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)

        if fln:
            with open(fln, 'r') as myfile:
                csv_reader = csv.reader(myfile)
                # Skip header row if exists
                next(csv_reader, None)  
                mydata = list(csv_reader)

            # Clear existing data in the table
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())

            # Populate the table with the CSV data
            for row in mydata:
                self.AttendanceReportTable.insert("", "end", values=row)

    # export CSV

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln,mode='w',newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"  successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # cursor

    def get_cursor(self,event=''):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0]);
        self.var_atten_roll.set(rows[1]);
        self.var_atten_name.set(rows[2]);
        self.var_atten_dep.set(rows[3]);
        self.var_atten_time.set(rows[4]);
        self.var_atten_date.set(rows[5]);
        self.var_atten_attendance.set(rows[6]);


    def update_data(self):
            # Get the updated values from entry fields
            atten_id = self.var_atten_id.get()
            roll = self.var_atten_roll.get()
            name = self.var_atten_name.get()
            dep = self.var_atten_dep.get()
            time = self.var_atten_time.get()
            date = self.var_atten_date.get()
            attendance = self.var_atten_attendance.get()

            # Update the row in the table
            selected_item = self.AttendanceReportTable.selection()[0]  # Get the selected item
            self.AttendanceReportTable.item(selected_item, values=(atten_id, roll, name, dep, time, date, attendance))

            # You can also update the data in the 'mydata' list if needed
            # Find the index of the selected item in 'mydata'
            for index, item in enumerate(mydata):
                if item[0] == atten_id:  # Assuming the first column is the Attendance ID
                    # Update the corresponding values in 'mydata'
                    mydata[index] = [atten_id, roll, name, dep, time, date, attendance]
                    break
    

    # reset

    def reset_fields(self):
        # Clear the entry fields
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("status")

        # Deselect any selected item in the treeview
        self.AttendanceReportTable.selection_remove(self.AttendanceReportTable.selection())




    



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()