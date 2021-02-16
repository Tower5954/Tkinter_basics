import tkinter as tk
from tkinter import ttk


def greet():
    # print(f"Greetings, {user_name.get() or 'Minion'}!")
    print(f"Hello {user_name.get() or 'minion'}!")

root = tk.Tk()
root.title("Greetings")

user_name = tk.StringVar()

# input_frame = ttk.Frame(root, padding=(20, 10, 20, 10))
# input_frame.grid()
#
# name_label = ttk.Label(input_frame , text='Name: ')
# name_label.grid()
# name_entry = ttk.Entry(input_frame , width=15, textvariable=user_name)
# name_entry.grid()
# name_entry.focus()
#
# buttons = ttk.Frame(root, padding=(20, 10))
# buttons.grid()
#
# greet_button = ttk.Button(buttons, text='Greet', command=greet)
# greet_button.grid()
# quit_button = ttk.Button(buttons, text='Quit', command=root.destroy)
# quit_button.grid()
#
#
# root.mainloop()

# ----- with grid geometry ------ #
root.columnconfigure(0, weight=1)

input_frame = ttk.Frame(root, padding=(20, 10, 20, 10))
input_frame.grid(row=0, column=0)
input_frame.grid(row=0, column=0, sticky='EW')

name_label = ttk.Label(input_frame, text='Name: ')
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10))
# buttons.grid()
buttons.grid(row=1, column=0, sticky='EW')

# buttons.columnconfigure(0, weight=1)
# buttons.columnconfigure(1, weight=1)
buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

greet_button = ttk.Button(buttons, text='Greet', command=greet)
# greet_button.grid(row=0, column=0)
greet_button.grid(row=0, column=0, sticky='EW')
quit_button = ttk.Button(buttons, text='Quit', command=root.destroy)
# quit_button.grid(row=0, column=1)
quit_button.grid(row=0, column=1, sticky='EW')


root.mainloop()