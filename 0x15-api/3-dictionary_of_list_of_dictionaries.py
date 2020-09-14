#!/usr/bin/python3
"""Get data from API and export it to json"""

import requests
import json

if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()

    user_dict = {}
    for user in users:
        user_id = str(user["id"])

        list_of_task = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId=" +
            user_id).json()

        new_list_task = []
        for task in list_of_task:
            new_dict = {}
            new_dict["username"] = user["username"]
            new_dict["task"] = task["title"]
            new_dict["completed"] = task["completed"]
            new_list_task.append(new_dict)

        user_dict[user_id] = new_list_task

    with open("todo_all_employees.json", 'w') as f:
        json.dump(user_dict, f)
