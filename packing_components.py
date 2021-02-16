import tkinter as tk

root = tk.Tk()
root.geometry('600x370')

# rectangle_1 = tk.Label(root, text='Rectangle 1 ', bg='green', fg='white')
# rectangle_1.pack(ipadx=10, ipady=10)
# rectangle_1.pack(ipadx=10, ipady=10, fill='x')
# rectangle_1.pack(ipadx=10, ipady=10, fill='both', expand=True)

# rectangle_2 = tk.Label(root, text='Rectangle 2 ', bg='white', fg='green')
# rectangle_2.pack(ipadx=10, ipady=10)
# rectangle_2.pack(ipadx=10, ipady=10, fill='x')
# rectangle_2.pack(ipadx=10, ipady=10, expand=True)

rectangle_3 = tk.Label(root, text='Rectangle 1 ', bg='green', fg='white')
rectangle_3.pack(side='left', ipadx=10, ipady=10, fill='both')

rectangle_4 = tk.Label(root, text='Rectangle 2 ', bg='white', fg='green')
rectangle_4.pack(ipadx=10, ipady=10, fill='both')

root.mainloop()
