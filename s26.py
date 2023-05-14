import tkinter as tk


def show(value):
    global our_result
    our_result += value
    number.set(our_result)


root = tk.Tk()
our_result = ''
number = tk.StringVar()
tk.Entry(root, width=17, textvariable=number).pack()
tk.Button(root, text="7", command=lambda: show('7')).pack()


root.mainloop()
