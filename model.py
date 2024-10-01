import sqlite3

class TodoModel:
    def __init__(self):
        # Initialize database connection
        self.conn = sqlite3.connect("todo.db")
        self.cursor = self.conn.cursor()
        # Create tasks table if it doesn't exist
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")

    def add_task(self, task):
        # Insert a new task into the database
        self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        self.conn.commit()

    def get_tasks(self):
        # Retrieve all tasks from the database
        self.cursor.execute("SELECT * FROM tasks")
        return [row[0] for row in self.cursor.fetchall()]

    def delete_task(self, task):
        # Delete a specific task from the database
        self.cursor.execute("DELETE FROM tasks WHERE task = ?", (task,))
        self.conn.commit()

    def close(self):
        # Close the database connection
        self.conn.close()
