#!/usr/bin/python3
"""
Make an api request for a given employee and returns information about them
"""

import csv
import json
import requests
from sys import argv


def call_api():
    """
    A function that calls a dummy api and displayes it's data in csv format
    """
    # customize urls for each action
    url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(url, argv[1])
    todo_url = '{}/todos?userId={}'.format(url, argv[1])
    filename = '{}.csv'.format(argv[1])

    # call the api and decode the fetched data from json to dictionary
    user = json.loads(requests.get(user_url).text)
    tasks = json.loads(requests.get(todo_url).text)

    # export data to csv format
    with open(filename, 'w', encoding='utf-8') as f:
        for row in tasks:
            data = (row["userId"], user['username'],
                    row['completed'], row['title'])
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(data)


if __name__ == '__main__':
    call_api()
