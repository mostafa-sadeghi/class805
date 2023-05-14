import tkinter as tk
from tkinter import ttk
def greet():
    out_put_val.set(user_name2.get() + user_name.get())
root = tk.Tk()
user_name = tk.IntVar()
user_name2 = tk.IntVar()
out_put_val = tk.IntVar()
frame = ttk.Frame(root)
frame.pack()
user_name_entry_label = ttk.Label(frame, text="user name", font=14)
user_name_entry_label.pack(side="left", padx=(0, 5), pady=10)
user_name_entry = ttk.Entry(frame, textvariable=user_name, font=14)
user_name_entry.pack(side="left",  padx=(0, 5), pady=10)
user_name2_entry = ttk.Entry(frame, textvariable=user_name2, font=14)
user_name2_entry.pack(side="left",  padx=(0, 5), pady=10)
button_frame = ttk.Frame(root)
button_frame.pack()
greet_button = ttk.Button(button_frame, text="greet", command=greet)
greet_button.pack(side="left", padx=(0, 5), pady=10)
quit_button = ttk.Button(button_frame, text="quit", command=root.destroy)
quit_button.pack(side="left", padx=(0, 5), pady=10)
out_put = ttk.Label(textvariable=out_put_val)
out_put.pack()
root.mainloop()