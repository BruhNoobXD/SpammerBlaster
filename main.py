import pyautogui,time
import os
from tkinter import * 
def run():
 i=0
 mess=mess_storage.get()
 ness=ness_storage.get()
 timewait=wait_storage.get()
 while i!=timewait:
  time.sleep(1)
  i+=1
 for i in range(1,ness+1):
  pyautogui.write(mess)
  pyautogui.press("enter")
screen = Tk()
screen.title("SpammerBlaster0.1")
screen.geometry("340x200")
screen.configure(bg='black')
screen.resizable(False, False)
Mess_Text=Label(text="What do you want to spam?", fg="lime", bg="black")
Mess_Text.pack()
Mess_Text.place(x=10,y=30)
wait_Text=Label(text="How much time do you need?", fg="lime", bg="black")
wait_Text.pack()
wait_Text.place(x=10,y=90)
Ness_Text=Label(text="How many times do you want to spam?", fg="lime", bg="black")
Ness_Text.pack()
Ness_Text.place(x=10,y=60)
StartButton=Button(text="Start!", fg="black", bg="green", command=run)
StartButton.place(x = 140, y = 150)
mess_storage=StringVar()
ness_storage=IntVar()
wait_storage=IntVar()
input_mess=Entry(textvariable=mess_storage,width=10)
input_mess.place(x = 235,y = 30)
input_ness=Entry(textvariable=ness_storage,width=10)
input_ness.place(x = 235, y = 60)
input_wait=Entry(textvariable=wait_storage,width=10)
input_wait.place(x = 235, y = 90)
screen.mainloop()