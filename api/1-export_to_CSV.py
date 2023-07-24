#!/usr/bin/python3
"""Export data in CSV"""
import csv
import requests
from sys import argv


def get_api():
    """Get data from the API"""
    if len(argv) != 2:
        print("Usage: python script_name.py user_id")
        return

    url = 'https://jsonplaceholder.typicode.com/'
    uid = argv[1]

    try:
        usr_response = requests.get(url + 'users/{}'.format(uid))
        usr_response.raise_for_status()
        usr = usr_response.json()

        todo_response = requests.get(url + 'todos', params={'userId': uid})
        todo_response.raise_for_status()
        todo = todo_response.json()

        with open('{}.csv'.format(uid), 'w') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for employee in todo:
                user_id = uid
                username = usr.get('username')
                task_comp = employee.get('completed')
                task_title = employee.get('title')

                emp_record = [user_id, username, task_comp, task_title]
                writer.writerow(emp_record)

        print("Number of tasks in CSV: OK")

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data from the API. {e}")

if __name__ == '__main__':
    get_api()
