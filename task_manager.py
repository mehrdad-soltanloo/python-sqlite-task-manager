import sqlite3

def connect():
    conn = sqlite3.connect('tasks.db')  # Creates 'tasks.db' file in the project folder
    return conn

def create_table():
    """create tasks table if it doesn't exist"""
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'Pending'
                    )''')
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()


def add_task(title,description):
    """add a new task to the database"""
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

def view_tasks(): 
    """Retrieve all tasks from the database """
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}, Status: {row[3]}")
    except Exception as e:
        print(f"Error fetching task: {e}")
    finally:
        conn.close()

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

            # If no fields to update, raise an error
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


def delete_task(task_id):
    """Delete a task from the database by its ID"""
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

def main():
    """Main CLI for interacting with the task manager"""
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
            add_task(title,description)
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


if __name__ == "__main__":
    create_table()
    main()

        