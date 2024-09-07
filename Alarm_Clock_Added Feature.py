from tkinter import *
from tkinter import messagebox
import datetime
import time
from threading import Thread
from pygame import mixer

root = Tk()

root.geometry("900x700")


def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    # Mapping weekdays from the dropdown to weekday numbers (Monday=0, ..., Sunday=6)
    day_map = {"Monday": 0, "Tuesday": 1,
               "Wednesday": 2, "Thursday": 3,
               "Friday": 4, "Saturday": 5,
               "Sunday": 6}
    selected_day_num = day_map[
        date.get()]  # Get the selected day's number

    while True:
        # Check if today is the selected day
        current_day_num = datetime.datetime.now().weekday()
        if current_day_num != selected_day_num:
            time.sleep(1)
            continue  # Skip the rest of the loop if it's not the selected day

        sat = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        cat = datetime.datetime.now().strftime(
            "%H:%M:%S")
        print(sat, cat)
        if sat == cat:
            print("Hurry up!")
            mixer.init()
            if song.get() == "OX":
                mixer.music.load("Ox.wav")
            elif song.get() == "Ox2":
                mixer.music.load("Ox2.wav")
            elif song.get() == "S1":
                mixer.music.load("song.wav")
            mixer.music.play()
            break  # Stop checking after the alarm goes off


def stop_alarm():
    mixer.music.stop()


# Validate time input
def validate_time(new_value, max_value):
    if new_value == "" or new_value.isdigit():
        if new_value == "" or 0 <= int(
                new_value) <= max_value:
            return True
        else:
            messagebox.showwarning(
                "Invalid Input",
                f"Please enter a valid value (0-{max_value}).")
            return False
    else:
        messagebox.showwarning("Invalid Input",
                               "Please enter numbers only.")
        return False


validate_hour_cmd = (
root.register(lambda v: validate_time(v, 23)),
'%P')
validate_min_sec_cmd = (
root.register(lambda v: validate_time(v, 59)),
'%P')

# Time selection setup
Label(root, text="Alarm", font=("Arial 20 bold"),
      fg="blue").pack(pady=10)
Label(root, text="Set Time",
      font=("Arial 20 bold")).pack()

frame_time = Frame(root)
frame_time.pack()

hour = StringVar(root)
hour.set("00")
hrs = Entry(frame_time, textvariable=hour,
            width=5, validate='key',
            validatecommand=validate_hour_cmd)
hrs.pack(side=LEFT)

minute = StringVar(root)
minute.set("00")
mins = Entry(frame_time, textvariable=minute,
             width=5, validate='key',
             validatecommand=validate_min_sec_cmd)
mins.pack(side=LEFT)

second = StringVar(root)
second.set("00")
secs = Entry(frame_time, textvariable=second,
             width=5, validate='key',
             validatecommand=validate_min_sec_cmd)
secs.pack(side=LEFT)

# Day selection setup
Label(root, text="Set Date",
      font=("Arial 20 bold")).pack()

frame_date = Frame(root)
frame_date.pack()

date = StringVar(root)
dates = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday",
         "Sunday"]
date.set("Monday")  # Default value
sos = OptionMenu(frame_date, date, *dates)
sos.pack()

# Sound selection setup
Label(root, text="Set Sound",
      font=("Arial 20 bold")).pack()
frame_sound = Frame(root)
frame_sound.pack()

song = StringVar(root)
songs = ["OX", "Ox2", "S1"]
song.set("OX")  # Default value
sos = OptionMenu(frame_sound, song, *songs)
sos.pack()

# Alarm control buttons
Button(root, text="Set alarm", font=("arial 15"),
       command=Threading).pack(pady=20)
Button(root, text="Stop alarm", bg="red",
       fg="blue", command=stop_alarm).pack(
    pady=40)

root.mainloop()
