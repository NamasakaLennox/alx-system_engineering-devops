#!/usr/bin/python3
"""
Make an api request for a given employee and returns information about them
"""
from sys import argv
import requests
import json

# customize urls for each action
url = 'https://jsonplaceholder.typicode.com'
user_url = '{}/users/{}'.format(url, argv[1])
todo_url = '{}/todos?userId={}'.format(url, argv[1])
complete = '{}/todos?userId={}&completed=true'.format(url, argv[1])

# call the api and decode the fetched data from json to dictionary
user = json.loads(requests.get(user_url).text)
tasks = json.loads(requests.get(todo_url).text)
task_true = json.loads(requests.get(complete).text)

# print the output based on the fetched data
print('Employee {} is done with tasks({}/{}):'.format(
    user['name'], len(task_true), len(tasks)))
# print tasks that have been completed
for item in task_true:
    print('\t {}'.format(item['title']))
