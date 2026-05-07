ЛАБОРАТОРНА РОБОТА № 8 
Посилання:
https://github.com/SirkoKropyvnytskyi/python-labs-2nd-year

Тема: Класи та об’єкти: основи об’єктно-орієнтованого програмування в Python. 

1. Мета роботи 

    Ознайомитися з основними поняттями об’єктно-орієнтованого 
    програмування (ООП) у мові Python; набути практичних навичок створення
    класів і об’єктів, використання конструктора класу, атрибутів та методів;
    навчитися моделювати предметну область із застосуванням класів.
    

2. Індивідуальне завдання 

    Варіант 7: Створити клас для зберігання особистих даних співробітників
    підприємства.

3. Код програми
```python

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
```

4. Висновок

1) Використовується модуль json для роботи з форматом збереження даних та модуль os для взаємодії з файловою системою, зокрема для перевірки наявності існуючої бази даних.  

2) За допомогою ключового слова class створено шаблон Employee, який описує структуру даних та поведінку об’єктів «співробітник».  

3) Конструктор \_\_init\_\_ - це спеціальний метод, який автоматично ініціалізує атрибути об’єкта (ім’я, прізвище, посаду тощо) у момент його створення. Параметр self виступає обов’язковим посиланням на поточний екземпляр класу.  

4) to_dict: реалізує базовий принцип інкапсуляції, перетворюючи внутрішні дані об’єкта у формат словника для подальшого збереження
display_info: використовує оператор крапки для доступу до атрибутів та виведення інформації на екран.  

5) Програма перевіряє наявність файлу employees.json. Якщо він існує, дані завантажуються у список; якщо ні — створюється порожній список. Це дозволяє зберігати інформацію після перезапуску програми.

6) Після введення даних користувачем викликається ім’я класу, що створює конкретний екземпляр (об’єкт).

7) Новий об’єкт додається до загального списку, який потім повністю перезаписується у файл за допомогою json.dump.

Після виконання лабораторної роботи було засвоєно ключові концепції об’єктно-орієнтованого програмування, зокрема принципи створення класів як шаблонів для об’єктів та використання конструктора \_\_init\_\_ для встановлення початкового стану атрибутів. На практиці реалізовано синтаксис оголошення класів у Python та відпрацьовано способи доступу до даних об’єкта через метод self (який є посиланням на об'єкт для якого викликається метод). В даній програмі дані та методи їх обробки об’єднані в одну логічну одиницю, що демонструє базові принципи інкапсуляції. Набуто досвіду структуризації програми за допомогою класів, що значно полегшує подальше налагодження та тестування функціоналу. Також було реалізовано механізм збереження стану об’єктів у зовнішній файл JSON, що підтверджує вміння практично застосовувати ООП для вирішення прикладних завдань.  