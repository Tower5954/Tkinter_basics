import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x371')
root.resizable(False, False)
root.title("widget examples")

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday['values'] = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
# weekday['state'] = 'readonly'
weekday.pack()


def handle_selection(event):
    print('Today is', selected_weekday.get())
    print(weekday.current())


weekday.bind('<<ComboboxSelected>>', handle_selection)

root.mainloop()

print(selected_weekday.get(),'was selected')