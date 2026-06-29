#!/usr/bin/python3
"""
This script exports employee TODO list data to JSON format.
"""

import json
import requests
import sys


def export_todos_to_json(employee_id):
    """
    Export employee todos to JSON file.
    
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
        print("Employee not found")
        return
    
    user_data = user_response.json()
    username = user_data.get("username")
    
    # Fetch todos for the user
    todos_response = requests.get(base_url + "/todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Could not fetch todos")
        return
    
    todos = todos_response.json()
    
    # Prepare data structure
    tasks_list = []
    for todo in todos:
        task_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)
    
    data = {str(employee_id): tasks_list}
    
    # Write to JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        export_todos_to_json(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
