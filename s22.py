import tkinter as tk
# tkinter._test()
from tkinter import ttk


root = tk.Tk()
root.title("Feet to Meters")
root.geometry("250x140")
root.resizable(False, False)
main_frame = ttk.Frame(root, padding=(10, 40, 10, 40))
main_frame.grid(column=0, row=0, sticky="NWES")


feet = tk.StringVar()
feet_entry = ttk.Entry(main_frame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky="WE")

meters = tk.StringVar()
ttk.Label(main_frame, textvariable=meters).grid(column=2, row=2, sticky="WE")


ttk.Button(main_frame, text="Calculate").grid(column=3, row=3, sticky="W")

ttk.Label(main_frame, text="feet", padding=(15, 2, 15, 2)).grid(
    column=3, row=1, sticky="w")
ttk.Label(main_frame, text="is equivalent to").grid(
    column=1, row=2, sticky="E")
ttk.Label(main_frame, text="meters", padding=(15, 2, 15, 2)).grid(
    column=3, row=2, sticky="W")

root.mainloop()
