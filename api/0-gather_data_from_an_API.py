#!/usr/bin/python3
"""
This module fetches and displays TODO list progress for a given employee ID.
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
        print(f"Error: Employee with ID {employee_id} not found")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Fetch TODO list for the user
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list")
        return
    
    todos_data = todos_response.json()
    
    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_done = len(completed_tasks)
    
    # Print the employee progress
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")
    
    # Print each completed task title with tab and space
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
