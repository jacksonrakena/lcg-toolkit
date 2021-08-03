import json

def open_templates():
    with open('templates.json', 'r') as file:
        return json.loads(file.read())