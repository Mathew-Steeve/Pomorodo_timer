import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    global REPS
    REPS = 0
    tick_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    REPS += 1

    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 9 == 0:
        reset_timer()
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1, count_down, count-1)
    else:
        start_timer()
        tick_mark = ""
        for _ in range(math.floor(REPS / 2)):
            tick_mark += TICK
        tick_label.config(text=tick_mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

window.mainloop()
