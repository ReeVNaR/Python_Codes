import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def add_task():
    task = simpledialog.askstring("Add Task", "Enter task to add:")
    if task:
        tasks.append(task)
        update_task_list()

def remove_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Remove Task", "No task selected.")
        return
    idx = selected[0]
    removed = tasks.pop(idx)
    update_task_list()
    messagebox.showinfo("Task Removed", f"Removed: {removed}")

root = tk.Tk()
root.title("📝 To-Do List")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

task_listbox = tk.Listbox(frame, width=40, height=10)
task_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

btn_frame = tk.Frame(frame)
btn_frame.pack(fill=tk.X, pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)

remove_btn = tk.Button(btn_frame, text="Remove Task", command=remove_task)
remove_btn.pack(side=tk.LEFT, padx=5)

exit_btn = tk.Button(btn_frame, text="Exit", command=root.destroy)
exit_btn.pack(side=tk.RIGHT, padx=5)

update_task_list()
root.mainloop()
