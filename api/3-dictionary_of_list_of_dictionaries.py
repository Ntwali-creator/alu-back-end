#!/usr/bin/python3
"""
This script exports all employees' TODO list data to JSON format.
"""

import json
import requests


def export_all_todos_to_json():
    """
    Export all employees' todos to a single JSON file.
    
    Args:
        None
        
    Returns:
        None
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch all users
    users_response = requests.get(base_url + "/users")
    if users_response.status_code != 200:
        return
    
    users = users_response.json()
    
    # Fetch all todos
    todos_response = requests.get(base_url + "/todos")
    if todos_response.status_code != 200:
        return
    
    all_todos = todos_response.json()
    
    # Create dictionary to store all data
    data = {}
    
    # Process each user
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        
        # Filter todos for this user
        user_tasks = []
        for todo in all_todos:
            if todo.get("userId") == user_id:
                task_dict = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                }
                user_tasks.append(task_dict)
        
        data[str(user_id)] = user_tasks
    
    # Write to JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    export_all_todos_to_json()
