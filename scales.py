import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x371')
root.resizable(False, False)
root.title("widget examples")

# scale = ttk.Scale(root, orient='horizontal', from_=0, to=10)
# # scale.pack()
# scale.pack(fill='x')

def handle_scale_change(event):
    print(scale.get())

scale = ttk.Scale(root, orient='horizontal', from_=0, to=10, command=handle_scale_change)
# scale.pack()
scale.pack(fill='x')



root.mainloop()