#!/usr/bin/python3
"""Employes ID"""

import requests
import sys

if __name__ == "__main__":

    empID = sys.argv[1]
    employed = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                            format(empID))

    name = employed.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(empID):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(empID) and task.get('completed')]))
