import os


with open("test.json", 'r') as file:
    content = file.read().strip()
    print(content[-1])
    content = content[:-1]
    with open("test.json", 'w') as file:
        file.write(content)
    with open("test.json", 'a') as file:
        file.write('\n]')