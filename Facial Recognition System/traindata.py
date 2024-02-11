# #from logging import exception
# #from os import close, path
# from tkinter import*
# from tkinter import ttk
# #from tkinter.font import Font
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# #from mysql.connector import cursor
# import  cv2
# import os
# import numpy as np


# class Traindata:
#     def __init__ (self,root):
#         self.root=root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face Recognition System")


#         # bg image

#         img=Image.open(r"C:\Users\Xaini Arham\Desktop\face recognition system\image\pic1.jpg")
#         img=img.resize((1366,768),Image.ANTIALIAS)
#         self.photoimg=ImageTk.PhotoImage(img)

#         bg_img1=Label(self.root,image=self.photoimg)
#         bg_img1.place(x=0,y=0,width=1366,height=768)


#         title_lbl=Label(bg_img1,text="TRAIN STUDENT DATASET ",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
#         title_lbl.place(x=0,y=0,width=1366,height=40)


#        # Button for train dataset

#         b1_1=Button(bg_img1,text="Train Dataset",command=self.train_classifier,cursor="hand2",font=("times new roman",17,"bold"),bg="darkgreen",fg="white")
#         b1_1.place(x=0,y=600,width=1366,height=40)


#     def train_classifier(self):
#         data_dir=("data")
#         path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


#         faces=[]
#         ids=[]

#         for image in path:
#             img=Image.open(image).convert('L') #gray sscale image
#             imgNP=np.array(img,'uint8')   #uint data type
#             id=int(os.path.split(image)[1].split('.')[1])

#             faces.append(imgNP)
#             ids.append(id)
#             cv2.imshow("Training",imgNP)
#             cv2.waitKey(1)==13
#         ids=np.array(ids)
#          #train classifierand save
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.train(faces,ids)
#         clf.write("classifier.xml")
#         cv2.destroyAllWindows()
#         messagebox.showinfo("Result","Training datasets completed",parent=self.root)
#         self.root.destroy()


# if  __name__ == "__main__":
#        root=Tk()
#        obj=Traindata(root)
#        root.mainloop()


# changed by shahzad

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import csv
import pandas as pd


class Traindata:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # bg image
        img = Image.open("download.jpeg")
        img = img.resize((1366, 768), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img1 = Label(self.root, image=self.photoimg)
        bg_img1.place(x=0, y=0, width=1366, height=768)

        title_lbl = Label(bg_img1, text="TRAIN STUDENT DATASET ", font=("times new roman", 35, "bold"), bg="white",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1366, height=40)

        # Entry fields for user information
        self.name_label = Label(bg_img1, text="Enter Your Name: ", font=(
            'times new roman', 22), fg="darkgreen")
        self.name_label.place(x=200, y=100)

        self.user_name_entry = Entry(bg_img1, font=(
            "times new roman", 20), bd=5, relief=GROOVE)
        self.user_name_entry.place(x=500, y=100)

        self.dep_label = Label(bg_img1, text="Department: ", font=(
            'times new roman', 22), fg="darkgreen")
        self.dep_label.place(x=200, y=150)

        self.department_entry = Entry(bg_img1, font=(
            "times new roman", 20), bd=5, relief=GROOVE)
        self.department_entry.place(x=500, y=150)

        self.rollno_label = Label(bg_img1, text="Roll No: ", font=(
            'times new roman', 22), fg="darkgreen")
        self.rollno_label.place(x=200, y=200)

        self.rollno_entry = Entry(bg_img1, font=(
            "times new roman", 20), bd=5, relief=GROOVE)
        self.rollno_entry.place(x=500, y=200)

        # Button for train dataset
        b1_1 = Button(bg_img1, text="Start Capturing", command=self.start_capturing, cursor="hand2",
                      font=("times new roman", 17, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=500, y=250, width=200, height=40)

    def start_capturing(self):
        user_name = self.user_name_entry.get()
        department = self.department_entry.get()
        rollno = self.rollno_entry.get()

        if not user_name or not department or not rollno:
            messagebox.showwarning(
                "Warning", "Please enter valid information.")
            return

        data_dir = f"data/{user_name}"

        # Check if the user's folder exists, if not, create it
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Create a cascade classifier for face detection
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Start capturing from the default webcam (index 0)
        cap = cv2.VideoCapture(0)

        # Initialize variables
        count = 0
        max_count = 200  # Set the maximum number of images to capture

        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Save the captured face to the user's folder
                cv2.imwrite(f"{data_dir}/user.{count}.jpg", roi_gray)
                count += 1

            cv2.imshow("Capturing Images", frame)

            # Break the loop if the user presses 'q' or if the required number of images is captured
            if cv2.waitKey(1) & 0xFF == ord('q') or count >= max_count:
                break

        cap.release()
        cv2.destroyAllWindows()

        if count >= max_count:
            # Save user information to Excel sheet
            self.save_user_info_to_excel(user_name, department, rollno)

            messagebox.showinfo(
                "Result", "Capturing completed", parent=self.root)
            self.create_train_button()

    def save_user_info_to_excel(self, user_name, department, rollno):
        info_df = pd.DataFrame({'Name': [user_name], 'Department': [
                               department], 'RollNo': [rollno]})

        # Check if the file exists
        excel_path = 'user_info.xlsx'
        if os.path.exists(excel_path):
            existing_info_df = pd.read_excel(excel_path)
            # Check if the user already exists in the sheet
            if user_name in existing_info_df['Name'].values:
                messagebox.showinfo(
                    "Info", "User already exists in the sheet.")
                return
            else:
                # Append new information to the existing sheet
                info_df = pd.concat(
                    [existing_info_df, info_df], ignore_index=True)

        # Save the information to the Excel sheet
        info_df.to_excel(excel_path, index=False)

    def create_train_button(self, main_dir='./data'):
        b1_2 = Button(self.root, text="Train Model", command=lambda: self.train_classifier(main_dir), cursor="hand2",
                      font=("times new roman", 17, "bold"), bg="darkgreen", fg="white")
        b1_2.place(x=500, y=300, width=200, height=40)

    def train_classifier(self, main_dir='./data/'):
        faces = []
        ids = []
        names = []  # List to store names

        name_id_mapping = {}  # Mapping to ensure unique IDs for each person

        for root, dirs, files in os.walk(main_dir):
            for file in files:

                if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                    image_path = os.path.join(root, file)
                    # print(image_path)
                    img = Image.open(image_path).convert(
                        'L')  # gray scale image
                    img_np = np.array(img, 'uint8')  # uint data type
                    # Assume person's name is the folder name
                    name = os.path.basename(root)

                    if name not in name_id_mapping:
                        # Assign a new ID for each unique name
                        id = len(name_id_mapping)
                        name_id_mapping[name] = id
                    else:
                        id = name_id_mapping[name]

                    faces.append(img_np)
                    ids.append(id)
                    names.append(name)

        if not faces or not ids:
            messagebox.showerror(
                "Error", "No valid images found for training!", parent=self.root)
            return

        ids = np.array(ids)

        # Save names and IDs to a CSV file
        with open(os.path.join(main_dir, 'names_ids.csv'), 'w', newline='') as csvfile:
            fieldnames = ['ID', 'Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for i in range(len(ids)):
                writer.writerow({'ID': ids[i], 'Name': names[i]})

        # train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training datasets completed", parent=self.root)
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Traindata(root)
    root.mainloop()
