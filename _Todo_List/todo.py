from tkinter import *

tasks = []

def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)

root = Tk()

root.title("To-Do List")
root.geometry("400x500")
root.config(bg="lightblue")

title = Label(root, text="To-Do List", font=("Arial", 20, "bold"), bg="lightblue")
title.pack(pady=10)

task_entry = Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

add_btn = Button(root, text="Add Task", bg="green", fg="white", font=("Arial", 12), command=add_task)
add_btn.pack(pady=5)

delete_btn = Button(root, text="Delete Task", bg="red", fg="white", font=("Arial", 12), command=delete_task)
delete_btn.pack(pady=5)

listbox = Listbox(root, font=("Arial", 14), width=30, height=12)
listbox.pack(pady=20)

root.mainloop()