# API Project

This project contains Python scripts that interact with a REST API to fetch and export employee TODO list data.

## Tasks

### Task 0: Gather data from an API
- **File:** `0-gather_data_from_an_API.py`
- **Description:** Fetches and displays TODO list progress for a given employee ID
- **Usage:** `python3 0-gather_data_from_an_API.py <employee_id>`

### Task 1: Export to CSV
- **File:** `1-export_to_CSV.py`
- **Description:** Exports employee TODO list data to CSV format
- **Usage:** `python3 1-export_to_CSV.py <employee_id>`
- **Output:** `USER_ID.csv`

### Task 2: Export to JSON
- **File:** `2-export_to_JSON.py`
- **Description:** Exports employee TODO list data to JSON format
- **Usage:** `python3 2-export_to_JSON.py <employee_id>`
- **Output:** `USER_ID.json`

### Task 3: Dictionary of list of dictionaries
- **File:** `3-dictionary_of_list_of_dictionaries.py`
- **Description:** Exports all employees' TODO list data to a single JSON file
- **Usage:** `python3 3-dictionary_of_list_of_dictionaries.py`
- **Output:** `todo_all_employees.json`

## Requirements

- Python 3.4.3
- requests module
- PEP 8 style compliance

## API Endpoints Used

- `https://jsonplaceholder.typicode.com/users`
- `https://jsonplaceholder.typicode.com/todos`

## Author

Ntwali-creator

## Project from ALU Back-End Curriculum
