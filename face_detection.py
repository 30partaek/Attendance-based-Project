from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
from time import strftime
from datetime import datetime


class Face_Detection_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x625')
        self.root.title("Face_Detection_System")

        title_lbl = Label(self.root, text="Face Detection System", font=('times new roman', 35, 'bold'), bg='lightgreen', fg='ghostWhite')
        title_lbl.place(x=2, y=1, width=1272, height=40)

        # Left image
        img_top = Image.open("IMAGE/face-recognition-personal-identification-collage (1).jpg")
        img_top = img_top.resize((635, 602), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=2, y=43, width=635, height=602)

        # Right image
        img_bottom = Image.open("IMAGE/2464733.jpg")
        img_bottom = img_bottom.resize((635, 602), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=640, y=43, width=635, height=602)

        # Add button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=('times new roman', 20, 'bold'), bg='aqua', fg='purple')
        b1_1.place(x=185, y=530, width=260, height=50)


    # mark attendance
    def mark_attendance(self, i, n, r, d):
        with open("attendance.csv", "r+", newline='\n') as f:
            myDataList = f.readlines()
            id_list = []

            for line in myDataList:
                entry = line.split(",")
                id_list.append(entry[0])  # Assuming ID is at index 0

            if i not in id_list:
                now = datetime.now()
                d1 = now.strftime("%d/%M/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
    


    def face_recog(self):

        def draw_boundary(img, faceCascade, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = faceCascade.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn = None
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="partaek2171014@",
                        database="face_recognizer"
                    )

                    try:
                        my_cursor = conn.cursor()
                        my_cursor.execute("SELECT  dpet,Name, Roll, Student_id FROM face_recognizer.student WHERE Student_id = %s", (id,))
                        
                        if confidence >77:
                            result = my_cursor.fetchone()
                            if result:
                                d,n, r, i = result
                                cv2.putText(img, f"Department: {d}", (x, y + h + 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Roll: {r}", (x, y + h + 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Name: {n}", (x, y + h + 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"id: {i}", (x, y + h + 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                                # print("details")
                                
                                self.mark_attendance(i,n,r,d)
                                my_cursor.close() 
                            else:
                                print("No data found for the provided Student_id:", id)

                        else:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                            cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)  
                    except mysql.connector.Error as err:
                            print("MySQL Error:", err)
                    finally:
                        if conn:
                            conn.close() 
                        
                except mysql.connector.Error as err:
                    print("MySQL Error:", err)
                finally:
                    if conn:
                        conn.close()
            return img

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)
        try:
            while True:
                ret, img = video_cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to capture video.")
                    break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to Face Recognition", img)
                if cv2.waitKey(1)==13:
                    break
        finally:
            video_cap.release()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Detection_System(root)
    root.mainloop()

    
