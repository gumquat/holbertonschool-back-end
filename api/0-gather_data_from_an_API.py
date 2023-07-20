#!/usr/bin/python3
"""
This Python script fetches and displays an employee's TODO list
progress for a given employee ID using the
[jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/) API.
It provides information about completed tasks and their titles
in a specified format.
"""
import requests


API_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"

def get_employee_info(employee_id):
    """Get employee information from the API"""
    employee_response = requests.get(f"{API_URL}/{employee_id}")
    employee_data = employee_response.json()

    """Get TODO list for the employee"""
    todos_response = requests.get(TODOS_URL, params={"userId": employee_id})
    todos_data = todos_response.json()

    """Extract completed tasks and count"""
    completed_tasks = [todo["title"] for todo in todos_data if todo["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    return employee_data["name"], num_completed_tasks, total_tasks, completed_tasks

def display_employee_progress(employee_name, num_completed_tasks, total_tasks, completed_tasks):
    print(
        f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print("\t", task)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    try:
        name, completed, total, tasks = get_employee_info(employee_id)
        display_employee_progress(name, completed, total, tasks)
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch data from the API.")
