#!/usr/bin/python3
"""A Python script that, using this REST API, returns information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo_tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_task = [t.get("title") for t in todo_tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_task), len(todo_tasks)))
    [print("\t {}".format(c)) for c in completed_task]
