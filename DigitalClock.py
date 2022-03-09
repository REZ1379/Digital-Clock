import tkinter as tk
import pyfiglet as pf
from time import strftime as st
from termcolor2 import colored as cd
print(cd(pf.figlet_format("""Created by :
\"Reza Rafiee\"\n08-Mar-22"""), "red"))
Win = tk.Tk()
Win.geometry("480x80")
Win.resizable(0, 0)
Win.configure(bg="#030924")
Win.title("Digital Clock \U0001F551")
lb1 = tk.Label(Win, font=("Arial", 20, "italic"), fg="#608ebf", bg="#030924")
lb1.pack(anchor="center", padx=15, pady=20)


def time():
    string = st(" %a  |  %b-%d-%Y  |  %I:%M:%S %p ")
    lb1.config(text=string)
    lb1.after(1000, time)


time()
Win.mainloop()
