from tkinter import *
from tkinter import messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
canvas_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    canvas.after_cancel(canvas_timer)
    #timer_text = 00:00 
    canvas.itemconfig(timer_text, text="00:00")
    #title = "Timer"
    timer_label.config(text="Timer", fg=GREEN)
    #reset check_marks
    check_mark.config(text="")
    #reset reps 
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        time_display(long_sec)
        timer_label.config(text="Break", fg=GREEN)
        messagebox.showinfo(title="Information", message="You can take break")
    elif reps % 2 == 0:
        time_display(short_sec)  
        timer_label.config(text="Break", fg=PINK) 
        messagebox.showinfo(title="Information", message="You can take a break")
    else:
        time_display(work_sec)     
        timer_label.config(text="Work", fg=RED)
        messagebox.showinfo(title="Information", message="You have to work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def time_display(timer):
    timer_min = math.floor(timer / 60)
    timer_sec = timer % 60
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"
    timer_display = f"{timer_min}:{timer_sec}"    
    canvas.itemconfig(timer_text, text=timer_display)
    if timer > 0:
        global canvas_timer
        canvas_timer = window.after(1000, time_display, timer - 1)
    else: 
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=20, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Pomdoro/tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

 
start_button = Button(width=10, text="Start",highlightbackground=YELLOW,highlightcolor=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(width=10, text="Reset",highlightbackground=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

check_mark= Label(font=(FONT_NAME, 30, "normal"), highlightthickness=0, bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=4)


window.mainloop()