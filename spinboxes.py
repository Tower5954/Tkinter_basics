import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x371')
root.resizable(False, False)
root.title("widget examples")

initial_value = tk.IntVar(value=30)
spin_box = tk.Spinbox(
    root,
    from_=0,
    to=30,
    textvariable=initial_value,
    wrap=False
)
spin_box.pack()

print(spin_box.get())

initial_value = tk.StringVar(value=20)
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=30,
    textvariable=initial_value,
    wrap=False
)
spin_box.pack()

print(spin_box.get())



root.mainloop()