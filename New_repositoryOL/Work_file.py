def read_data():
    global notes
    with open("database.json", "r", encoding="utf-8") as file:
        notes = json.load(file)



def write_data():
    global notes
    with open("database.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)