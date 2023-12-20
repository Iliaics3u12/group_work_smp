import tkinter as tk
from tkinter import messagebox

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return a

def factorial(n):
    if n < 0:
        return "Input should be a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

def calculate_factorial():
    try:
        num = int(entry_factorial.get())
        result = factorial(num)
        messagebox.showinfo("Factorial", f"The factorial of {num} is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

def calculate_fibonacci():
    try:
        position = int(entry_fibonacci.get())
        result = fibonacci(position)
        messagebox.showinfo("Fibonacci", f"The {position}th fibonacci number is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

def select_factorial():
    label_fibonacci.pack_forget()
    entry_fibonacci.pack_forget()
    button_fibonacci.pack_forget()
    label_factorial.pack()
    entry_factorial.pack()
    button_factorial.pack()

def select_fibonacci():
    label_factorial.pack_forget()
    entry_factorial.pack_forget()
    button_factorial.pack_forget()
    label_fibonacci.pack()
    entry_fibonacci.pack()
    button_fibonacci.pack()


root = tk.Tk()
root.title("Factorial and Fibonacci Calculator")


root.geometry("250x200")


button_select_factorial = tk.Button(root, text="Calculate Factorial", command=select_factorial)
button_select_factorial.pack()
button_select_fibonacci = tk.Button(root, text="Calculate Fibonacci", command=select_fibonacci)
button_select_fibonacci.pack()


label_factorial = tk.Label(root, text="Enter a number for factorial:")
entry_factorial = tk.Entry(root)
button_factorial = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)


label_fibonacci = tk.Label(root, text="Enter a position for fibonacci:")
entry_fibonacci = tk.Entry(root)
button_fibonacci = tk.Button(root, text="Calculate Fibonacci", command=calculate_fibonacci)


root.mainloop()

