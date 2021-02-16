import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# from windows import set_dpi_awareness
#
# set_dpi_awareness()

root = tk.Tk()
root.geometry("600x371")
root.resizable(False, False)
root.title('widget examples')

# image = Image.open('/home/skavenslayer59/PycharmProjects/Tkinter_basics/towbot1.png')
# image = Image.open('/home/skavenslayer59/PycharmProjects/Tkinter_basics/towbot1.png').resize((264, 264))
# photo = ImageTk.PhotoImage(image)
# # label = ttk.Label(root, image=photo, padding=5)
# # label = ttk.Label(root, text='Towbot', image=photo, padding=5, compound='right')
# # label = ttk.Label(root, text='Towbot', image=photo, padding=5, compound='center')
# label = ttk.Label(root, text='Towbot', image=photo, padding=5, compound='top')
# label.pack()

# label = ttk.Label(root, text='hello world', padding=20)
# label.config(font=('Segoe UI', 20))
# label.pack()

greeting = tk.StringVar()

label = ttk.Label(root, padding=10, textvariable=greeting)
label.pack()

greeting.set('Hello, Grant!')


root.mainloop()