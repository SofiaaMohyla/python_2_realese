import json
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import game
import qest_window
from file1 import read_data


def shop():




    window = QDialog()
    window.setStyleSheet("""
           QWidget
           {
           background-color: #0000ff;
           }


           QLabel
           {
               background-color: #e0f542;
               font-size: 18px;
               color: blue;
               border-style: double;
               border-width: 5px;
               border-color: orange;
               border-radius: 12px;
           }


           QPushButton 
           {  
               background-color: #e0f542;
               font-size: 18px;
               color: blue;
               border-style: double;
               border-width: 5px;
               border-color: orange;
               border-radius: 12px;
               min-height: 20px;
               min-width: 100;
               margin: 5px;
           }


       """)

    window.resize(500,600)

    pixmax1 = QPixmap("kartunka/photo_1_m.jpg")
    pixmax2 = QPixmap("kartunka/photo_2_m.jpg")
    pixmax3 = QPixmap("kartunka/photo_3_m.jpg")
    pixmax4 = QPixmap("kartunka/photo_4_m.jpg")
    pixmax5 = QPixmap("kartunka/photo_5_m.jpg")
    pixmax6 = QPixmap("kartunka/photo_6_m.jpg")
    pixmax7 = QPixmap("kartunka/photo_7_m.jpg")
    pixmax8 = QPixmap("kartunka/photo_8_m.jpg")
    pixmax9 = QPixmap("kartunka/photo_9_m.jpg")
    pixmax10 = QPixmap("kartunka/photo_10_m.jpg")
    pixmax11 = QPixmap("kartunka/photo_11_m.jpg")
    pixmax12 = QPixmap("kartunka/photo_12_m.jpg")
    pixmax13 = QPixmap("kartunka/photo_13_m.jpg")


    img_lbl1 = QLabel()
    img_lbl2 = QLabel()
    img_lbl3 = QLabel()
    img_lbl4 = QLabel()
    img_lbl5 = QLabel()
    img_lbl6 = QLabel()
    img_lbl7 = QLabel()
    img_lbl8 = QLabel()
    img_lbl9 = QLabel()
    img_lbl10 = QLabel()
    img_lbl11 = QLabel()
    img_lbl12 = QLabel()
    img_lbl13 = QLabel()

    answer_lbl_1 = QLabel("15 L")
    answer_lbl_2 = QLabel("25 L")
    answer_lbl_3 = QLabel("25 L")
    answer_lbl_4 = QLabel("30 L")
    answer_lbl_5 = QLabel("50 L")
    answer_lbl_6 = QLabel("100 L")
    answer_lbl_7 = QLabel("150 L")
    answer_lbl_8 = QLabel("180 L")
    answer_lbl_9 = QLabel("220 L")
    answer_lbl_10 = QLabel("250 L")
    answer_lbl_11 = QLabel("250 L")
    answer_lbl_12 = QLabel("300 L")
    answer_lbl_13 = QLabel("1L = 1,5 грн.")
    answer_lbl_14 = QLabel("Logika ")
    settings = read_data()
    answer_lbl_15 = QLabel(str(settings["money"]))
    answer_lbl_16 = QLabel("Логіків")


    qest_btn1 = QPushButton("Купити")
    qest_btn2 = QPushButton("Купити")
    qest_btn3 = QPushButton("Купити")
    qest_btn4 = QPushButton("Купити")
    qest_btn5 = QPushButton("Купити")
    qest_btn6 = QPushButton("Купити")
    qest_btn7 = QPushButton("Купити")
    qest_btn8 = QPushButton("Купити")
    qest_btn9 = QPushButton("Купити")
    qest_btn10 = QPushButton("Купити")
    qest_btn11 = QPushButton("Купити")
    qest_btn12 = QPushButton("Купити")
    qest_btn13 = QPushButton("Купити")

    mine_line = QVBoxLayout()



    h1 = QHBoxLayout()

    v1 = QVBoxLayout()
    v1.addWidget(answer_lbl_14)
    v1.addWidget(img_lbl1)
    v1.addWidget(answer_lbl_1)
    v1.addWidget(qest_btn1)
    h1.addLayout(v1)

    v2 = QVBoxLayout()
    v2.addWidget(answer_lbl_15)
    v2.addWidget(img_lbl2)
    v2.addWidget(answer_lbl_2)
    v2.addWidget(qest_btn2)
    h1.addLayout(v2)

    v3 = QVBoxLayout()
    v3.addWidget(answer_lbl_16)
    v3.addWidget(img_lbl3)
    v3.addWidget(answer_lbl_3)
    v3.addWidget(qest_btn3)
    h1.addLayout(v3)

    mine_line.addLayout(h1)


    h2 = QHBoxLayout()
    v1 = QVBoxLayout()
    v1.addWidget(img_lbl4)
    v1.addWidget(answer_lbl_4)
    v1.addWidget(qest_btn4)
    h2.addLayout(v1)

    v2 = QVBoxLayout()
    v2.addWidget(img_lbl5)
    v2.addWidget(answer_lbl_5)
    v2.addWidget(qest_btn5)
    h2.addLayout(v2)

    v3 = QVBoxLayout()
    v3 = QVBoxLayout()
    v3.addWidget(img_lbl6)
    v3.addWidget(answer_lbl_6)
    v3.addWidget(qest_btn6)
    h2.addLayout(v3)

    mine_line.addLayout(h2)


    h3 = QHBoxLayout()
    v1 = QVBoxLayout()
    v1.addWidget(img_lbl7)
    v1.addWidget(answer_lbl_7)
    v1.addWidget(qest_btn7)
    h3.addLayout(v1)

    v2 = QVBoxLayout()
    v2.addWidget(img_lbl8)
    v2.addWidget(answer_lbl_8)
    v2.addWidget(qest_btn8)
    h3.addLayout(v2)

    v3 = QVBoxLayout()
    v3 = QVBoxLayout()
    v3.addWidget(img_lbl9)
    v3.addWidget(answer_lbl_9)
    v3.addWidget(qest_btn9)
    h3.addLayout(v3)

    mine_line.addLayout(h3)


    h4 = QHBoxLayout()
    v1 = QVBoxLayout()
    v1.addWidget(img_lbl10)
    v1.addWidget(answer_lbl_10)
    v1.addWidget(qest_btn10)
    h4.addLayout(v1)

    v2 = QVBoxLayout()
    v2.addWidget(img_lbl11)
    v2.addWidget(answer_lbl_11)
    v2.addWidget(qest_btn11)
    h4.addLayout(v2)


    v3 = QVBoxLayout()
    v3.addWidget(img_lbl12)
    v3.addWidget(answer_lbl_12)
    v3.addWidget(qest_btn12)
    h4.addLayout(v3)

    mine_line.addLayout(h4)

    h5 = QHBoxLayout()
    v1 = QVBoxLayout()
    v1.addWidget(img_lbl13)
    v1.addWidget(answer_lbl_13)
    v1.addWidget(qest_btn13)
    h5.addLayout(v1)

    mine_line.addLayout(h5)


    img_lbl1.setPixmap(pixmax1)
    img_lbl2.setPixmap(pixmax2)
    img_lbl3.setPixmap(pixmax3)
    img_lbl4.setPixmap(pixmax4)
    img_lbl5.setPixmap(pixmax5)
    img_lbl6.setPixmap(pixmax6)
    img_lbl7.setPixmap(pixmax7)
    img_lbl8.setPixmap(pixmax8)
    img_lbl9.setPixmap(pixmax9)
    img_lbl10.setPixmap(pixmax10)
    img_lbl11.setPixmap(pixmax11)
    img_lbl12.setPixmap(pixmax12)
    img_lbl13.setPixmap(pixmax13)

    def menu_show(price, element):
        window.hide()
        qest_window.menu_window(price, element)
        window.show()
        settings = read_data()
        answer_lbl_15.setText(str(settings["money"]))





    qest_btn1.clicked.connect(lambda price: menu_show(15, "браслет"))
    qest_btn2.clicked.connect(lambda price: menu_show(25, "наліпки"))
    qest_btn3.clicked.connect(lambda price: menu_show(25, "ручки,олівці"))
    qest_btn4.clicked.connect(lambda price: menu_show(30, "значки"))
    qest_btn5.clicked.connect(lambda price: menu_show(50, "попсокет"))
    qest_btn6.clicked.connect(lambda price: menu_show(100, "шкарпертки"))
    qest_btn7.clicked.connect(lambda price: menu_show(150, "пляшка"))
    qest_btn8.clicked.connect(lambda price: menu_show(180, "килимок"))
    qest_btn9.clicked.connect(lambda price: menu_show(220, "бананка"))
    qest_btn10.clicked.connect(lambda price: menu_show(250, "футболка"))
    qest_btn11.clicked.connect(lambda price: menu_show(250, "парасолька"))
    qest_btn12.clicked.connect(lambda price: menu_show(300, "Навушники"))
    qest_btn13.clicked.connect(lambda price: menu_show(1, "Донат на ЗСУ 1L = 1,5 грн."))

    window.setLayout(mine_line)
    window.show()
    window.exec()