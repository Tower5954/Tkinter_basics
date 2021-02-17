import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x371')
root.resizable(False, False)
root.title("widget examples")

programming_languages = ("C", "Go", "Javascript", "Perl", "Python", "Rust")

langs = tk.StringVar(value=programming_languages)
# langs_select = tk.Listbox(root, listvariable=langs, height=6)
langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode='extended')
# or langs_selected['selectmode'] = 'extended' # 'browse' is the counter part that selects just one
langs_select.pack()

def handle_selection_change(event):
    selected_indices = langs_select.curselection()
    for i in selected_indices:
        print(langs_select.get(i))


langs_select.bind("<<ListboxSelect>>", handle_selection_change)

root.mainloop()