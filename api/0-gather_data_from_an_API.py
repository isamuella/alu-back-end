#!/usr/bin/python3
import requests
import sys
my name
def get_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    
    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: User not found")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Could not fetch tasks")
        return
    
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
