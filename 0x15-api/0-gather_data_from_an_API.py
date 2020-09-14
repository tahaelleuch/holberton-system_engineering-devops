#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/" +
                        user_id).json()

    user_name = user["name"]

    todo_list_done = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" +
        user_id + "&completed=true").json()

    number_of_task = len(requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" +
        user_id).json())

    print("Employee " + user_name + " is done with tasks({}/{}):"
          .format(len(todo_list_done), number_of_task))

    for task in todo_list_done:
        print("\t {}".format(task["title"]))
