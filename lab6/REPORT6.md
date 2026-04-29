ЛАБОРАТОРНА РОБОТА № 6 
Посилання:
https://github.com/SirkoKropyvnytskyi/python-labs-2nd-year

Тема: Робота з JSON, CSV та Excel файлами у Python 

1. Мета роботи 

    Навчитися працювати з різними форматами файлів у Python (JSON, CSV,
    Excel), здійснювати читання, запис та маніпуляцію даними, а також
    використовувати відповідні бібліотеки (json, csv, openpyxl, pandas).
    

2. Індивідуальне завдання 

    Варіант 7: Розробити програму для підрахунку середнього віку студентів і запису
    результату у JSON.

3. Код програми
```python

import json

student_data = {
    "Shadow The Hedgehog": 50,
    "Hatsune Miku": 16,
    "Haruhi Suzumiya": 17,
    "Misato Katsuragi": 29,
    "Allan Wake": 40,
    "Goblin Slayer": 25,
    "Pepino Spaghetti": 30,
    "Amelia Watson": 20,
    "Alice Lendrott": 18,
    "Johnny Cage": 29,
    "Peter Griffin": 42,
    "Saitama": 25,
    "Ultra Instinct Shaggy": 30
}

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(student_data, file, ensure_ascii=False, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

ages = list(loaded_students.values())
average_age = sum(ages) // len(ages) 

print(f"Average student age: {average_age}")

result = {
    "average_age": average_age,
    "total_students": len(ages)
}

with open("average_age_result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print("Result succesfully saved in 'average_age_result.json'.")
```

4. Висновок

1) Створюється словник student_data, де ключі - студенти, а значення — їхній вік.
2) За допомогою функції open() з параметром w (запис) та контекстного менеджера with дані зберігаються у файл students.json. Метод json.dump() перетворює словник Python на текстовий формат JSON.
3) При записі використано параметри ensure_ascii=False для коректного збереження символів кирилиці та indent=4 для створення відступів, що робить файл читабельним для людини.
4) Файл students.json відкривається в режимі r (читання). Функція json.load() зчитує вміст файлу та перетворює його назад у структуру Python (словник) для подальшої обробки.
5) Програма витягує всі значення віку за допомогою методу .values() і підраховує середній вік. Використовується оператор цілочисельного ділення // для отримання результату без дробової частини.
7) Створюється новий словник result, куди записується обчислений середній вік та загальна кількість студентів. Ці дані зберігаються у фінальний файл average_age_result.json

Я навчився працювати з різними форматами файлів, здійснювати їх читання, запис та маніпуляцію даними. Опанував структуру та особливості формату JSON. Застосування стандартного модуля json дозволило мені засвоїти основні методи роботи з файлами, зокрема функцію json.load для зчитування даних та json.dump для їхнього збереження. Окрім роботи з JSON, я ознайомився з принципами принципом роботи форматів CSV та Excel, вивчивши відповідні бібліотеки csv та pandas для автоматизації обробки табличних даних. Я навчився вносити зміни в існуючих структурах, додавання нових записів та організації даних у Python для подальшого аналізу. Було реалізовано алгоритм підрахунку середнього віку студентів із подальшою серіалізацією результату у новий файл.
