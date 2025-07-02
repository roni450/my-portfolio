import tkinter as tk

root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")  # App background color

# Entry field
entry = tk.Entry(root, font=("Arial", 24), bg="#ffffff", fg="#000000", borderwidth=4, relief="ridge", justify="right")
entry.pack(pady=20, padx=10, fill="x")

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

btn_bg = "#e0e0e0"
btn_fg = "#000000"
btn_active_bg = "#cccccc"

for row in buttons:
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: click(x) if x != "=" else calculate()
        tk.Button(
            frame,
            text=btn,
            font=("Arial", 18),
            command=action,
            bg=btn_bg,
            fg=btn_fg,
            activebackground=btn_active_bg,
            padx=10, pady=10
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)

tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    bg="red",
    fg="white",
    activebackground="#aa0000",
    command=clear
).pack(fill="x", padx=10, pady=5)

root.mainloop()
