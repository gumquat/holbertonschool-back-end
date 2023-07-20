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


def get_employee_todo_progress(employee_id):

    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    response = requests.get(url)
    response.raise_for_status()
    todo_list = response.json()

    name = ""
    total_tasks = len(todo_list)
    done_tasks = 0
    completed_task_titles = []

    for task in todo_list:
        if task['completed']:
            done_tasks += 1
            completed_task_titles.append(task['title'])
        if 'username' in task:
            name = task['username']

    print("Employee {} is done\
           with tasks({}/{}):".format(name, done_tasks, total_tasks))
    print(f"{name}: {done_tasks} tasks")

    if done_tasks > 0:
        print("Completed tasks:")
        for title in completed_task_titles:
            print(f"\t{title}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
