import tkinter as tk
import time

window=tk.Tk()
window.title("Pomodoro App")
window.geometry("600x400")
window.resizable(False,False)
#colors
green="#c4d6b0"
move="#58355f"

time_label=tk.Label(window,text="25:00",font=("arial",90),fg=move,bg=green)
time_label.pack(pady=100,padx=20)
window.configure(bg=green)
#-------colors-------


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
        take_break()
    
def take_break():
    window.bell()
    countdown(5*60)
    if time_label.cget("text")=="00:00":
        start()
    

start_btn=tk.Button(window,text="START",font=("arial",15),bg=move, fg=green,command=lambda:start())
start_btn.pack(pady=10)
start_btn.place(relx=0.3, rely=0.6)

break_btn=tk.Button(window,text="BREAK",font=("arial",15),bg=move, fg=green,command=lambda:take_break())
break_btn.pack(pady=10,side="left")
break_btn.place(relx=0.57, rely=0.6)
window.mainloop()