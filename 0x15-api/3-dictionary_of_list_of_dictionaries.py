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
    user_url = '{}/users'.format(url)
    filename = 'todo_all_employees.json'

    # call the api and decode the fetched data from json to dictionary
    user = json.loads(requests.get(user_url).text)

    data_dict = {}
    # iterate through each user
    for person in user:
        todo_url = '{}/todos?userId={}'.format(url, person['id'])
        # call api to fetch todo data for that user
        tasks = json.loads(requests.get(todo_url).text)
        data_list = []
        # create a list of tasks for the user
        for task in tasks:
            data = {"username": person['username'], "task": task['title'],
                    "completed": task['completed']}
            data_list.append(data)
        # add the list to a dictionary
        data_dict[person['id']] = data_list

    # export data as json file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f)


if __name__ == '__main__':
    call_api()
