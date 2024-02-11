import cv2
import tkinter as tk

# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)

# while True:
#    success, img = cap.read()
#    cv2.imshow("Face Attendance", img)
#    cv2.waitKey(1)

root = tk.Tk()
root.geometry("1000x500")
root.title("My App")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(pady=40)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=50)

entry = tk.Entry(root)
entry.pack()
root.mainloop()
