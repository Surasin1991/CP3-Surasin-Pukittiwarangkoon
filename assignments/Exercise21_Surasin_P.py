from tkinter import *
import math

def leftClickButton(event):
    result = '%.2f'%(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if result <= "18.5":
        caption = "ผอมเกินไป"
    elif result <= "22.9":
        caption = "น้ำหนักปกติ เหมาะสม"
    elif result <= "24.9":
        caption = "น้ำหนักเกิน"
    elif result <= "29.9":
        caption = "อ้วน"
    elif result > "29.9":
        caption = "อ้วนมาก"
        
    print(result,caption)
    labelResult.configure(text=caption)

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm.")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()