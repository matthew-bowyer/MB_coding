# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create files if they don't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w"): pass

if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read tasks
with open("tasks.txt", 'r') as task_file:
    task_data = [t for t in task_file.read().split("\n") if t != ""]

task_list = []
for t_str in task_data:
    task_components = t_str.split(";")
    task = {
        'username': task_components[0],
        'title': task_components[1],
        'description': task_components[2],
        'due_date': datetime.strptime(task_components[3], DATETIME_STRING_FORMAT),
        'assigned_date': datetime.strptime(task_components[4], DATETIME_STRING_FORMAT),
        'completed': task_components[5] == "Yes"
    }
    task_list.append(task)

# Read user data
with open("user.txt", 'r') as user_file:
    user_data = [u for u in user_file.read().split("\n") if u]

username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

#========== Functions ==========

def save_tasks():
    with open("tasks.txt", "w") as task_file:
        task_file.write("\n".join(
            f"{t['username']};{t['title']};{t['description']};{t['due_date'].strftime(DATETIME_STRING_FORMAT)};"
            f"{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if t['completed'] else 'No'}"
            for t in task_list
        ))

def reg_user():
    while True:
        new_username = input("New Username: ")
        if new_username in username_password:
            print("Username already exists. Try a different one.")
            continue
        break

    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    username_password[new_username] = new_password
    with open("user.txt", "w") as out_file:
        out_file.write("\n".join(f"{k};{v}" for k, v in username_password.items()))
    print("New user added successfully.")

def add_task():
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password:
        print("User does not exist.")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    curr_date = date.today()

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    save_tasks()
    print("Task successfully added.")

def view_all():
    for i, t in enumerate(task_list, 1):
        disp_str = f"""
Task {i}:
Title:\t\t {t['title']}
Assigned to:\t {t['username']}
Assigned Date:\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}
Due Date:\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}
Completed:\t {"Yes" if t['completed'] else "No"}
Description:
 {t['description']}
"""
        print(disp_str)

def view_mine(curr_user):
    user_tasks = [t for t in task_list if t['username'] == curr_user]

    if not user_tasks:
        print("No tasks assigned.")
        return

    for i, t in enumerate(user_tasks, 1):
        print(f"""
Task Number: {i}
Title: {t['title']}
Assigned Date: {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}
Due Date: {t['due_date'].strftime(DATETIME_STRING_FORMAT)}
Completed: {"Yes" if t['completed'] else "No"}
Description: {t['description']}
""")

    try:
        choice = int(input("Enter task number to select or -1 to return: "))
        if choice == -1:
            return
        if choice < 1 or choice > len(user_tasks):
            print("Invalid selection.")
            return

        selected_task = user_tasks[choice - 1]

        action = input("Choose: 'c' to mark complete, 'e' to edit: ").lower()

        if action == 'c':
            selected_task['completed'] = True
            print("Task marked as complete.")

        elif action == 'e':
            if selected_task['completed']:
                print("Cannot edit a completed task.")
                return

            new_user = input("Reassign to (or press enter to skip): ")
            if new_user:
                if new_user in username_password:
                    selected_task['username'] = new_user
                else:
                    print("User does not exist.")

            new_due = input("New due date (YYYY-MM-DD) or enter to skip: ")
            if new_due:
                try:
                    selected_task['due_date'] = datetime.strptime(new_due, DATETIME_STRING_FORMAT)
                except ValueError:
                    print("Invalid date. No change made.")

        save_tasks()

    except ValueError:
        print("Invalid input.")

def generate_reports():
    # Task overview
    total_tasks = len(task_list)
    completed_tasks = sum(1 for t in task_list if t['completed'])
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for t in task_list if not t['completed'] and t['due_date'].date() < date.today())

    task_report = f"""Task Overview
-------------------------
Total Tasks: {total_tasks}
Completed Tasks: {completed_tasks}
Incomplete Tasks: {incomplete_tasks}
Overdue Tasks: {overdue_tasks}
% Incomplete: {incomplete_tasks / total_tasks * 100:.2f}%
% Overdue: {overdue_tasks / total_tasks * 100:.2f}%
"""

    with open("task_overview.txt", "w") as f:
        f.write(task_report)

    # User overview
    total_users = len(username_password)

    user_report = "User Overview\n-------------------------\n"
    for user in username_password:
        user_tasks = [t for t in task_list if t['username'] == user]
        num_tasks = len(user_tasks)
        if num_tasks == 0:
            continue

        num_complete = sum(1 for t in user_tasks if t['completed'])
        num_incomplete = num_tasks - num_complete
        num_overdue = sum(1 for t in user_tasks if not t['completed'] and t['due_date'].date() < date.today())

        user_report += f"""
User: {user}
Total Assigned Tasks: {num_tasks}
% of Total Tasks: {num_tasks / total_tasks * 100:.2f}%
% Completed: {num_complete / num_tasks * 100:.2f}%
% Incomplete: {num_incomplete / num_tasks * 100:.2f}%
% Overdue: {num_overdue / num_tasks * 100:.2f}%
"""

    with open("user_overview.txt", "w") as f:
        f.write(user_report)

    print("Reports generated.")

def display_statistics():
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()

    with open("task_overview.txt") as f:
        print(f.read())

    with open("user_overview.txt") as f:
        print(f.read())

#========== Login ==========
logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")

    if curr_user not in username_password:
        print("User does not exist")
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
    else:
        print("Login successful!")
        logged_in = True

#========== Menu ==========
while True:
    print()
    menu = input('''Select one:
r  - Register a user
a  - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e  - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine(curr_user)

    elif menu == 'gr' and curr_user == 'admin':
        generate_reports()

    elif menu == 'ds' and curr_user == 'admin':
        display_statistics()

    elif menu == 'e':
        print("Goodbye!")
        break

    else:
        print("Invalid selection.")
