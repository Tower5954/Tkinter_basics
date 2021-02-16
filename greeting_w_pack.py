import tkinter as tk
from tkinter import ttk

# def greet():
#     # print(f"Greetings, {user_name.get() or 'Minion'}!")
#     print(f"Hello {user_name.get() or 'minion'}!")
#
# root = tk.Tk()
# root.title("Greetings")
#
# user_name = tk.StringVar()
#
# name_label = ttk.Label(root, text='Name: ')
# name_label.pack(side='left', padx=(0, 10))
# name_entry = ttk.Entry(root, width=15, textvariable=user_name)
# name_entry.pack(side='left')
# name_entry.focus()
#
# greet_button = ttk.Button(root, text='Greet', command=greet)
# greet_button.pack(side='left', fill='x', expand=True)
# quit_button = ttk.Button(root, text='Quit', command=root.destroy)
# quit_button.pack(side='right', fill='x', expand=True)


# ------ now with frames ------ #

def greet():
    # print(f"Greetings, {user_name.get() or 'Minion'}!")
    print(f"Hello {user_name.get() or 'minion'}!")

root = tk.Tk()
root.title("Greetings")

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 10))
input_frame.pack(fill='both')

name_label = ttk.Label(input_frame , text='Name: ')
name_label.pack(side='left', padx=(0, 10))
name_entry = ttk.Entry(input_frame , width=15, textvariable=user_name)
name_entry.pack(side='left')
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill='both')

greet_button = ttk.Button(buttons, text='Greet', command=greet)
greet_button.pack(side='left', fill='x', expand=True)
quit_button = ttk.Button(buttons, text='Quit', command=root.destroy)
quit_button.pack(side='right', fill='x', expand=True)


root.mainloop()