#!/usr/bin/python3
"""
using what you did in task 0,
extend your Python script to export data in the JSON format
"""
import json
import requests


def export_all_prog_to_json():
    """ like what i did in task 2, but now for every employee """
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users"
    todo_url = f"{url}/todos"

    user_data = requests.get(user_url).json()
    id_list = [usr["id"] for usr in user_data]

    user_todo_dict = {}

    for user_id in id_list:
        empl_url = f"{user_url}/{user_id}"

        empl_data = requests.get(empl_url).json()
        todo_data = requests.get(todo_url,
                                 params={"userId": user_id}).json()

        user_name = empl_data.get("username")

        user_todo_list = []
        for task in todo_data:
            task_dict = {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name
            }
            user_todo_list.append(task_dict)

        user_todo_dict.update({f"{user_id}": user_todo_list})

    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(user_todo_dict))


if __name__ == "__main__":
    export_all_prog_to_json()
