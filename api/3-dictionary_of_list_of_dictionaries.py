#!/usr/bin/python3
"""
Request from API; return todo list of an employee using his ID
"""
import json
import requests


def fetch_data():
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(user_url).json()
    todo = requests.get(todo_url).json()

    data = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        user_tasks = [
            {
                 "username": username,
                 "task": task["title"],
                 "completed": task["completed"]
            }
            for task in todo if task["userId"] == user_id
        ]

        data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    fetch_data()
