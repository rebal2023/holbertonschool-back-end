#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""
import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)

    # User Response
    res = requests.get(user_uri).json()

    # Employee name
    name = res.get('name')

    # User TODO Response
    res = requests.get(todo_uri).json()

    # Total nb of tasks, the sum of completed and non-completed tasks
    total = len(res)

    # Nb of non-completed tasks
    non_completed = sum([elem['completed'] is False for elem in res])

    # Nb of completed tasks
    completed = total - non_completed

    # Expected output
    str = "Employee {emp_name} is done with tasks({completed}/{total}):"
    print(str.format(emp_name=name, completed=completed, total=total))

    # Printing completed tasks
    for elem in res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
