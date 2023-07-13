import tkinter as tk

def my_function():
    name = textbox.get()
    message = "Hello, " + name + "!"
    label.config(text=message)

root = tk.Tk()
root.title("My GUI Program")

label = tk.Label(root, text="Enter your name:")
textbox = tk.Entry(root)
button = tk.Button(root, text="Press here!", command=my_function)

label.grid(row=0, column=0)
textbox.grid(row=0, column=1)
button.grid(row=1, column=0)

root.mainloop()
