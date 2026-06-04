import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.title("My To-Do List")
window.geometry("450x500")
window.config(bg="lightblue")

# ---------------- FUNCTIONS ----------------

# Add task
def add_task():
    task = entry_box.get()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        task_list.insert(tk.END, task)
        entry_box.delete(0, tk.END)

# Delete selected task
def delete_task():
    selected = task_list.curselection()

    if selected:
        task_list.delete(selected)
    else:
        messagebox.showwarning("Warning", "Please select a task")

# Clear all tasks
def clear_tasks():
    task_list.delete(0, tk.END)

# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="TO-DO LIST",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)

title.pack(pady=15)

# ---------------- ENTRY BOX ----------------

entry_box = tk.Entry(
    window,
    width=30,
    font=("Arial", 15)
)

entry_box.pack(pady=10)

# ---------------- BUTTONS ----------------

add_button = tk.Button(
    window,
    text="Add Task",
    width=15,
    bg="green",
    fg="white",
    font=("Arial", 12),
    command=add_task
)

add_button.pack(pady=5)

delete_button = tk.Button(
    window,
    text="Delete Task",
    width=15,
    bg="red",
    fg="white",
    font=("Arial", 12),
    command=delete_task
)

delete_button.pack(pady=5)

clear_button = tk.Button(
    window,
    text="Clear All",
    width=15,
    bg="orange",
    fg="white",
    font=("Arial", 12),
    command=clear_tasks
)

clear_button.pack(pady=5)

# ---------------- TASK LIST ----------------

task_list = tk.Listbox(
    window,
    width=35,
    height=12,
    font=("Arial", 14),
    selectbackground="blue"
)

task_list.pack(pady=20)

# Run application
window.mainloop()