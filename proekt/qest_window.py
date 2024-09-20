from PyQt5.QtWidgets import *

from file1 import read_data, write_data


def menu_window(price, element):
    window = QDialog()
    qest_lbl = QLabel("Підтрвердіть свій вибір.")
    add_quest_btn = QPushButton("Підтвердити покупку")
    canel_quest_btn = QPushButton("Скасувати")
    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(qest_lbl)
    main_line.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(canel_quest_btn)
    h2.addWidget(add_quest_btn)
    main_line.addLayout(h2)


    def buy():
        set = read_data()
        if set["money"] >= price:
            set["money"] -= price
            set["inventori"].append(element)
        write_data(set)
        window.close()

    def close():
        window.close()

    canel_quest_btn.clicked.connect(close)
    add_quest_btn.clicked.connect(buy)
    window.setLayout(main_line)
    window.exec()