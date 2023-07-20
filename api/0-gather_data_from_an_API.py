#!/usr/bin/python3
import json
import requests
import urllib.request
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
    try:
        with urllib.request.urlopen(url) as response:
            response = requests.get(url)
            todos = response.json()
    except urllib.error.URLError as x:
        print("Error fetching data:", x)
        exit(1)
    """stored as dict so make sure to grab data that way"""
    try:
        data_list = json.loads(todos)
    except json.JSONDecodeError as x:
        print("Error parsing JSON data:", x)
        exit(1)

    """get relavent data from dict object"""
    for item in data_list:
        employee_name = item.get('name',)
        total_tasks = len(todos)
        """count len of tasks with 'completed - LOOP'"""
        for _ in todos:
            if _['completed']:
                completed_tasks += 1
                completed_task_titles.append(_['title'])
        completed_task_titles = []

    """PRINT selected employee TODO list progress"""
    print(f"Employee {employee_name} is done with tasks ({(completed_tasks)}/{total_tasks}):")

    """PRINT completed task titles"""
    for _ in completed_tasks:
        print(f"\t{_[completed_task_titles]}")


"""DO NOT REMOVE BELOW CODE - NECCESSARY TO RUN"""
if __name__ == "__main__":
    """hope to GOD the script is called with the employee ID as a command-line argument"""
    import sys
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
