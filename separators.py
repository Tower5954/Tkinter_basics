import tkinter as tk
from tkinter import ttk

# root = tk.Tk()
# root.geometry('600x371')
# root.resizable(False, False)
# root.title("widget examples")
#
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
#
# ttk.Label(root, text='Hello, world!', padding=20).pack()
#
#
# ttk.Label(root, text='Hello, world!!', padding=20).pack()
#
# root.mainloop()

root = tk.Tk()
root.geometry('600x371')
root.resizable(False, False)
root.title("widget examples")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

ttk.Label(root, text='Hello, world!', padding=20).pack()

ttk.Separator(root, orient='horizontal').pack(fill='x')

ttk.Label(root, text='Hello, world!!', padding=20).pack()

root.mainloop()