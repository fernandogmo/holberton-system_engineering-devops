#!/usr/bin/python3
'''
Using the JSONPlaceholder API, export to CSV all tasks
corresponding to a given employee ID.
Example usage:
>$ ./2-export_to_JSON.py 2
>$ bat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem
incidunt", "completed": false, "username": "Antonette"}, {"task":
"distinctio vitae autem nihil ut molestias quo", "completed":
true, "username": "Antonette"}, {"task": "et itaque necessitatibus
maxime molestiae qui quas velit", "completed": false, "username":
"Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat
    ...
{"task": "doloremque quibusdam asperiores libero corrupti illum
qui omnis", "completed": false, "username": "Antonette"}, {"task":
"totam atque quo nesciunt", "completed": true, "username": "Antonette"}]}
'''


if __name__ == '__main__':
    import json
    from requests import get
    from sys import argv

    try:
        URL = "https://jsonplaceholder.typicode.com"
        ID = argv[1]
        employee = get(URL + "/users/" + ID).json()
        name = employee.get('name')
        all_tasks = get(URL + "/todos?userId=" + ID).json()

        with open(ID + ".json", 'w') as f:
            tasks = [{"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": name} for task in all_tasks]
            json.dump({ID: tasks}, f)
    except IndexError:
        print("USAGE: ./2-export_to_JSON.py <NUMERIC_ID>")
