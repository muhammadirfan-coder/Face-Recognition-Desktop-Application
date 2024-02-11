from tkinter import *
from PIL import Image, ImageTk
import tkinter
# from tkinter.font import Font
import os
from time import strftime
from datetime import datetime
from student import Student
from traindata import Traindata
from face_recognition import Face_Recognition
from StudentAttendance import Student_Attendance


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

       # first image

        # img = Image.open(r"./download.jpeg")
        # img = img.resize((455, 150), Image.LANCZOS)
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl.place(x=0, y=0, width=455.33, height=150)

        # 2nd Image

        # img1 = Image.open(r"./download.jpeg")
        # img1 = img1.resize((455, 150), Image.LANCZOS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl.place(x=455.33, y=0, width=455.33, height=150)

   # 3rd image

        # img2 = Image.open(r"./download.jpeg")
        # img2 = img2.resize((455, 150), Image.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # f_lbl = Label(self.root, image=self.photoimg2)
        # f_lbl.place(x=910.66, y=0, width=455.33, height=150)

      # bg image

        img3 = Image.open(r"./download.jpeg")
        img3 = img3.resize((1366, 768), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1366, height=768)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM ", font=(
            "times new roman", 37, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1366, height=47)

       # time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman',
                    14, 'bold'), foreground='black')
        lbl.place(x=0, y=0, width=110, height=47)
        time()

        # student  button

        # img4 = Image.open(r"./download.jpeg")
        # img4 = img4.resize((150, 150), Image.LANCZOS)
        # self.photoimg4 = ImageTk.PhotoImage(img4)

        # b1 = Button(bg_img, image=self.photoimg4,
        #             command=self.student_details, cursor="hand2")
        # b1.place(x=300, y=100, width=150, height=150)

        # b1_1 = Button(bg_img, text="Student Details", command=self.student_details,
        #               cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        # b1_1.place(x=300, y=230, width=150, height=30)

        # Detect face  button

        img5 = Image.open(r"./download.jpeg")
        img5 = img5.resize((250, 250), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_data)
        b1.place(x=550, y=250, width=250, height=250)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=550, y=480, width=250, height=50)

        # Attendace face  button

        # img6 = Image.open(r"./download.jpeg")
        # img6 = img6.resize((150, 150), Image.LANCZOS)
        # self.photoimg6 = ImageTk.PhotoImage(img6)

        # b1 = Button(bg_img, image=self.photoimg6,
        #             cursor="hand2", command=self.attendance_data)
        # b1.place(x=840, y=100, width=150, height=150)

        # b1_1 = Button(bg_img, text="Attendace", cursor="hand2", command=self.attendance_data, font=(
        #     "times new roman", 15, "bold"), bg="darkblue", fg="white")
        # b1_1.place(x=840, y=230, width=150, height=30)

        # Train face  button

        img8 = Image.open(r"./download.jpeg")
        img8 = img8.resize((250, 250), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2", command=self.train_data)
        b1.place(x=200, y=250, width=250, height=250)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=480, width=250, height=50)

        # Photos  button

        # img9 = Image.open(r"./download.jpeg")
        # img9 = img9.resize((150, 150), Image.LANCZOS)
        # self.photoimg9 = ImageTk.PhotoImage(img9)

        # b1 = Button(bg_img, image=self.photoimg9,
        #             cursor="hand2", command=self.open_img)
        # b1.place(x=570, y=350, width=150, height=150)

        # b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=(
        #     "times new roman", 15, "bold"), bg="darkblue", fg="white")
        # b1_1.place(x=570, y=480, width=150, height=30)

        # Exit  button

        img11 = Image.open(r"./download.jpeg")
        img11 = img11.resize((250, 250), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,
                    cursor="hand2", command=self.exit)
        b1.place(x=900, y=250, width=250, height=250)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.exit, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=900, y=480, width=250, height=50)

    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

        # function button

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Traindata(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    # root = root.attributes('-fullscreen', True)
    obj = Face_Recognition_System(root)
    root.mainloop()
