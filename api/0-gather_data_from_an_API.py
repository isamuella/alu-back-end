#!/usr/bin/python3
"""
Request from API; return todo list of an employee using his ID
"""
import requests # type: ignore
import sys


def get_todo_lists(employee_id):
    main_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{main_url}/users/{employee_id}"
    todo_url = f"{main_url}/todos?userId={employee_id}"

    """ Fetch user data """
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: User not found")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    """ Fetch the todo list data """
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print("Error: Could not fetch tasks")
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_todo_lists(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer")
