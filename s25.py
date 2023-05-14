# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def move(self):
#         print(f'{self.name} is moving')


# car_1 = Car("pride X2000", 1910)
# car_2 = Car("BMW X6", 2020)

# car_1.move()
# car_2.move()

import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry_value = ''
        tk.Entry(master, width=17, bg="#ccddff", font=(
            'Arial', 28), textvariable=self.equation).pack()
        tk.Button(master, text="7", command=lambda: self.show(
            '7'), padx=10, pady=10, font=20).pack(side="left")
        tk.Button(master, text="+", command=lambda: self.show(
            '+'), padx=10, pady=10, font=20).pack(side="left")
        tk.Button(master, text="=", command=self.solve,
                  padx=10, pady=10, font=20).pack(side="left")

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        print(result)
        self.equation.set(result)


root = tk.Tk()
calc = Calculator(root)

root.mainloop()
