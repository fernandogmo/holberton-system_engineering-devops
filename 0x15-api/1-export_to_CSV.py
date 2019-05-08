#!/usr/bin/python3
'''
Using the JSONPlaceholder API, export to CSV all tasks
corresponding to a given employee ID.
USAGE:
>$ ./1-export_to_CSV.py <NUMERIC_ID>
>$ bat <NUMERIC_ID>.csv
"NUMERIC_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"NUMERIC_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"NUMERIC_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    ...
"NUMERIC_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"NUMERIC_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"NUMERIC_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
'''


if __name__ == '__main__':
    import csv
    from requests import get
    from sys import argv

    try:
        URL = "https://jsonplaceholder.typicode.com"
        ID = argv[1]
        employee = get(URL + "/users/" + ID).json()
        name = employee.get('username')
        all_tasks = get(URL + "/todos?userId=" + ID).json()

        with open(ID + ".csv", 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in all_tasks:
                writer.writerow([ID, name,
                                 task.get('completed'), task.get('title')])
    except IndexError:
        print("USAGE: ./1-export_to_CSV.py <NUMERIC_ID>")
