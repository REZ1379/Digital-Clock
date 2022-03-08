import tkinter as tk
import pyfiglet as pf
from time import strftime as st
from termcolor2 import colored as cd
print(cd(pf.figlet_format("""Created by :
\"Reza Rafiee\"\n08-Mar-22"""), "yellow"))
Win = tk.Tk()
Win.title("Digital Clock \U0001F551")
lb1 = tk.Label(Win, font=("Arial", 20, "italic"), fg="black", bg="white")
lb1.pack(anchor="center")


def time():
    string = st(" %a | %b-%d-%Y | %H:%M:%S ")
    lb1.config(text=string)
    lb1.after(1000, time)


time()
Win.mainloop()
