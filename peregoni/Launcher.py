import json


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from magazine import start_magaz
from main import start_game

app = QApplication([])
window = QWidget()
window.setWindowTitle("Супер лаунчер")
window.resize(300, 300)
window.show()


settings = {}
#def read_data():
#    global settings
#    try:
#        with open("settings.json", "r", encoding="utf-8") as file:
#            settings = json.load(file)
#    except:
#        settings ={
#                "skin": "optimys_prime/img.png",
#                "money": 100
#            }
#def write_data():
#    global settings
#    with open("settings.json", "w", encoding="utf-8") as file:
#        json.dump(settings, file, indent=4, ensure_ascii=False)
#
#def buy_skin_1():
#    read_data()
#    if settings["money"] >=7:
#        settings["money"] -= 7
#        settings["skin"] = "optimys_prime/автомобіль2.png"
#        write_data()
#    else:
#        print("Грочей не хватає")





knopka1 = QPushButton("Грати")
buy_skin = QPushButton("Купити скін")
leave = QPushButton("Вийти з гри")

h1 = QVBoxLayout()
h1.addWidget(knopka1)
h1.addWidget(buy_skin)
h1.addWidget(leave)


window.setLayout(h1)
knopka1.clicked.connect(start_game)
buy_skin.clicked.connect(start_magaz)
leave.clicked.connect(quit)

app.setStyleSheet("""
    QWidget
    {
        background-color: #3a784e;
        border-radius: 4px;
    }


    QPushButton
    {
        min-height: 25px;
        border-style: double;
        border-width: 2px;
        border-color: bleck;
        background-color: #d9d9d9;
        font-size:16px;
    }
    QTextEdit
    {
        background-color: #d9d9d9;
        border-radius: 4px;
    }

    QListWidget
    {
        background-color: #d9d9d9;
        border-radius: 4px;
    }

    QLineEdit
    {
        background-color: #d9d9d9;
        border-radius: 4px;
        border-width: 7px;
        min-height: 20px;
    }



""")




window.show()

app.exec()
