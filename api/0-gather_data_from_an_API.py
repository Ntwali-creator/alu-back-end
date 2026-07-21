#!/usr/bin/python3
"""
This module fetches and displays TODO list progress for a given employee ID
using the JSONPlaceholder REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays TODO list progress for a specific employee.

    Args:
        employee_id (int): The ID of the employee

    Returns:
        None: Prints the employee's TODO list progress to stdout
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list for the user
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        return

    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_done = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_done, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        sys.exit(1)
