



from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root;
        self.root.geometry('1200x600')
        self.root.title("Student Details")
    
        # ---variables-----
        self.var_dep=StringVar();
        self.var_course=StringVar();
        self.var_year=StringVar();
        self.var_semester=StringVar();
        self.var_std_id=StringVar();
        # self.var_std_rollno=StringVar();
        self.var_std_name=StringVar();
        self.var_roll=StringVar();
        self.var_gender=StringVar();
        self.var_dob=StringVar();
        self.var_email=StringVar();
        self.var_phone=StringVar();
        self.var_div=StringVar();
        self.var_address=StringVar();
        self.var_teacher=StringVar();




        # img1
        img=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\images (7).jpg")
        img=img.resize((450,80),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=80)

        # img2
        img1=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\download (1).png")
        img1=img1.resize((450,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=80)
        # img3

        img2=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\images (8).jpg")
        img2=img2.resize((450,80),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=80)

          # bgImage

        img3=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\pngtree-blue-face-recognition-technology-design-poster-background-image_195905.jpg")
        img3=img3.resize((1300,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=60,width=1300,height=600)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM " ,font=('time new roman',20,'bold'),bg='white',fg='blue');
        title_lbl.place(x=0,y=0,width=1300,height=25);

        # main frame
        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=5,y=45,width=1268,height=540)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=6,y=6,width=615,height=530)

        # add image left

        img_left=Image.open(r"IMAGE/pexels-pavel-danilyuk-8423092.jpg")
        img_left=img_left.resize((605,80),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=605,height=70)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=6,y=71,width=620,height=95)

        #department

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg='white')
        dep_label.grid(row=0,column=0,padx=8,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=21,state="read only")
        dep_combo['values']=("Select department","CSE","IT","Electrical","ECE")
        dep_combo.current(0);
        dep_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        #course

        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg='white')
        course_label.grid(row=0,column=2,padx=8,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=21,state="read only")
        course_combo['values']=("Select Course","B.tech","BE")
        course_combo.current(0);
        course_combo.grid(row=0,column=3,padx=2,pady=8,sticky=W)

        #year
         
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg='white')
        year_label.grid(row=1,column=0,padx=8,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=21,state="read only")
        year_combo['values']=("Select Year","2021","2022","2023","2024")
        year_combo.current(0);
        year_combo.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg='white')
        semester_label.grid(row=1,column=2,padx=8,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=21,state="read only")
        semester_combo['values']=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        semester_combo.current(0);
        semester_combo.grid(row=1,column=3,padx=2,pady=8,sticky=W)

         #class Student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=172,width=600,height=330)
        # studentId
        StudentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",10,"bold"),bg='white')
        StudentId_label.grid(row=0,column=0,padx=8,pady=8,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",10,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,pady=8,sticky=W);

        #StudentName
        
        StudentName_label=Label(class_Student_frame,text="Student_NAME:",font=("times new roman",10,"bold"),bg='white')
        StudentName_label.grid(row=0,column=2,padx=5,pady=8,sticky=W)

        StudentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",10,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=5,pady=8,sticky=W);

        #class Division
        
        class_div_label=Label(class_Student_frame,text="class Division:",font=("times new roman",10,"bold"),bg='white')
        class_div_label.grid(row=1,column=0,padx=5,pady=8,sticky=W)

        # class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_div,font=("times new roman",10,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=5,pady=8,sticky=W);

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),width=18,state="read only")
        div_combo['values']=("Select division","A","B","C")
        div_combo.current(0);
        div_combo.grid(row=1,column=1,padx=5,pady=8,sticky=W)

        # rollNO
        roll_no_label=Label(class_Student_frame,text="Roll :",font=("times new roman",10,"bold"),bg='white')
        roll_no_label.grid(row=1,column=2,padx=5,pady=8,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=5,pady=8,sticky=W);

        # gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",10,"bold"),bg='white')
        gender_label.grid(row=2,column=0,padx=5,pady=8,sticky=W)

        # gender_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_gender,font=("times new roman",10,"bold"))
        # gender_entry.grid(row=2,column=1,padx=5,pady=8,sticky=W);

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=18,state="read only")
        gender_combo['values']=("Select gender","Male","female","other")
        gender_combo.current(0);
        gender_combo.grid(row=2,column=1,padx=5,pady=8,sticky=W)

        #Email
        emial_label=Label(class_Student_frame,text="Email:",font=("times new roman",10,"bold"),bg='white')
        emial_label.grid(row=2,column=2,padx=5,pady=8,sticky=W)

        emial_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",10,"bold"))
        emial_entry.grid(row=2,column=3,padx=5,pady=8,sticky=W);

        # address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",10,"bold"),bg='white')
        address_label.grid(row=3,column=0,padx=5,pady=8,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",10,"bold"))
        address_entry.grid(row=3,column=1,padx=5,pady=8,sticky=W);

        # teacherName
        teacher_label=Label(class_Student_frame,text="teacher_Name:",font=("times new roman",10,"bold"),bg='white')
        teacher_label.grid(row=3,column=2,padx=5,pady=8,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",10,"bold"))
        teacher_entry.grid(row=3,column=3,padx=5,pady=8,sticky=W);

        # phoneNUmber
        Phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",10,"bold"),bg='white')
        Phone_label.grid(row=4,column=0,padx=5,pady=8,sticky=W)

        Phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",10,"bold"))
        Phone_entry.grid(row=4,column=1,padx=5,pady=8,sticky=W);
        
        # DOB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",10,"bold"),bg='white')
        dob_label.grid(row=4,column=2,padx=5,pady=8,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",10,"bold"))
        dob_entry.grid(row=4,column=3,padx=5,pady=8,sticky=W);
        
        # radio Buttons

        # create variable 
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take photo Sample",value="yes")
        radiobtn1.grid(row=5,column=0)

       

        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo Sample",value="no")
        radiobtn2.grid(row=5,column=1)

        # bbuttons Frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=1,y=225,width=620,height=40)
        # save button
        save_btn=Button(btn_frame,text="save", command=self.add_data,font=("times new roman",12,"bold"),bg='blue',fg='white',width=16)
        save_btn.grid(row=0,column=0)
        # update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg='blue',fg='white',width=16)
        update_btn.grid(row=0,column=1)
        # delete button
        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg='blue',fg='white',width=16)
        Delete_btn.grid(row=0,column=2)
        # reset button
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg='blue',fg='white',width=16)
        Reset_btn.grid(row=0,column=3)

        # create new frame
        btn_frame_1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame_1.place(x=1,y=260,width=620,height=40)

        #add button for take photo
        Take_photo_sample_btn=Button(btn_frame_1,text="Take_photo_sample",command=self.generate_dataset,font=("times new roman",12,"bold"),bg='blue',fg='white',width=35)
        Take_photo_sample_btn.grid(row=1,column=0)
        # update button
        Update_photo_btn=Button(btn_frame_1,text="Update Photo Sample",command=self.update_photo_sample,font=("times new roman",12,"bold"),bg='blue',fg='white',width=35)
        Update_photo_btn.grid(row=1,column=1)

        


        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=6,width=620,height=530)

        # add image right

        img_right=Image.open(r"C:\Users\PARTAEK YADAV\Desktop\Attendance based Project\IMAGE\download (6).jpg")
        img_right=img_right.resize((605,80),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=605,height=70)


        # --Search System---
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Searchchb System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=70,width=600,height=70)

        Search_label=Label(Search_frame,text="Search BY:",font=("times new roman",12,"bold"),bg='red',fg='white')
        Search_label.grid(row=0,column=0,padx=8,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=13,state="read only")
        search_combo['values']=("Select ","Roll no","Phone_no")
        search_combo.current(0);
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        #add entry button
        search_entey=ttk.Entry(Search_frame,font=("times new roman",12,"bold"))
        search_entey.grid(row=0,column=2,padx=5,pady=8,sticky=W)
        # search button
        search_btn=Button(Search_frame,text="Search",font=("times new roman",12,"bold"),command=self.search_student,bg='blue',fg='white',width=9)
        search_btn.grid(row=0,column=3)
        #show all button
        showAll_btn=Button(Search_frame,text="Show All",font=("times new roman",12,"bold"),command=self.show_all_data,bg='blue',fg='white',width=9)
        showAll_btn.grid(row=0,column=4,padx=2)

        # -------table frame--------------


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=150,width=600,height=350)
        # scroll bar
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Student_Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.pack(fill=BOTH,expand=1)
       

        # set column width
        self.student_table.column("dep",width=90)
        self.student_table.column("course",width=90)
        self.student_table.column("year",width=90)
        self.student_table.column("sem",width=90)
        self.student_table.column("id",width=90)
        self.student_table.column("name",width=90)
        self.student_table.column("div",width=90)
        self.student_table.column("roll",width=90)
        self.student_table.column("dob",width=90)
        self.student_table.column("gender",width=90)
        self.student_table.column("email",width=90)
        self.student_table.column("phone",width=90)
        self.student_table.column("address",width=90)
        self.student_table.column("teacher",width=90)
        self.student_table.column("photo",width=90)
        
        # self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()

      # ------function declaration-----------

    def add_data(self):
        if(self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","all field are required",parent=self.root)
        else:
            # messagebox.showinfo("sucessful ")
            # connection DB
            try:
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="partaek2171014@",
                database="face_recognizer"
                )
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                    self.var_dep.get(),
                                                    self.var_course.get(),
                                                    self.var_year.get(),
                                                    self.var_semester.get(),
                                                    self.var_std_id.get(),
                                                    self.var_std_name.get(),
                                                    self.var_div.get(),
                                                    self.var_roll.get(),
                                                    
                                                    self.var_gender.get(),
                                                    self.var_dob.get(),
                                                    self.var_email.get(),
                                                    self.var_phone.get(),
                                                    self.var_address.get(),
                                                    self.var_teacher.get(),
                                                    self.var_radio1.get()
                                                    
                ))

                conn.commit()
                self.fetch_data()
                conn.close();
                messagebox.showinfo("Success ","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root);


    # =========fetch data==============  
    def fetch_data(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="partaek2171014@",
                database="face_recognizer"
                )
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if(len(data)!=0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ----get cursor---
    def get_cursor(self,event=""):
        cursor_foucus=self.student_table.focus()
        content=self.student_table.item(cursor_foucus)
        data=content["values"]

        self.var_dep.set(data[0]);
        self.var_course.set(data[1]);
        self.var_year.set(data[2]);
        self.var_semester.set(data[3]);
        self.var_std_id.set(data[4]);#4
        self.var_std_name.set(data[5]);#5
        self.var_div.set(data[6]);
        self.var_roll.set(data[7]);
        self.var_gender.set(data[8]);
        self.var_dob.set(data[9]);
        self.var_email.set(data[10]);
        self.var_phone.set(data[11]);
        self.var_address.set(data[12]);
        self.var_teacher.set(data[13]);
        self.var_radio1.set(data[14]);
    

    # -----------update Function----------
    def update_data(self):
        if (self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student's details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="partaek2171014@",
                        database="face_recognizer"
                    )

                    
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET dpet=%s, course=%s, year=%s, Semester=%s, Division=%s,Name=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teachar=%s, PhotoSample=%s WHERE Student_id=%s",
                                    (self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_div.get(),
                                    self.var_std_name.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),
                                    self.var_std_id.get())
                                    )
                    conn.commit()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    self.fetch_data()
                    
                    conn.close()
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    # delete function-----
    
    def delete_data(self):
        if(self.var_std_id.get()==""):
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page ","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="partaek2171014@",
                        database="face_recognizer"
                    )

                    
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val);
                else:
                    if not delete:
                        return     
                conn.commit()
                messagebox.showinfo("Delete ", "Student details successfully Deleted", parent=self.root)
                self.fetch_data()
                    
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # -----Reset Function---------
    def reset_data(self):
        self.var_dep.set("Select Department");
        self.var_course.set("Select Course");
        self.var_year.set("Select Year");
        self.var_semester.set("Select Semester");
        self.var_std_id.set("");#4
        self.var_std_name.set("");#5
        self.var_div.set("Select Division");
        self.var_roll.set("");
        self.var_gender.set("Select Gender");
        self.var_dob.set("");
        self.var_email.set("");
        self.var_phone.set("");
        self.var_address.set("");
        self.var_teacher.set("");
        self.var_radio1.set("");


    # ------------Generate Data set or take photo Samples------------
    def generate_dataset(self):
        if(self.var_std_id.get()==""):
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="partaek2171014@",
                        database="face_recognizer"
                    )

                    
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET dpet=%s, course=%s, year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teachar=%s, PhotoSample=%s WHERE Student_id=%s",
                                    (self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),

                                    self.var_std_id.get()==id+1)
                                    )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                

                # -------LOad predefined data on face frontals from opencv-------
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    # minimum neighbor=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                # open camera capture
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break;
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!!!")


            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

        # update data        # 

    def update_photo_sample(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="partaek2171014@",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (self.var_std_id.get(),))
            student_data = my_cursor.fetchone()

            if student_data is None:
                messagebox.showerror("Error", "Student not found", parent=self.root)
                conn.close()
                return

            # Load predefined data on face frontals from OpenCV
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y+h, x:x+w]
                    return face_cropped

            # Open camera capture
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = f"data/user.{student_data[4]}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Photo sample updated successfully")
            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

    
    def show_all_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="partaek2171014@",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            if len(data) == 0:
                messagebox.showinfo("Result", "No records found", parent=self.root)
            else:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)


    def search_student(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="partaek2171014@",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (self.var_std_id.get(),))
            student_data = my_cursor.fetchone()

            if student_data is None:
                messagebox.showerror("Error", "Student not found", parent=self.root)
            else:
                self.clear()
                self.var_roll_no.set(student_data[1])
                self.var_name.set(student_data[2])
                self.var_email.set(student_data[3])
                self.var_dep.set(student_data[5])
                self.var_gender.set(student_data[6])
                self.var_contact.set(student_data[7])
                self.var_dob.set(student_data[8])
                self.txt_address.delete("1.0", END)
                self.txt_address.insert(END, student_data[9])

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

if __name__=="__main__":
      root=Tk()
      obj=Student(root)
      root.mainloop()