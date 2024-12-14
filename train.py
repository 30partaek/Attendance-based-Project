
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x600')
        self.root.title("Train Dataset")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=('times new roman', 35, 'bold'), bg='lightgreen', fg='ghostWhite')
        title_lbl.place(x=2, y=1, width=1272, height=40)

        # Top image
        img_top = Image.open(r"IMAGE/istockphoto-913641964-1024x1024.jpg")
        img_top = img_top.resize((1272, 260), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=2, y=42, width=1272, height=260)

        # Add button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=('times new roman', 35, 'bold'), bg='purple', fg='black')
        b1_1.place(x=2, y=308, width=1272, height=63)

        # Bottom image
        img_bottom = Image.open(r"IMAGE/istockphoto-925574662-1024x1024.jpg")
        img_bottom = img_bottom.resize((1272, 260), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=2, y=380, width=1272, height=260)

    def train_classifier(self):
        data_dir =("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Grey scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        print("cv353")
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
