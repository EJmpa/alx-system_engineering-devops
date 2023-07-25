#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
and exporting data in JSON format
"""

import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = [
            {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            } for task in tasks
        ]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
