import json
# added for pull request
json_file_path = 'data/library.json'


def load_entries():
    with open(json_file_path, 'r') as file:
        return json.load(file)


def save_entries(entries):
    with open(json_file_path, 'w') as file:
        json.dump(entries, file, indent=4)
