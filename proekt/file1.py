import json


def read_data():

    try:
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    except:
        settings = {
            "skin": "img.png",
            "money": 0
        }
    return settings
def write_data(settings):
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)