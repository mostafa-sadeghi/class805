import tkinter as tk
from tkinter import ttk


def greet():
    print(f'{name.get()} {family.get()}')


root = tk.Tk()

name = tk.StringVar()
family = tk.StringVar()


root.geometry('290x120')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)


frame_1 = ttk.Frame(root)
frame_1.grid(row=0, column=0, sticky="ewns", pady=5, padx=5)
frame_1.columnconfigure(0, weight=1)
frame_1.columnconfigure(1, weight=3)
frame_1.rowconfigure(0, weight=1)
name_label = ttk.Label(frame_1, text="name: ")
name_label.grid(row=0, column=0, sticky="ewns")
name_entry = ttk.Entry(frame_1, textvariable=name)
name_entry.grid(row=0, column=1, sticky="ewns")


frame_2 = ttk.Frame(root)
frame_2.grid(row=1, column=0, sticky="ewns", pady=5, padx=5)
frame_2.columnconfigure(0, weight=1)
frame_2.columnconfigure(1, weight=3)
frame_2.rowconfigure(0, weight=1)
family_label = ttk.Label(frame_2, text="family: ")
family_label.grid(row=0, column=0, sticky="ewns")
family_entry = ttk.Entry(frame_2, textvariable=family)
family_entry.grid(row=0, column=1, sticky="ewns")


frame_3 = ttk.Frame(root)
frame_3.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
frame_3.columnconfigure(0, weight=1)
frame_3.columnconfigure(1, weight=1)
frame_3.rowconfigure(0, weight=1)
greet_button = ttk.Button(frame_3, text="greet", command=greet)
greet_button.grid(row=0, column=0, sticky="ewsn", pady=5, padx=5)
quit_button = ttk.Button(frame_3, text="quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="ewsn", pady=5, padx=5)


root.mainloop()
