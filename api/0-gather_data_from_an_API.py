#!/usr/bin/python3
"""
This Python script fetches and displays an employee's TODO list
progress for a given employee ID using the
[jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/) API.
It provides information about completed tasks and their titles
in a specified format.
"""
import json
import requests
import urllib.request


import requests

def get_employee_todo_progress(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        todo_list = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        exit(1)
    except requests.exceptions.JSONDecodeError as e:
        print("Error parsing JSON data:", e)
        exit(1)

    employee_name = ""
    total_tasks = len(todo_list)
    done_tasks = 0
    completed_task_titles = []

    for task in todo_list:
        if task['completed']:
            done_tasks += 1
            completed_task_titles.append(task['title'])
        if 'username' in task:
            employee_name = task['username']

    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    print(f"{employee_name}: {done_tasks} tasks")

    if done_tasks >= 0:
        print("Completed tasks:")
        for title in completed_task_titles:
            print(f"\t{title}")

if __name__ == "__main__":
    import sys
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
