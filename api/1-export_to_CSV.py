#!/usr/bin/python3
"""
This script exports employee TODO list data to CSV format.
"""

import csv
import requests
import sys


def export_todos_to_csv(employee_id):
    """
    Export employee todos to CSV file.
    
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
    
    # Write to CSV file
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])
    
    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        export_todos_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
