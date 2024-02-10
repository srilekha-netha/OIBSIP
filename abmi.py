from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

ws = Tk()
ws.title("BMI Calculator")
ws.geometry("470x580+300+200")
ws.resizable(False, False)
ws.configure(bg="#f0f1f5")

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    labels = view_report()
    bmi_index(bmi, labels)
    
def view_report():
    label1 = Label(ws, font="arial 60 bold", bg="lightblue", fg="#fff")
    label1.place(x=125, y=305)

    label2 = Label(ws, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
    label2.place(x=280, y=430)

    label3 = Label(ws, font="arial 10 ", bg="lightblue")
    label3.place(x=200, y=500)

    return label1, label2, label3


def bmi_index(bmi, labels):
    label1, label2, label3 = labels
    
    if bmi < 18.5:
        label2.config(text="UnderWeight!")
        label3.config(text="You have lower weight than normal body")
    elif (bmi > 18.5) and (bmi < 24.9):
        label2.config(text="Normal!")
        label3.config(text="It indicates that you are healthy!")
    elif (bmi > 24.9) and (bmi < 29.9):
        label2.config(text="OverWeight!")
        label3.config(text="It indicates that a person is \n slightly overweight! \n A doctor may advice to lose some \n weight for health reasons!")
    elif (bmi > 29.9):
        label2.config(text="Obes!")
        label3.config(text="Health may be at risk, if they do not")
    else:
        label2.config('bmi-pythonguides', 'something went wrong!')


#icon
image_icon = PhotoImage(file= "Images/icon.png")
ws.iconphoto(False,image_icon)

#top
top=PhotoImage(file= "Images/top.png")
top_image=Label(ws,image=top,background="#f0f1f5")
top_image.place(x=-10,y=-10)

#bottom box
Label(ws,width=72,height=18,bg="light blue").pack(side=BOTTOM)



var = IntVar()

frame = Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)


age_lb = Label(
    frame,
    text="Enter Age (2 - 120)"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame, 
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

# Create the frame for buttons
frame3 = Frame(ws)

# View Report button
view_report_btn = Button(
    ws,
    text="View Report",
    width=15,
    height=2,
    font="arial 10 bold",
    bg="#1f6e68",
    fg="white",
    command=calculate_bmi
)
view_report_btn.place(x=280, y=340)

# Calculate button
cal_btn = tk.Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack()
# Grid for frame3
frame3.pack(pady=10)


ws.mainloop()
