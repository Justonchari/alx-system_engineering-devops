#!/usr/bin/python3
'''a Python script that, using this REST API,
   for a given employee ID, returns information
   about his/her TODO list progress
'''
if __name__ == "__main__":
    import csv
    import json
    import requests

    us = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get(us)
    res = r.json()

    to_json_dict = {}
    for user in res:
        user_id = user.get('id')
        td = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        res_todos = requests.get(td)
        todos = res_todos.json()
        myListAll = []
        for todo in todos:
            Mydict = {}
            mydict = {
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                    }
            myListAll.append(mydict)
        to_json_dict["{}".format(user_id)] = myListAll

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(to_json_dict, jsonfile)
