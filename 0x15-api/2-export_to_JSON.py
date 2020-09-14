#!/usr/bin/python3
"""Get data from API and export it to json"""

import requests
from sys import argv
import json

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/" +
                        user_id).json()

    user_name = user["username"]

    list_of_task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" +
        user_id).json()

    new_list_task = []
    for task in list_of_task:
        new_dict = {}
        new_dict["task"] = task["title"]
        new_dict["completed"] = task["completed"]
        new_dict["username"] = user_name
        new_list_task.append(new_dict)

    user_dict = {}
    user_dict[user_id] = new_list_task

    with open(user_id + ".json", 'w') as f:
        json.dump(user_dict, f)
