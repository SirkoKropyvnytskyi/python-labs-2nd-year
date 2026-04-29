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

