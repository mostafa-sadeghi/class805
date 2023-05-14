import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def calculate():
    value = feet.get()
    res = float(value) / 3.2808
    res = f'{res:.2f}'
    meters.set(res)


root = ttk.Window(themename="darkly")
root.title("Feet to Meters")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
# root.geometry("250x140")
# root.resizable(False, False)
main_frame = ttk.Frame(root, padding=(10, 40, 10, 40))
main_frame.grid(column=0, row=0, sticky="NWES")
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
feet = tk.StringVar()
feet_entry = ttk.Entry(main_frame, width=7,
                       textvariable=feet, font=(
                           "Arial", 18))


feet_entry.grid(column=1, row=0, sticky="WE")
meters = tk.StringVar()
ttk.Label(main_frame, textvariable=meters, font=(
    "Arial", 28, 'bold')).grid(column=1, row=1,
                               sticky="WE")
ttk.Button(main_frame, text="Calculate",
           cursor="hand2", command=calculate,
           padding=(50, 20),
           bootstyle="danger outline").grid(
    column=2, row=2, sticky="NSWE")
ttk.Label(main_frame, text="feet", font=(
    "Arial", 18), padding=(15, 2),
    foreground="red").grid(
    column=2, row=0, sticky="w")
ttk.Label(main_frame, font=(
    "Arial", 18), foreground="gray",
    text="is equivalent to").grid(
    column=0, row=1, sticky="E")
ttk.Label(main_frame, font=(
    "Arial", 18), text="meters",
    foreground="green",
    padding=(15, 2)).grid(
    column=2, row=1, sticky="W")
root.mainloop()
