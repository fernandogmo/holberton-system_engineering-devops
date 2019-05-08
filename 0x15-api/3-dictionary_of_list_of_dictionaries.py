#!/usr/bin/python3
'''
Using the JSONPlaceholder API, export to CSV all tasks
corresponding to a given employee ID.
Example usage:
>$ ./3-dictionary_of_list_of_dictionaries.py 2
>$ bat todo_all_employees.json
{"1": [{"task": "suscipit repellat esse quibusdam voluptatem
incidunt", "completed": false, "username": "Chad"}, {"task":
"distinctio vitae autem nihil ut molestias quo", "completed":
true, "username": "Chad"}, {"task": "et itaque necessitatibus
maxime molestiae qui quas velit", "completed": false, "username":
"Chad"}, {"task": "adipisci non ad dicta qui amet quaerat
    ...
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem
incidunt", "completed": false, "username": "Antonette"}, {"task":
"distinctio vitae autem nihil ut molestias quo", "completed":
true, "username": "Antonette"}, {"task": "et itaque necessitatibus
maxime molestiae qui quas velit", "completed": false, "username":
"Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat
    ...
{"task": "doloremque quibusdam asperiores libero corrupti illum
qui omnis", "completed": false, "username": "Ziggy"}, {"task":
"totam atque quo nesciunt", "completed": true, "username": "Ziggy"}]}
'''


if __name__ == '__main__':
    import json
    from requests import get

    try:
        URL = "https://jsonplaceholder.typicode.com"
        employees = get(URL + "/users/").json()

        user_tasks = {}
        for user in employees:
            uid = str(user.get('id'))
            tasks = get(URL + "/todos?userId=" + uid).json()
            user_tasks[uid] = [{"username": user.get('username'),
                                "task": task.get('title'),
                                "completed": task.get('completed')}
                               for task in tasks]
        with open("todo_all_employees.json", 'w') as f:
            json.dump(user_tasks, f)
    except Exception as err:
        print("USAGE: ./3-dictionary_of_list_of_dictionaries.py")
        raise err
