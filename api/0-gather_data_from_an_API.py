#!/usr/bin/python3
"""
This script fetches and displays TODO list progress for a given employee ID.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee

    Returns:
        None
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(base_url + "/users/{}".format(employee_id))
    if user_response.status_code != 200:
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos for the user
    todos_response = requests.get(base_url + "/todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        return

    todos = todos_response.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, number_of_done_tasks, total_tasks))

    # Display completed task titles
    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
