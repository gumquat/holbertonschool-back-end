#!/usr/bin/python3
import requests
"""
This Python script fetches and displays an employee's TODO list 
progress for a given employee ID using the 
[jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/) API. 
It provides information about completed tasks and their titles
in a specified format.
"""

def get_employee_todo_progress(employee_id):
    """grab the TODO list data for the recieved employee ID"""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    todos = response.json()

    """filter completed tasks and count the number of tasks"""
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]

    """pull employee name from the first TODO record"""
    employee_name = todos[0]['userId']
    # Assuming that the first name record of the user is the employee name
    url_user = f'https://jsonplaceholder.typicode.com/users/{employee_name}'
    response_user = requests.get(url_user)
    user_info = response_user.json()
    employee_name = user_info['name']

    """Display the employee TODO list progress"""
    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

    """Display the titles of completed tasks"""
    for task in completed_tasks:
        print(f"\t{task['title']}")


"""DO NOT REMOVE BELOW CODE - NECCESSARY TO RUN"""
if __name__ == "__main__":
    """hope to GOD the script is called with the employee ID as a command-line argument"""
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
