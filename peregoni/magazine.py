import json


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


def start_magaz():
    window = QDialog()
    window.setWindowTitle("Магазин")
    window.resize(400, 400)
    window.show()


    knopka1 = QPushButton("Вийти в головне меню")
    kartinka_px = QPixmap("optimys_prime/бус-removebg-preview.png")
    kartinka = QLabel("optimys_prime/бус-removebg-preview.png")
    kartinka2_px = QPixmap("optimys_prime/автомобіль3.png")
    kartinka2_px=kartinka2_px.scaledToWidth(125)
    kartinka2 = QLabel("optimys_prime/автомобіль3.png")
    kartinka3_px = QPixmap("optimys_prime/автомобіль4.png")
    kartinka3_px = kartinka3_px.scaledToWidth(135)
    kartinka3 = QLabel("optimys_prime/автомобіль4.png")

    kartinka4_px = QPixmap("optimys_prime/автомобіль5.png")
    kartinka4_px = kartinka4_px.scaledToWidth(135)
    kartinka4 = QLabel("optimys_prime/автомобіль5.png")
    rohunok = QLabel("гроші")

    buy_skin_1_btn = QPushButton("Купити скін👆")
    buy_skin_2_btn = QPushButton("Купити скін👆")
    buy_skin_3_btn = QPushButton("Купити скін👆")
    buy_skin_4_btn = QPushButton("Купити скін👆")

    buy_skin_1_money = QLabel("5")
    buy_skin_2_money = QLabel("20")
    buy_skin_3_money = QLabel("10")
    buy_skin_4_money = QLabel("15")
    h1 = QVBoxLayout()
    h2 = QHBoxLayout()
    h3 = QHBoxLayout()
    h4 = QHBoxLayout()

    h1.addWidget(knopka1)
    h1.addWidget(rohunok)
    h2.addWidget(kartinka)
    h2.addWidget(kartinka2)
    h2.addWidget(kartinka3)
    h2.addWidget(kartinka4)
    h1.addLayout(h2)
    h1.addLayout(h3)
    h1.addLayout(h4)
    h3.addWidget(buy_skin_1_btn)
    h3.addWidget(buy_skin_2_btn)
    h3.addWidget(buy_skin_3_btn)
    h3.addWidget(buy_skin_4_btn)

    h4.addWidget(buy_skin_1_money)
    h4.addWidget(buy_skin_2_money)
    h4.addWidget(buy_skin_3_money)
    h4.addWidget(buy_skin_4_money)

    window.setLayout(h1)

    settings = {}




    def read_data():
        global settings
        try:
            with open("settings.json", "r", encoding="utf-8") as file:
                settings = json.load(file)
        except:
            settings = {
                "skin": "optimys_prime/img.png",
                "money": 100
            }

    def write_data():
        global settings
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4, ensure_ascii=False)

    def grohi():
        global settings
        read_data()
        rohunok.setText("Монет на рахунку:  "+str(settings["money"]))
    grohi()

    def buy_skin_1():
        global settings
        read_data()
        if settings["money"] >= 5:
            settings["money"] -= 5
            settings["skin"] = "optimys_prime/бус-removebg-preview.png"
            write_data()
        else:
            print("Грочей не хватає")
        grohi()


    def buy_skin_2():
        global settings
        read_data()
        if settings["money"] >= 20:
            settings["money"] -= 20
            settings["skin"] = "optimys_prime/автомобіль3.png"
            write_data()
        else:
            print("Грочей не хватає")
        grohi()

    def buy_skin_3():
        global settings
        read_data()
        if settings["money"] >= 10:
            settings["money"] -= 10
            settings["skin"] = "optimys_prime/автомобіль4.png"
            write_data()
        else:
            print("Грочей не хватає")
        grohi()

    def buy_skin_4():
        global settings
        read_data()
        if settings["money"] >= 15:
            settings["money"] -= 15
            settings["skin"] = "optimys_prime/автомобіль5.png"
            write_data()
        else:
            print("Грочей не хватає")
        grohi()


    kartinka.setPixmap(kartinka_px)
    kartinka2.setPixmap(kartinka2_px)
    kartinka3.setPixmap(kartinka3_px)
    kartinka4.setPixmap(kartinka4_px)
    window.show()
    buy_skin_1_btn.clicked.connect(buy_skin_1)
    buy_skin_2_btn.clicked.connect(buy_skin_2)
    buy_skin_3_btn.clicked.connect(buy_skin_3)
    buy_skin_4_btn.clicked.connect(buy_skin_4)
    knopka1.clicked.connect(window.close)
    window.exec()