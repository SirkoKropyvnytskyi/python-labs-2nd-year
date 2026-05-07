import json
import os

class Employee:
    def __init__(self, name, surname, position, department, salary):
        self.first_name = name
        self.last_name = surname
        self.position = position
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "position": self.position,
            "department": self.department,
            "salary": self.salary
        }

    def display_info(self):
        print(f"\nEmployee: {self.last_name} {self.first_name}")
        print(f"Position: {self.position} ({self.department})")
        print(f"Salary: {self.salary} UAH")

file_name = "employees.json"
employees_data = []

if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        try:
            employees_data = json.load(f)
        except json.JSONDecodeError:
            employees_data = []

first_name = input("Enter name: ")
last_name = input("Enter surname: ")
position = input("Enter position: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

worker = Employee(first_name, last_name, position, department, salary)
worker.display_info()

employees_data.append(worker.to_dict())

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(employees_data, f, indent=4, ensure_ascii=False)

print(f"\nRecord saved. Total in file: {len(employees_data)}")