#!/usr/bin/python3

import sys
import requests

def fetch_employee_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    endpoint = f"/users/{employee_id}"
    url = base_url + endpoint

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_todo_progress(employee_data):
    if not employee_data:
        print("Employee not found.")
        return

    employee_name = employee_data['name']
    todos = fetch_employee_todo_list(employee_data['id'])

    if not todos:
        print("TODO list not found for the employee.")
        return

    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])
    task_titles = [todo['title'] for todo in todos if todo['completed']]

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for title in task_titles:
        print("\t", title)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data = fetch_employee_todo_list(employee_id)
    display_todo_progress(employee_data)
