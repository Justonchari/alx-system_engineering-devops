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
    td = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    us = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    r = requests.get(us)
    res = r.json()

    res_todos = requests.get(td)
    todos = res_todos.json()
    myListAll = []
    for todo in todos:
        MyList = []
        myList = [
                "{}".format(argv[1]),
                "{}".format(res.get("username")),
                "{}".format(todo.get("completed")),
                "{}".format(todo.get("title"))
                ]
        myListAll.append(myList)

    with open(f'{argv[1]}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for item in myListAll:
            csv_writer.writerow(item)
