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
        user_username = user_data[0].get('username', None)
        todo_all = urllib.request.urlopen(
            url='https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                sys.argv[1])).read().decode('utf-8')
        todo_all = json.loads(todo_all)
        with open("./{}.csv".format(sys.argv[1]), "w") as f:
            for task in todo_all:
                task_title = task.get('title', None)
                task_complete = task.get('completed', None)
                string = '"{}","{}","{}","{}"\n'.format(
                    sys.argv[1], user_username, task_complete, task_title
                )
                f.write(string)
