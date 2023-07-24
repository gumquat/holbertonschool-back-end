#!/usr/bin/python3
"""
using what still doesn't work in task 0...
extend your Python script to export data in the JSON format
"""
import json
import requests


def export_empl_prog_to_json(user_id):
    """ like what i did in 1 but with JSON """
    url = "https://jsonplaceholder.typicode.com"
    empl_url = f"{url}/users/{user_id}"
    todo_url = f"{url}/todos"

    empl_data = requests.get(empl_url).json()
    todo_data = requests.get(todo_url,
                             params={"userId": user_id}).json()

    empl_name = empl_data.get("name")
    user_name = empl_data.get("username")
    completed_tasks = [t["title"] for t in todo_data if t["completed"]]
    num_done = len(completed_tasks)
    num_total = len(todo_data)

    user_todo_list = []
    for task in todo_data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user_name
        }
        user_todo_list.append(task_dict)

    user_todo_dict = {f"{user_id}": user_todo_list}

    with open(f"{user_id}.json", "w") as f:
        f.write(json.dumps(user_todo_dict))

    print("Employee {} is done with tasks({}/{}):"
          .format(empl_name, num_done, num_total))
    for todo in completed_tasks:
        print(f"\t {todo}")

if __name__ == "__main__":
    import sys

    export_empl_prog_to_json(int(sys.argv[1]))
