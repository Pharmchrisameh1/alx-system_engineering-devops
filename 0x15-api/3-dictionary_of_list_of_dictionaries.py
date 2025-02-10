#!/usr/bin/python3
"""This script uses REST API for a given employee ID, returns
information about his/her TODO list progress.
"""
import json
import sys
import urllib.request


if __name__ == "__main__":
    user_data = urllib.request.urlopen(
        url='https://jsonplaceholder.typicode.com/users').read().decode(
            'utf-8')
    user_data = json.loads(user_data)
    json_dict = {}
    for user in user_data:
        user_id = user.get('id')
        user_username = user.get('username')
        user_todos = urllib.request.urlopen(
            url='https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                user_id)).read().decode('utf-8')
        user_todos = json.loads(user_todos)
        tasks_list = []
        for task in user_todos:
            task_dict = {}
            task_dict['username'] = user_username
            task_dict['task'] = task.get('title', None)
            task_dict['completed'] = task.get('completed', None)
            tasks_list.append(task_dict)
        json_dict[user_id] = tasks_list
    with open('todo_all_employees.json', 'w') as f:
        json.dump(json_dict, f)
