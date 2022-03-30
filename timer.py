from tkinter import *
import time
import math
FONT_SIZE= ["Arial", 35, "bold"]
COLOR =	"#E0EEEE"
RED="#FF0000"
WORK_TIME=25
SHORT_BREAK=2
LONG_BREAK=10
reps=0
timer=None


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    lable_timer.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0

def start_timer():
    global reps
    reps+=1
    work_time=WORK_TIME*60
    short_break=SHORT_BREAK*60
    long_break=LONG_BREAK*60

    if reps % 8 == 0:
        count_down(long_break)
        lable_timer.config(text="Long Break",fg=RED)

    elif reps % 2 ==0:
        count_down(short_break)
        lable_timer.config(text="short break", fg=RED)

    else:
        count_down(work_time)
        lable_timer.config(text="work", fg=RED)


def count_down(count):
    global timer
    count_min= math.floor(count/60)
    if count_min<10:
        count_min= f"0{count_min}"
    count_sec= count%60
    if count_sec<10:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text, text=(f"{count_min}:{count_sec}"))
    if count >0:
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()






window= Tk()
window.config(padx=50, pady=100, bg=COLOR)
window.title("POMODORO")
canvas= Canvas(width=225, height=224, bg=COLOR, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(103, 105, image=tomato_img)
timer_text=canvas.create_text(103,105,text="00:00", fill="white", font=FONT_SIZE)
canvas.grid(column=1, row=1)
start_button=Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
stop_button= Button(text="stop", highlightthickness=0, command=reset)
stop_button.grid(column=2,row=2)
lable_timer=Label(text="TIMER", bg=COLOR, fg="green", font=(FONT_SIZE, 40," bold"))
lable_timer.grid(column=1, row=0)
check_marks= Label(text="✓")
check_marks.grid(column=1,row=3)











window.mainloop()
