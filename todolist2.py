# todolist2.py 2024
# imports
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import os

# variables
current_path = os.path.dirname(os.path.realpath(__file__))
END = True
app = tk.Tk()
font_1 = ("Arial", 30, "bold")
font_2 = ("Arial", 18, "bold")
font_3 = ("Arial", 10, "bold")

# author
ctk.CTkLabel(master=app, text="Raymond de Vries", font=("Arial", 7), text_color="dark grey").grid(row=1, column=0, padx=55, pady=0, sticky="sw")

# functions
def add_task():
    task = prompt.get()
    if task:
        task_list.insert(0, task)
        prompt.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showerror("Error", "Enter a task")

def remove_tasks():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected[0])
        save_tasks() 
    else:
        messagebox.showerror("Error", "Choose a task to delete") 
        
def save_tasks():
    with open("memory", "w") as f:
        tasks = task_list.get(0, END)
        for task in tasks:
            f.write(task + "\n")          

def load_tasks():
    try:
        with open("memory", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                task_list.insert(0, task.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "Cannot load task")
        
def on_closing():
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
        app.destroy()


# ui
app.title("to do list")
app.geometry("900x600")
app.bg_image = ctk.CTkImage(Image.open(current_path + "/images/vecteezy_to-do-list.png"), size=(400,400))
app.bg_image_label = ctk.CTkLabel(app, image=app.bg_image, text = "")
app.bg_image_label.grid(row=1, column=0, pady=50)
app.bg_image_label.grid(row=0, column=0)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue") 

tasks_text = ctk.CTkLabel(master=app, text="Your tasks:", font=font_1, text_color="black") 
tasks_text.grid(row=0, column=1, padx=50, pady=50, sticky="nw")

task_list = tk.Listbox(master=app, width=47, height=15, font=font_3, background="grey")
task_list.grid(row=0, column=1, padx=1)

prompt = ctk.CTkEntry(master=app, font=font_2, width=330, height=28, corner_radius=2, text_color="black", fg_color="white")
prompt.grid(row=1, column=1, padx=1)

add_task_button = ctk.CTkButton(master=app, font=font_2, height=40, width=80, fg_color="blue", command=add_task, text="add task", hover_color="light blue")
add_task_button.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")
add_task_button.bind("<Enter>", lambda event: add_task_button.configure(text_color="black"))
add_task_button.bind("<Leave>", lambda event: add_task_button.configure(text_color="light grey"))

remove_task_button = ctk.CTkButton(master=app, font=font_2, height=40, width=80, text_color="white", fg_color="blue", command=remove_tasks, text="remove task", hover_color="red")
remove_task_button.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="e")

# on close
app.protocol("WM_DELETE_WINDOW", on_closing)

# run
load_tasks()
app.mainloop()
