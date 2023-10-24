#!/usr/bin/python3
'''a Python script that, using this REST API,
   for a given employee ID, returns information
   about his/her TODO list progress
'''
if __name__ == "__main__":
    import json
    import requests
    import sys
    argv = sys.argv
    td = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    us = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    r = requests.get(us)
    res = r.json()

    res_todos = requests.get(td)
    todos = res_todos.json()
    titles = []
    for todo in todos:
        if todo.get('completed'):
            titles.append(todo.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(res.get('name'), len(titles), len(todos)))
    for title in titles:
        print('\t {}'.format(title))
