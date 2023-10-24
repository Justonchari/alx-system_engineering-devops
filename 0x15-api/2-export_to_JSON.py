#!/usr/bin/python3
'''a Python script that, using this REST API,
   for a given employee ID, returns information
   about his/her TODO list progress
'''
if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    argv = sys.argv
    user_id = argv[1]
    us = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    r = requests.get(us)
    res = r.json()

    to_json_dict = {}
    td = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    res_todos = requests.get(td)
    todos = res_todos.json()
    myListAll = []
    for todo in todos:
        Mydict = {}
        mydict = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": res.get("username")
                }
        myListAll.append(mydict)
    to_json_dict["{}".format(user_id)] = myListAll

    with open(f'{user_id}.json', 'w') as jsonfile:
        json.dump(to_json_dict, jsonfile)
