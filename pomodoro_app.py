import tkinter as tk
import time
from PIL import Image, ImageTk

window=tk.Tk()
window.title("Pomodoro App")
window.geometry("600x400")
window.resizable(False,False)
#colors
burgundy="#8d2645"
green="#c4d6b0"
move="#622F63"
Pink="#fff8f3"
bg_color="#f9f6ee"
#---------background---------
bg = ImageTk.PhotoImage(Image.open("bg_pomo.png").resize((600,400)))
bg_label = tk.Label(window, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


time_label=tk.Label(window,text="25:00",font=("arial",90),fg=move,bg=bg_color)
time_label.pack(pady=100,padx=20)
window.configure(bg = bg_color)

def countdown(seconds): 
    while seconds >= 0:
        min = seconds // 60
        sec = seconds % 60
        time_label.config(text=f"{min:02d}:{sec:02d}")
        window.update()
        time.sleep(1)   
        seconds -= 1

def start():
    window.bell()
    countdown(25*60)
    if time_label.cget("text")=="00:00":
        short_break()
    
def short_break():
    window.bell()
    countdown(5*60)
    if time_label.cget("text")=="00:00":
        start()
    
def long_break():
    window.bell()
    countdown(15*60)
    if time_label.cget("text")=="00:00":
        start()
#---------start button---------
start_btn=tk.Button(window,text="     ▶︎",font=("arial",30),bg=move, fg=Pink,command=lambda:start())
start_btn.pack(pady=5)
start_btn.place(relx=0.36, rely=0.65)

#---------short break---------
break_btn=tk.Button(window,text="short break",font=("arial",15),bg=move, fg=Pink,command=lambda:short_break())
break_btn.pack(pady=10,side="left")
break_btn.place(relx=0.29, rely=0.15)

#---------long break---------
break_btn=tk.Button(window,text="long break",font=("arial",15),bg=move, fg=Pink,command=lambda:long_break())
break_btn.pack(pady=10,side="left")
break_btn.place(relx=0.53, rely=0.15)

window.mainloop()