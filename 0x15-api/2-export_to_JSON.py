#!/usr/bin/python3
"""
Make an api request for a given employee and returns information about them
"""

import json
import requests
from sys import argv


def call_api():
    """
    A function that calls a dummy api and displayes it's data
    """
    # customize urls for each action
    url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(url, argv[1])
    todo_url = '{}/todos?userId={}'.format(url, argv[1])
    filename = '{}.json'.format(argv[1])

    # call the api and decode the fetched data from json to dictionary
    user = json.loads(requests.get(user_url).text)
    tasks = json.loads(requests.get(todo_url).text)

    # export file as json
    with open(filename, 'w', encoding='utf-8') as f:
        data_list = []
        for task in tasks:
            data = {"task": task['title'], "completed": task['completed'],
                    "username": user['username']}
            data_list.append(data)
        data_dict = {argv[1]: data_list}
        json.dump(data_dict, f)


if __name__ == '__main__':
    call_api()
