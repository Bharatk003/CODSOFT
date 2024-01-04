import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ITFT1 To-Do List")
        self.root.geometry("600x400")

        self.tasks = []

        # Create GUI components
        self.task_entry = ttk.Entry(root, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="ew")

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task, style="TButton", state='disable')
        self.add_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.update_button = ttk.Button(root, text="Update Task", command=self.update_task, style="TButton", state='disable')
        self.update_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.delete_button = ttk.Button(root, text="Delete Task", command=self.delete_task, style="TButton", state='disable')
        self.delete_button.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

        # Ensure task_listbox is created before calling load_tasks
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40, font=("Arial", 12), bd=2, relief="groove")
        self.task_listbox.grid(row=2, column=0, padx=10, pady=5, columnspan=3, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.task_listbox.yview)
        self.scrollbar.grid(row=2, column=3, pady=5, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.sizegrip = ttk.Sizegrip(root)
        self.sizegrip.grid(row=3, column=3, sticky="se")

        # Populate initial tasks (if any)
        self.load_tasks()  # Load tasks from the file when the app starts

        # Bind entry change event
        self.task_entry.bind("<KeyRelease>", self.on_entry_change)

        # Configure row and column weights for resizing
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=0)
        root.rowconfigure(0, weight=0)
        root.rowconfigure(1, weight=0)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=0)

    # ... (rest of the code remains the same)


    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()  # Save tasks to the file after adding a new task
            messagebox.showinfo("Task Added", "Task has been added successfully.")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()
            self.save_tasks()  # Save tasks to the file after deleting a task
            messagebox.showinfo("Task Deleted", "Task has been deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Select a task to delete!")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index[0]] = updated_task
                self.update_task_list()
                self.task_listbox.selection_clear(0, tk.END)
                self.save_tasks()  # Save tasks to the file after updating a task
                messagebox.showinfo("Task Updated", "Task has been updated successfully.")
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        else:
            messagebox.showwarning("Warning", "Select a task to update!")

    def on_entry_change(self, *_):
        if self.task_entry.get():
            self.add_button['state'] = 'normal'
            selected_task_index = self.task_listbox.curselection()
            self.update_button['state'] = 'normal' if selected_task_index else 'disable'
            self.delete_button['state'] = 'normal' if selected_task_index else 'disable'
        else:
            self.add_button['state'] = 'disable'
            self.update_button['state'] = 'disable'
            self.delete_button['state'] = 'disable'

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")

    def save_tasks(self):
        with open("TO-DO_List/tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("TO-DO_List/tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass  # If the file is not found, no tasks will be loaded

        # Ensure the loaded tasks are displayed
        self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
