#!/usr/bin/ptyhon3
"""
this script fetches and dislays  the todo list of an employee
"""
import json
import urllib.request
import sys

def get_employee(employee_id):
    """fetch and parse the name of an employee"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

        total_tasks = len(data)
        completed_tasks = sum(task['completed'] for task in data)
        return data, total_tasks, completed_tasks
    
def get_employee_name(employee_id):
    """fetch and parse the name of an employee"""
    url = f"https://jsonplaceholder.typicode.com/user/{employee_id}"
    with urlib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

        return data['name']
    
def display_progress(employee_name, completed_tasks, total_tasks):
    """Display the todo list progress of an employee"""
    print(f"Employee {employee_name} is done with ({completed_tasks}/{total_tasks}):")
    for task in data:
        if task['completed']:
            print("\t" + task['title'])

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    task, total_tasks, completed_tasks = get_employee(employee_id)
    employee_name = get_employee_name(employee_id)
    display_progress(employee_name, completed_tasks, total_tasks)
    