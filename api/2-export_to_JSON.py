#!/usr/bin/python3
"""connect to and pull info from 
REST API using an employee ID
returns info about their TODO list progress"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    response = requests.get(
        f"{API_URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    user_tasks = {EMPLOYEE_ID: []}
    for task in data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        }
        user_tasks[EMPLOYEE_ID].append(task_dict)

    with open(f"{EMPLOYEE_ID}.json", "w") as file:
        json.dump(user_tasks, file)