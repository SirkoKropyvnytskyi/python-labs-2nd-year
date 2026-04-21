import os

file_name = 'data.txt'
line_to_add = "cool new line that is very (not) important and definitely not the screams of the damned"

if not os.path.exists(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("test file text.\n")

with open(file_name, 'a', encoding='utf-8') as f:
    f.write(f"added line: {line_to_add}\n")

print(f"New line added. Please check file {file_name}")