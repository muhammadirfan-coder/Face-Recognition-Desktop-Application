
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
# from time import strftime
# from datetime import datetime


# class Face_Recognition:
#     def __init__ (self,root):
#         self.root=root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face Recognition System")

#           # bg image

#         imgg=Image.open(r"./download.jpeg")
#         imgg=imgg.resize((1366,768),Image.ANTIALIAS)
#         self.photoimgg=ImageTk.PhotoImage(imgg)

#         bg_img2=Label(self.root,image=self.photoimgg)
#         bg_img2.place(x=0,y=0,width=1366,height=768)


#         title_lbl=Label(bg_img2,text="FACE RECOGNITION ",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
#         title_lbl.place(x=0,y=0,width=1366,height=40)


#          #first image

#         image1=Image.open(r"./download.jpeg")
#         image1=image1.resize((600,500),Image.ANTIALIAS)
#         self.photoimage1=ImageTk.PhotoImage(image1)

#         f_lbl=Label(bg_img2,image=self.photoimage1)
#         f_lbl.place(x=350,y=100,width=600,height=500)


#        # Button for train dataset

#         b1_1=Button(bg_img2,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",17,"bold"),bg="darkgreen",fg="white")
#         b1_1.place(x=355,y=640,width=600,height=40)

#         # attendance........

#     def mark_attendance(self,i,r,n,d):
#         with open("Attendance.csv","r+",newline="\n") as f:
#             myDatalist=f.readlines()
#             name_list=[]
#             for line in myDatalist:
#                 entry=line.split((","))
#                 name_list.append(entry[0])
#             if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
#                 now=datetime.now()
#                 d1=now.strftime("%d/%m/%Y")
#                 dtString=now.strftime("%H:%M:%S")
#                 f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


# # face recognition
#     def  face_recog(self):
#          def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#              gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#              features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)


#              coord=[]

#              for (x,y,w,h) in features:
#                  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#                  id,predict=clf.predict(gray_image[y:y+h,x:x+w])
#                  confidence=int((100*(1-predict/300)))

#                  conn=mysql.connector.connect(host="localhost",username="root",password="agri123",database="face_recognizer")
#                  my_cursor=conn.cursor()

#                  my_cursor.execute("select Name from student where Student_id="+str(id))
#                  n=my_cursor.fetchone()
#                 #n=str(n)
#                  n='+'.join(n)
#                 # separator="my_id=separator.join"(str(x)for x in i)


#                  my_cursor.execute("select Roll from student where Student_id="+str(id))
#                  r=my_cursor.fetchone()
#                  # r=str(r)
#                  r='+'.join(r)
#                  #separator="my_id=separator.join"(str(x)for x in r)


#                  my_cursor.execute("select Dept from student where Student_id="+str(id))
#                  d=my_cursor.fetchone()
#                  # d=str(d)
#                  d='+'.join(d)
#                  #separator="my_id=separator.join"(str(x)for x in d)

#                  my_cursor.execute("select Student_id from student where Student_id="+str(id))
#                  i=my_cursor.fetchone()
#                  # d=str(d)
#                  i='+'.join(i)
#                  #separator="my_id=separator.join"(str(x)for x in d)


#                  if confidence>77:
#                      cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                      cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                      cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                      cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                      self.mark_attendance(i,r,n,d)

#                  else:
#                      cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                      cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                  coord=[x,y,w,h]

#              return coord

#          def  recognize(img,clf,faceCascade):
#               coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
#               return img

#          faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#          clf=cv2.face.LBPHFaceRecognizer_create()
#          clf.read("classifier.xml")

#          video_cap=cv2.VideoCapture(0)


#          while True:
#              ret,img=video_cap.read()
#              img=recognize(img,clf,faceCascade)
#              cv2.imshow("Welcome To face Recognition",img)

#              if cv2.waitKey(1)==13:
#                  break
#          video_cap.release()
#          cv2.destroyAllWindows()
#          self.root.destroy()


# if  __name__ == "__main__":
#        root=Tk()
#        obj=Face_Recognition(root)
#        root.mainloop()

# changed by shehzad

# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import cv2
# import os
# import numpy as np
# from time import strftime
# from datetime import datetime
# import csv

# class Face_Recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face Recognition System")

#         # bg image
#         imgg = Image.open("./download.jpeg")
#         imgg = imgg.resize((1366, 768), Image.ANTIALIAS)
#         self.photoimgg = ImageTk.PhotoImage(imgg)

#         bg_img2 = Label(self.root, image=self.photoimgg)
#         bg_img2.place(x=0, y=0, width=1366, height=768)

#         title_lbl = Label(bg_img2, text="FACE RECOGNITION ", font=("times new roman", 35, "bold"), bg="white",
#                           fg="darkgreen")
#         title_lbl.place(x=0, y=0, width=1366, height=40)

#         # first image
#         image1 = Image.open("./download.jpeg")
#         image1 = image1.resize((600, 500), Image.ANTIALIAS)
#         self.photoimage1 = ImageTk.PhotoImage(image1)

#         f_lbl = Label(bg_img2, image=self.photoimage1)
#         f_lbl.place(x=350, y=100, width=600, height=500)

#         # Button for face recognition
#         b1_1 = Button(bg_img2, text="Face Recognition", cursor="hand2", command=self.face_recog,
#                       font=("times new roman", 17, "bold"), bg="darkgreen", fg="white")
#         b1_1.place(x=355, y=640, width=600, height=40)

#     def mark_attendance(self, i, r, n, d):
#         with open("Attendance.csv", "a", newline="\n") as f:
#             now = datetime.now()
#             d1 = now.strftime("%d/%m/%Y")
#             dtString = now.strftime("%H:%M:%S")
#             f_writer = csv.writer(f)
#             f_writer.writerow([i, r, n, d, dtString, d1, "Present"])

#     # face recognition
#     def face_recog(self):
#         def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

#             coord = []

#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#                 id, predict = clf.predict(gray_image[y:y + h, x:x + w])
#                 confidence = int((100 * (1 - predict / 300)))
#                 print(confidence)
#                 if confidence >= 80:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                     cv2.putText(img, "Person Recognized", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

#                     # cv2.putText(img, f"ID:{id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     # cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     # cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     # cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                     # self.mark_attendance(id, r, n, d)
#                 else:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                     cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

#                 coord = [x, y, w, h]

#             return coord

#         def recognize(img, clf, faceCascade):
#             coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
#             return img

#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")

#         video_cap = cv2.VideoCapture(0)

#         while True:
#             ret, img = video_cap.read()
#             img = recognize(img, clf, faceCascade)
#             cv2.imshow("Welcome To Face Recognition", img)

#             if cv2.waitKey(1) == 13:
#                 break

#         video_cap.release()
#         cv2.destroyAllWindows()
#         self.root.destroy()


# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()


from tkinter import *
from PIL import Image, ImageTk
import cv2
import os
from datetime import datetime
import pandas as pd


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.face_id_name_mapping = dict()

        # bg image
        imgg = Image.open("./download.jpeg")
        imgg = imgg.resize((1366, 768), Image.LANCZOS)
        self.photoimgg = ImageTk.PhotoImage(imgg)

        bg_img2 = Label(self.root, image=self.photoimgg)
        bg_img2.place(x=0, y=0, width=1366, height=768)

        title_lbl = Label(bg_img2, text="FACE RECOGNITION ", font=("times new roman", 35, "bold"), bg="white",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1366, height=40)

        # first image
        image1 = Image.open("./download.jpeg")
        image1 = image1.resize((600, 500), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(image1)

        f_lbl = Label(bg_img2, image=self.photoimage1)
        f_lbl.place(x=350, y=100, width=600, height=500)

        # Button for face recognition
        b1_1 = Button(bg_img2, text="Face Recognition", cursor="hand2", command=self.face_recog,
                      font=("times new roman", 17, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=355, y=640, width=600, height=40)

        # Load training data for mapping face IDs to names
        self.face_id_name_mapping = self.load_face_id_name_mapping()

        # Create or load the attendance DataFrame
        self.attendance_df = pd.DataFrame(
            columns=['ID', 'Roll', 'Name', 'Department', 'Time', 'Date', 'Status'])
        self.present_students = set()  # To keep track of students already marked present

    def load_face_id_name_mapping(self):
        mapping = {}
        # Assuming your training dataset folder is named 'dataset'
        dataset_folder = "data"
        for root, dirs, files in os.walk(dataset_folder):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                    path = os.path.join(root, file)
                    name = os.path.basename(root)
                    img = cv2.imread(path)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # Assuming the person's name is the folder name and is numeric
                    face_id = str(name)
                    if face_id not in mapping:
                        mapping[face_id] = name
        print(mapping)
        return mapping

    def mark_attendance(self, i, r, n, d):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")

        # Check if the student is already marked present
        if i not in self.present_students:
            # print("not marked attendence yet")

            info = [{'ID': i, 'Roll': r, 'Name': n, 'Department': d,
                     'Time': dtString, 'Date': d1, 'Status': 'Present'}]
            info_df = pd.DataFrame(info)
            # print("info", info_df)
            self.attendance_df = pd.concat(
                [self.attendance_df, info_df], ignore_index=True)

            self.present_students.add(i)
            self.attendance_df.to_excel('Attendance.xlsx', index=False)

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                file = pd.read_csv('data/names_ids.csv')
                user_info = pd.read_excel('user_info.xlsx')
                try:

                    name = file[file['ID'] == id]['Name'][:1].values[0]
                    dept = user_info[user_info['Name'] ==
                                     name]['Department'][:1].values[0]
                    Rno = user_info[user_info['Name']
                                    == name]['RollNo'][:1].values[0]
                    self.mark_attendance(id, Rno, name, dept)

                except:
                    print("could not matched")

                print(confidence)
                if confidence >= 80:
                    # Fetch the name from the training dataset
                    # name=self.load_face_id_name_mapping()
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"{str(name)} Recognized", (x, y - 55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,
                                  10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
