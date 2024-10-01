import tkinter as tk

from model import TodoModel
from view import TodoView

# Controller: Mediates between the Model and View
class TodoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Set up command bindings
        self.view.set_add_task_command(self.add_task)
        self.view.set_delete_task_command(self.delete_task)
        # Initial view update
        self.update_view()

    def add_task(self):
        # Add a new task
        task = self.view.get_task_input()
        if task:
            self.model.add_task(task)
            self.view.clear_task_input()
            self.update_view()

    def delete_task(self):
        # Delete the selected task
        task = self.view.get_selected_task()
        if task:
            self.model.delete_task(task)
            self.update_view()

    def update_view(self):
        # Update the view with current tasks
        tasks = self.model.get_tasks()
        self.view.update_task_list(tasks)

def main():
    # Create the main application window
    root = tk.Tk()
    # Initialize MVC components
    model = TodoModel()
    view = TodoView(root)
    controller = TodoController(model, view)
    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()