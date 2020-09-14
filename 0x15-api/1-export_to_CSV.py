#!/usr/bin/python3
"""Get data from API and export it to csv"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/" +
                        user_id).json()

    user_name = user["username"]

    list_of_task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" +
        user_id).json()

    with open(user_id + ".csv", 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for row in list_of_task:
            writer.writerow([user_id, user_name,
                            row["completed"], row["title"]])
