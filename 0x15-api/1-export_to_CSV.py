#!/usr/bin/python3
"""script that gathers data from API and exports it to CSV file.
"""
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
