#!/usr/bin/python3
"""This script uses REST API for a given employee ID, returns
information about his/her TODO list progress.
"""
import json
import sys
import urllib.request


if __name__ == "__main__":
    if (len(sys.argv) == 2):
        user_data = urllib.request.urlopen(
            url='https://jsonplaceholder.typicode.com/users?id={}'.format(
                sys.argv[1])).read().decode('utf-8')
        user_data = json.loads(user_data)
        user_name = user_data[0].get('name', None)
        todo_all = urllib.request.urlopen(
            url='https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                sys.argv[1])).read().decode('utf-8')
        todo_all = json.loads(todo_all)
        completed = 0
        tasks = ""
        for task in todo_all:
            if (task.get('completed') is True):
                completed += 1
                tasks += '\t '
                tasks += task.get('title', None)
                tasks += "\n"
        print("Employee {} is done with tasks({}/{}):".format(
            user_name, completed, len(todo_all)
        ))
        print(tasks, end="")
