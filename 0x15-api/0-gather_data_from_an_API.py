#!/usr/bin/python3
'''
Using the JSONPlaceholder API, returns the TODO list
corresponding to a given employee ID.
USAGE:
>$ ./0-gather_data_from_an_API.py <NUMERIC_ID>
Employee [EMPLOYEE_NAME] is done with tasks(#_DONE_TASKS/TOTAL_#_TASKS):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
'''


if __name__ == '__main__':
    from requests import get
    from sys import argv

    try:
        URL = "https://jsonplaceholder.typicode.com"
        ID = argv[1]
        employee = get(URL + "/users/" + ID).json()
        name = employee.get('name')
        all_tasks = get(URL + "/todos?userId=" + ID).json()
        done_tasks = [task.get('title')
                      for task in all_tasks if task.get('completed')]
        print("Employee {} is done with tasks({}/{}):"
              .format(name, len(done_tasks), len(all_tasks)))
        print("\t", "\n\t ".join(done_tasks))
    except IndexError:
        print("USAGE: ./0-gather_data_from_an_API.py <NUMERIC_ID>")
