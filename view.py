import tkinter as tk
from tkinter import messagebox

class TodoView:
    def __init__(self, master):
        self.master = master
        master.title("The To-Do List App")
        master.geometry("500x400")

        # Create and pack UI elements
        # Entry widget for task input
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=10)

        # Button to add tasks
        self.add_button = tk.Button(master, text="Add Task")
        self.add_button.pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(master, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Button to delete tasks
        self.delete_button = tk.Button(master, text="Delete Task")
        self.delete_button.pack(pady=5)

    def set_add_task_command(self, command):
        """
        Set the command for the Add Task button.

        Args:
            command (callable): The function to be called when the Add Task button is clicked.
        """
        self.add_button.config(command=command)

    def set_delete_task_command(self, command):
        """
        Set the command for the Delete Task button.

        Args:
            command (callable): The function to be called when the Delete Task button is clicked.
        """
        self.delete_button.config(command=command)

    def get_task_input(self):
        """
        Get the text from the task entry field.

        Returns:
            str: The text entered in the task entry field.
        """
        return self.task_entry.get()

    def clear_task_input(self):
        """
        Clear the task entry field.
        """
        self.task_entry.delete(0, tk.END)

    def update_task_list(self, tasks):
        """
        Update the listbox with the current tasks.

        Args:
            tasks (list): A list of task strings to be displayed in the listbox.
        """
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            self.task_listbox.insert(tk.END, task)

    def get_selected_task(self):
        """
        Get the selected task from the listbox.

        Returns:
            str or None: The selected task string if a task is selected, None otherwise.
        """
        try:
            index = self.task_listbox.curselection()[0]
            return self.task_listbox.get(index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return None