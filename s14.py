import tkinter as tk
from tkinter import ttk


def hello():
    print('hello')


def hi():
    print('hi')


def bye():
    print('bye')


def good():
    print('good')


root = tk.Tk()

# frame one contains button Hello and button hi
frame1 = ttk.Frame(root)
frame1.pack()

# buttons
button_hello = ttk.Button(frame1, text="Hello!", command=hello)
button_hello.pack(side="left")
button_hi = ttk.Button(frame1, text="Hi!", command=hi)
button_hi.pack(side="left")


# frame two contains button bye and button good
frame2 = ttk.Frame(root)
frame2.pack()

# buttons
button_Bye = ttk.Button(frame2, text="bye", command=bye)
button_Bye.pack(side="left")
button_good = ttk.Button(frame2, text="good", command=good)
button_good.pack(side="left")


# exercise:
# اضافه کردن برچسب که نام هر یک از دکمه ها در آن نمایش داده شود
# تغییر اندازه دکمه ها
# تنظیم فاصله میان دکمه ها

root.mainloop()
