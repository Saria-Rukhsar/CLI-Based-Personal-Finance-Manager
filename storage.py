import json

with open("data.json", "w") as f:
    f.write("")

def load_data():
    with open("data.json", "r") as f:
        loaded = json.load(f)
    return loaded

def save_Data(transactions):
    data_list = load_data()
    data_list.append(transactions)
    with open("data.json", "w") as f:
        json.dump(data_list, f, indent=4)

def save_updated_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
