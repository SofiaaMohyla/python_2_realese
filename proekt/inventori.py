from PyQt5.QtWidgets import *

from file1 import read_data


def window():

    window = QDialog()
    window.resize(800, 800)

    img_lbl1 = QListWidget()

    mine_line = QVBoxLayout()

    h1 = QHBoxLayout()
    h1.addWidget(img_lbl1)
    mine_line.addLayout(h1)
    set = read_data()
    img_lbl1.addItems(set["inventori"])


    window.setLayout(mine_line)
    window.show()
    window.exec()