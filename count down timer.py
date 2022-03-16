from tkinter import *
import time
from tkinter import messagebox
win = Tk()
win.geometry('300x300')
win.resizable(False,False)
win.config(bg='black')
sec = StringVar()
Entry(win, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=140,y=120)
sec.set('00')
mins= StringVar()
Entry(win, textvariable = mins, width =2, font = 'Helvetica 14').place(x=110,y=120)
mins.set('00')
hrs= StringVar()
Entry(win, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=80,y=120)
hrs.set('00')
def countdowntimer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      win.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      if times==0:
         messagebox.showinfo("Timer count down ","Time over")
      times -= 1
Label(win, font =('Helvetica bold',22), text = 'Set the Timer',bg='blue').place(x=50,y=70)
Button(win, text='GO',  bg = 'red',font =('Helveticabold',10), command = countdowntimer)\
    .place(x=167, y=165)
win.mainloop()