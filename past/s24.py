import tkinter as tk


def number1():
    number1.set("1")


def add():
    result = int(number1) + int(number2)
    out.set(result)


root = tk.Tk()

number1 = tk.StringVar()
number2 = tk.StringVar()

out = tk.StringVar()
b1 = tk.Button(root, text="1", command=number1)
b1.grid(row=0, column=0)
b2 = tk.Button(root, text="2")
b2.grid(row=0, column=1)
bAdd = tk.Button(root, text="+", command=add)
bAdd.grid(row=0, column=2)
bequal = tk.Button(root, text="=")
bequal.grid(row=0, column=3)


output = tk.Label(root, textvariable=out)
bequal.grid(row=0, column=4)

root.mainloop()
