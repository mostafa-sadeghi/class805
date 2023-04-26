import tkinter as tk
from tkinter import ttk


def submit():
    print(user_name.get())


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)

main_frame = ttk.Frame(root)
main_frame.pack()

user_name_label = ttk.Label(
    main_frame, text="user name", font=14, padding=(0, 0, 10, 0))
user_name_label.pack(side="left")
user_name = ttk.Entry(main_frame, font=14, foreground="red")
user_name.pack(side="left")

buttons_frame = ttk.Frame(root)
buttons_frame.pack()

submit_button = ttk.Button(
    buttons_frame, text="Submit", command=submit, padding=10)
submit_button.pack(side="left", padx=10, pady=10)
quit_button = ttk.Button(buttons_frame, text="quit",
                         command=root.destroy, padding=10)
quit_button.pack(side="left", padx=10, pady=10)


root.mainloop()
