import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("1200x800")

# Store the original background color
original_color = root.cget("bg")

def flash_green():
    root.config(bg="green")           # Change background to green
    root.after(500, reset_color)      # Wait 500 ms (0.5 sec), then reset

def reset_color():
    root.config(bg=original_color)    # Change it back

label = tk.Label(root, text="Hello World!")
label.pack()

button = tk.Button(root, text="Click Me", command=flash_green)
button.pack()

root.mainloop()