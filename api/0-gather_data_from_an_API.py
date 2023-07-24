#!/usr/bin/python3
"""Gets infro about user from an API"""
import requests


def display_employee_progress(employee_id):
    """ script must display to stdout the employee todo list progress """
    url = "https://jsonplaceholder.typicode.com"
    empl_url = f"{url}/users/{employee_id}"
    todo_url = f"{url}/todos"

    empl_data = requests.get(empl_url).json()
    todo_data = requests.get(todo_url,
                             params={"userId": employee_id}).json()

    empl_name = empl_data.get("name")
    completed_tasks = [t["title"] for t in todo_data if t["completed"]]
    num_done = len(completed_tasks)
    num_total = len(todo_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(empl_name, num_done, num_total))
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    import sys

    display_employee_progress(int(sys.argv[1]))
