from tkinter import *
import math

reps = 0
timer = ""

# Constants
YELLOW = "#FFEBB7"
BROWN = "#AD8E70"
TOMATO = "#F26849"
NAVY = "#243763"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# Timer reset
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=TOMATO)
    check_label.config(text="")
    start_button.config(state=NORMAL)
    global reps
    reps = 0


# Timer mechanism
def start_time():
    start_button.config(state=DISABLED)
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        title_label.config(text="Work", fg=TOMATO)
        count_down(work_sec)
    elif reps % 2 == 0:
        if reps != 8:
            title_label.config(text="Break", fg=YELLOW)
            count_down(short_break_sec)
        else:
            title_label.config(text="Break", fg=BROWN)
            reps = 0
            count_down(long_break_sec)


# Countdown mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            check_label.config(text=check_label["text"] + "🗸")
        start_time()


# Windows settings
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=NAVY)

# Canvas and img
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=NAVY, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Label title
title_label = Label(text="Timer", fg=TOMATO, bg=NAVY, font=(FONT_NAME, 30, "bold"))
title_label.grid(row=0, column=1)

# Label check
check_label = Label(bg=NAVY, fg=TOMATO, font=(FONT_NAME, 30, "bold"))
check_label.grid(row=3, column=1)

# Button Start
start_button = Button(text="Start", highlightthickness=0, command=start_time)
start_button.grid(row=2, column=0)

# Button Reset
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
