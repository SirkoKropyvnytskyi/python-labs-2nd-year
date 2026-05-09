ЛАБОРАТОРНА РОБОТА № 9 
Посилання:
https://github.com/SirkoKropyvnytskyi/python-labs-2nd-year

Тема: Використання регулярних виразів для пошуку та заміни в рядках 

1. Мета роботи 

    Ознайомитися з основами регулярних виразів у мові програмування
    Python, вивчити їх синтаксис та навчитися застосовувати регулярні вирази для
    пошуку, перевірки та заміни фрагментів тексту з використанням модуля re.
    

2. Індивідуальне завдання 

    Варіант 7: Написати програму для пошуку всіх email-адрес у тексті.

3. Код програми
```python

import re

Slayer_Testament_text = "In the first age, in the first battle, doomslayer@gmail.com when the shadows first lengthened, one stood. Burned by the embers of Armageddon, his soul blistered by the fires of Hell and iconofsin@ukr.net tainted beyond ascension, he chose the path of perpetual torment. In his ravenous hatred he found no peace; and with boiling blood he scoured the Umbral Plains samuelhayden@yahoo.com seeking vengeance against the dark lords who had wronged him. He wore the crown of the Night Sentinels, and those that tasted the bite of his sword named him... the Doom Slayer."

email_found = re.findall(r'[\w\.-]+@[\w\.-]+', Slayer_Testament_text)

print("Found emails:")
for email in email_found:
    print(email)

try:
    with open("emails.txt", "w", encoding="utf-8") as file:
        for email in email_found:
            file.write(email + "\n")
    print("\nResults successfully saved to file 'emails.txt'.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
```

4. Висновок

1) Підключаємо стандартну бібліотеку re, яка необхідна для роботи з регулярними виразами в Python.  

2) Створюємо змінну Slayer_Testament_text, що містить текст, у якому потрібно знайти електронні адреси.  

3) Використовуємо функцію re.findall(), шукаємо усі входження шаблону у рядку, повертаємо
список адрес. Ми застосовуємо регулярний вираз r'[\w\.-]+@[\w\.-]+', де:

    \w — шукає букви, цифри або підкреслення.

    \\. та - — дозволяють включати у назву пошти крапки та дефіси.
    
    \+ — квантифікатор, що вказує на наявність одного або більше таких символів. 

4) За допомогою циклу for ми перебираємо список знайдених адрес, зберігаючи кожну у змінну email, та виводимо їх у консоль з нового рядка  

5) Використовуємо конструкцію with open(), щоб створити файл emails.txt. За допомогою методу .write() записуємо кожен знайдений імейл у файл, додаючи символ переносу рядка \n для коректного форматування.

Опанував призначення регулярних виразів як спеціальних шаблонів для пошуку, перевірки та заміни даних, а також їхній синтаксис і структуру. Навчився створювати регулярні вирази для роз'язання прикладних задач, аналізу та обробки текстових даних створюючи ефективні шаблонни для автоматищації рутинних завдань. Це продемонстровано на прикладі моєї реалізації програми для пошуку email адрес в тексті, які самостійно людині найти б в тексті ці адреси зайняло б набагато більше часу.