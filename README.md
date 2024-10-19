# Task Manager in Python with SQLite

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Prerequisites](#prerequisites)
5. [Project Setup](#project-setup)
6. [How to Run the Project](#how-to-run-the-project)
7. [Code Explanation](#code-explanation)
   - [1. Database Connection](#1-database-connection)
   - [2. Creating the Tasks Table](#2-creating-the-tasks-table)
   - [3. Adding Tasks](#3-adding-tasks)
   - [4. Viewing Tasks](#4-viewing-tasks)
   - [5. Updating Tasks](#5-updating-tasks)
   - [6. Deleting Tasks](#6-deleting-tasks)
   - [7. Command-Line Interface (CLI)](#7-command-line-interface-cli)
8. [Future Improvements](#future-improvements)

---

## Project Overview

This is a simple **Task Manager** application built using **Python** and **SQLite**. The application allows you to perform the basic CRUD operations:

- **Create**: Add new tasks.
- **Read**: View all tasks.
- **Update**: Update existing tasks.
- **Delete**: Delete tasks.

The project uses SQLite as a database to store tasks, and all interactions are done via the command line interface (CLI).

## Features

- Add new tasks with a title and description.
- View all tasks in the database.
- Update a task's title, description, and status.
- Delete tasks by their ID.
- A simple command-line interface for user interaction.

## Technologies Used

- **Python** (version 3.7+)
- **SQLite** (Python `sqlite3` module)

## Prerequisites

Before you begin, ensure that you have met the following requirements:

- Python 3.7 or higher installed on your local machine.
- Basic knowledge of Python and SQL.

## Project Setup

1. Clone the repository or download the project files.

```bash
   git clone https://github.com/yourusername/task-manager-sqlite.git
```

2. Navigate to the project folder.

```bash
cd task-manager-sqlite
```

3. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

## How to Run the Project

1. Make sure you have Python 3.7+ installed and your virtual environment activated (if using one).

2. Run the Python script.

```bash
python task_manager.py
```

3. Follow the command-line prompts to add, view, update, or delete tasks.

## Code Explanation

Here’s a breakdown of the major components of the project:

1. Database Connection
   The project connects to an SQLite database using the sqlite3 module. The connect() function creates a connection to a database file named tasks.db. If the file doesn’t exist, SQLite will create it.

```bash
import sqlite3

def connect():
    return sqlite3.connect('tasks.db')
```

2. Creating the Tasks Table
   The create_table() function ensures that the tasks table is created when the project starts. If the table doesn’t exist, it is created with columns for id, title, description, and status.

```bash
def create_table():
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        status TEXT DEFAULT 'Pending'
                    )''')
        conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()
```

3. Adding Tasks
   The add_task() function allows you to add new tasks to the database. Each task has a title and an optional description. The status is set to 'Pending' by default.

```bash
def add_task(title, description):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
        conn.commit()
        print("Task added successfully!")
    except Exception as e:
        print(f"Error adding task: {e}")
    finally:
        conn.close()
```

4. Viewing Tasks
   The view_tasks() function retrieves all tasks from the database and prints them in a readable format. It fetches all rows from the tasks table using cur.fetchall()

```bash
def view_tasks():
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}, Status: {row[3]}")
    except Exception as e:
        print(f"Error fetching tasks: {e}")
    finally:
        conn.close()
```

5. Updating Tasks
   The update_task() function allows you to update an existing task's title, description, or status. It builds the update query dynamically based on which fields are provided.

```bash
def update_task(task_id, title=None, description=None, status=None):
    conn = connect()
    try:
        cur = conn.cursor()
        updates = []
        params = []

        if title:
            updates.append("title = ?")
            params.append(title)
        if description:
            updates.append("description = ?")
            params.append(description)
        if status:
            updates.append("status = ?")
            params.append(status)

        if not updates:
            print("No fields provided to update.")
            return

        query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
        params.append(task_id)

        cur.execute(query, params)
        conn.commit()
        print("Task updated successfully!")
    except Exception as e:
        print(f"Error updating task: {e}")
    finally:
        conn.close()

```

6. Deleting Tasks
   The delete_task() function deletes a task based on its ID. It uses the DELETE SQL statement and removes the specified task from the database.

```bash
def delete_task(task_id):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        print("Task deleted successfully!")
    except Exception as e:
        print(f"Error deleting task: {e}")
    finally:
        conn.close()

```

7. Command-Line Interface (CLI)
   The main() function serves as the command-line interface. It presents the user with options to add, view, update, or delete tasks. Based on the user's input, the corresponding function is called.

```bash
def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to skip): ")
            description = input("Enter new description (leave blank to skip): ")
            status = input("Enter new status (leave blank to skip): ")
            update_task(task_id, title or None, description or None, status or None)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

```

## Future Improvements

- Add a user authentication system to manage tasks for multiple users.
- Create a GUI using a framework like Tkinter or PyQt.
- Allow task prioritization and deadlines.
- Implement filtering and sorting options for tasks.

> Thank you for checking out this project! Your interest and contributions are highly appreciated. If you have any questions or feedback, don't hesitate to reach out or open an issue on GitHub. Happy coding! 🙂
