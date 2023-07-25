#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetches employee data and TODO list from the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing employee data (dict)
        and a list of TODOs (list).
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        response_employee = requests.get(employee_url)
        response_todo = requests.get(todo_url)
        response_employee.raise_for_status()
        response_todo.raise_for_status()

        employee_data = response_employee.json()
        todos = response_todo.json()

        return employee_data, todos

    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        sys.exit(1)


def export_to_json(employee_data, todos):
    """
    Exports employee's TODO list to a JSON file.

    Args:
        employee_data (dict): Data of the employee.
        todos (list): List of TODOs.
    """
    user_id = employee_data['id']
    file_name = f"{user_id}.json"
    data_to_export = ({str(user_id): [
            {"task": todo['title'], "completed": todo['completed'],
             "username": employee_data['username']}
            for todo in todos]})

    with open(file_name, 'w') as json_file:
        json.dump(data_to_export, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todos = fetch_employee_todo_list(employee_id)
    export_to_json(employee_data, todos)
