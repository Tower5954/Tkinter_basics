import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("600x371")
root.resizable(False, False)
root.title('widget examples')

text = tk.Text(root, height=8)
text.pack()

text.insert('1.5', "Please enter a comment...")
# 1.0 means start at the 1 line 0 character 'apparently' ???
# --- to disable the writing function --- #
# text['state'] = 'disabled'

# this will get the inputted text
text_content = text.get('1.0', 'end')

root.mainloop()
