import random
import json
from PyQt5 import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from pygame.time import wait
start_game_work = 0
notes = {}
jackpot_chance = 0
x_buyer = 0
random_crate = 0
backChange = 0


def read_data():
    global notes
    with open("database.json", "r", encoding="utf-8") as file:
        notes = json.load(file)



def write_data():
    global notes
    with open("database.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)
read_data()
app = QApplication([])

good = 0
app.setStyleSheet("""
        QPushButton {
            color:#35374B;
        background-color: #FFFFCC;
        }
        
        QWidget {
            color:#35374B;
        background-image: url("Back.png");
        }
        
                
        QLabel#introduction {
            color: #FF6666;
            border: 20px;
            font-size: 33px;
            fx-border-size: 15px;
        }
        QLabel#okk {
            color: #999900;
            font-size: 22px;

        }                 
        QLabel#Cases {            
             color: #999900; 
             font-size: 22px;
                                    
        }
        QPushButton#Open_crate {                  
             color: #35374B;             
             background-color: #FFFFCC;      
        }
        QPushButton#Name {                  
             font-size: 22px;           
             background-color: #ADD899;   
             height: 55px;   
             weight: 75px;   
        }
        QPushButton#lost {                  
             font-size: 22px;           
             background-color: #973131;   
             height: 55px;   
             weight: 75px;   
        }
        QPushButton#changed {                  
             font-size: 22px;           
             background-color: #9BEC00;   
             height: 55px;   
             weight: 75px;   
        }
        QPushButton#Addmore {                  
             font-size: 22px;           
             background-color: #adfc99;   
             height: 55px;   
             weight: 75px;   
        }
        QPushButton#changemore{                  
             font-size: 22px;           
             background-color: #adfc99;   
             height: 55px;   
             weight: 75px;   
        }                                              
    """)





add_perclick_button = QPushButton("Збільшити множувач монет:КОШТУЄ 10 МОНЕТ")
add_perclick_button5 = QPushButton("...")
add_perclick_button20 = QPushButton("...")
Byblik_coiner = QLabel("Бублік")
Byblik_coiner_px = QPixmap("pixil-frame-0 (1).png")
byblik_coiner_downpx = QPixmap("pixil-frame-0 (2).png")
Byblik_coiner.setPixmap(Byblik_coiner_px)


open_case = QPushButton("Відкрити кейс(1-10000+ монет)")
coins_count = QLabel("Ваші монети:"+str(notes["coins"]))
intro = QLabel("Математичні завдання!")
ans1 = QPushButton("49")
ans2 = QPushButton("7")
ans3 = QPushButton("23")
ans4 = QPushButton("5")
ans5 = QPushButton("2.3")
ans6 = QPushButton("6")

byblik_add10 = QPushButton("Вложити 10000 монет")
byblik_add = QPushButton("Вложити 1000 монет")
shop = QPushButton("Магазин")
byb_coiner = QPushButton("Бубл_койнер")
question = QLabel("Нажміть на кнопку старту для створення питання")
Start = QPushButton("Створити питання")
Case_count = QLabel("Ваші кейси:"+ str(notes["case_count"]))
byblik_get = QLabel("При виведенні ви получите:" + str(notes["byblik_addAmount"]))
byblik_lose = QPushButton("Вивести кошти з byblik")
byblik_change = QPushButton("Запустити курс(30 монет за 1 запуск)")
buy_case = QPushButton("Купити кейс КОШТУЄ 4000")
byblik_change10x = QPushButton("Запустити курс(300 монет за 10 запусків)")

window = QWidget()
window.resize(700, 500)

K1 = QVBoxLayout()

B1 = QHBoxLayout()
B2 = QHBoxLayout()
B3 = QHBoxLayout()


B2.addWidget(add_perclick_button)

K1.addWidget(coins_count)
K1.addWidget(Case_count)
B2.addWidget(add_perclick_button5)
B3.addWidget(open_case)
B3.addWidget(add_perclick_button20)
K1.addWidget(byb_coiner)
K1.addWidget(buy_case)

window.setLayout(K1)

K1.addLayout(B1)
K1.addLayout(B2)
K1.addLayout(B3)





byblik_Coiner = QDialog()
byblik_Coiner.resize(900,500)

N1 = QHBoxLayout()
M1 = QVBoxLayout()
M2 = QVBoxLayout()

byblik_Coiner.setLayout(N1)
N1.addLayout(M1)
N1.addLayout(M2)
M1.addWidget(Byblik_coiner)
M2.addWidget(byblik_add)
M2.addWidget(byblik_add10)
M2.addWidget(byblik_get)

M2.addWidget(byblik_lose)
M2.addWidget(byblik_change)
M2.addWidget(byblik_change10x)




def bybl_coinik():
    byblik_Coiner.show()

def invest():
    if notes["coins"] >= 1001:
        notes["coins"] -= 1000
        notes["byblik_addAmount"] += 1000
        byblik_get.setText("При виведенні ви получите:" + str(notes["byblik_addAmount"]))
        coins_count.setText("Ваші монети:"+str(notes["coins"]))
    else:
        print("Нехватає коштів!")

def invest10x():
    if notes["coins"] >= 10001:
        notes["coins"] -= 10000
        notes["byblik_addAmount"] += 10000
        byblik_get.setText("При виведенні ви получите:" + str(notes["byblik_addAmount"]))
        coins_count.setText("Ваші монети:" + str(notes["coins"]))
    else:
        print("Нехватає коштів!")

def buy_cases():
    if notes["coins"] >= 4000:
        notes["coins"] -= 4000
        notes["case_count"] += 1
        coins_count.setText("Ваші монети:"+str(notes["coins"]))
        Case_count.setText("Ваші кейси:"+ str(notes["case_count"]))
    else:
        print("Нехватає коштів!")


def exchange():
    if notes["byblik_addAmount"] >= 10:
        notes["coins"] += notes["byblik_addAmount"]
        notes["byblik_addAmount"] = 0
        byblik_get.setText("При виведенні ви получите:" + str(notes["byblik_addAmount"]))
        coins_count.setText("Ваші монети:"+str(notes["coins"]))
        print("Успішно")
    else:
        print("На рахунку немає коштів!")





menu_play = QDialog()
menu_play.resize(700,450)

menu_play.show()

H1 = QVBoxLayout()
V1 = QHBoxLayout()
V2 = QHBoxLayout()
V3 = QHBoxLayout()
V4 = QHBoxLayout()
V5 = QHBoxLayout()

menu_play.setLayout(H1)
H1.addLayout(V1)
H1.addLayout(V2)
H1.addLayout(V3)
H1.addLayout(V4)
H1.addLayout(V5)





V1.addWidget(question)

H1.addWidget(intro)
V2.addWidget(ans1)
V2.addWidget(ans2)
V3.addWidget(ans3)
V3.addWidget(ans4)
V4.addWidget(ans5)
V4.addWidget(ans6)
V5.addWidget(shop)
V5.addWidget(Start)



def gotoshop():
    coins_count.setText("Ваші монети:" + str(notes["coins"]))
    window.show()



def next_question():
    global good
    rand = random.randint(1,8)
    if rand == 1:
        question.setText("Скільки буде 7*7")
        good = 1
    if rand == 2:
        question.setText("Скільки буде 1-2+6")
        good = 2
    if rand == 3:
        question.setText("Скільки буде (2.6/2)+1")
        good = 3
    if rand == 4:
        question.setText("Скільки буде 30-7")
        good = 4
    if rand == 5:
        question.setText("Скільки буде 3*4/2")
        good = 5
    if rand == 6:
        question.setText("Скільки буде √25")
        good = 6
    if rand == 7:
        question.setText("Скільки буде √2401")
        good = 7
    if rand == 8:
        question.setText("Скільки буде 6-2-6-2+6+5")
        good = 8


def start_game():
    global good
    intro.setText("   ")
    rand = random.randint(1,8)
    global good
    global start_game_work
    if start_game_work == 0:
        rand = random.randint(1,8)
        if rand == 1:
            question.setText("Скільки буде 7*7")
            good = 1
        if rand == 2:
            question.setText("Скільки буде 1-2+6")
            good = 2
        if rand == 3:
            question.setText("Скільки буде (2.6/2)+1")
            good = 3
        if rand == 4:
            question.setText("Скільки буде 30-7")
            good = 4
        if rand == 5:
            question.setText("Скільки буде 3*4/2")
            good = 5
        if rand == 6:
            question.setText("Скільки буде √25")
            good = 6
        if rand == 7:
            question.setText("Скільки буде √2401")
            good = 7
        if rand == 8:
            question.setText("Скільки буде 6-2-6-2+6+5")
            good = 8
        start_game_work = 1

case_mon = random.randint(1,500)
def open_crates():
    global case_mon
    if notes["case_count"] >= 1:
        notes["case_count"] -= 1
        notes["coins"] += notes["money_x"]*case_mon
        Case_count.setText("Ваші кейси:"+ str(notes["case_count"]))
        coins_count.setText(("Ваші монети:"+str(notes["coins"])))



    else:
        pass

def CRATE():
    global random_crate
    random_crate = random.randint(0,33)
    if random_crate == 33:
        notes["case_count"] += 1
        random_crate = 0
        print("Ви получили кейс")
        Case_count.setText(("Ваші кейси:"+ str(notes["case_count"])))

def jackpot():
    global jackpot_chance
    jackpot_chance = random.randint(0,30)
    if jackpot_chance == 7:
        notes["coins"] += 7*notes["money_x"]
        print("Джекпот!")

def change_curs():
    global backChange
    if notes["coins"] >= 30:
        notes["coins"] -= 30
        coins_count.setText("Ваші монети:"+str(notes["coins"]))
        backChange = random.randint(1,2)
        if backChange == 1:
            Byblik_coiner.setPixmap(Byblik_coiner_px)
            notes["byblik_addAmount"] *= 2
            print(notes["byblik_addAmount"])
            byblik_get.setText("При виведенні ви получите:" + str(notes["byblik_addAmount"]))

        if backChange == 2:
            Byblik_coiner.setPixmap(byblik_coiner_downpx)
            notes["byblik_addAmount"] /= 2
            byblik_get.setText("При виведенні ви получите:" + str(notes["byblik_addAmount"]))
    else:
        print("У вас нехватає коштів!")

def change_curs10x():
    global backChange
    if notes["coins"] >= 300:
        notes["coins"] -= 300
        for i in range(10):
            coins_count.setText("Ваші монети:"+str(notes["coins"]))
            backChange = random.randint(1,2)
            if backChange == 1:
                Byblik_coiner.setPixmap(Byblik_coiner_px)
                notes["byblik_addAmount"] *= 2
                print(notes["byblik_addAmount"])
                byblik_get.setText("При виведенні ви получите:" + str(notes["byblik_addAmount"]))

            if backChange == 2:
                Byblik_coiner.setPixmap(byblik_coiner_downpx)
                notes["byblik_addAmount"] /= 2
                byblik_get.setText("При виведенні ви получите:" + str(notes["byblik_addAmount"]))
    else:
        print("У вас нехватає коштів!")




def answr49():
    global good
    if good == 1:
        notes["coins"] += notes["money_x"]
        print(1)
        jackpot()
        CRATE()
    next_question()


def answr5():
    if good == 2:
        notes["coins"] += notes["money_x"]
        jackpot()
        print(2)
        CRATE()
    next_question()


def answr2_3():
    if good == 3:
        notes["coins"] += notes["money_x"]
        jackpot()
        CRATE()
        print(3)
    next_question()
def answr23():
    if good == 4:
        notes["coins"] += notes["money_x"]
        jackpot()
        CRATE()
        print(4)
    next_question()
def answr6():
    if good == 5:
        notes["coins"] += notes["money_x"]
        jackpot()
        CRATE()
        print(5)
    next_question()
def answr5_2():
    if good == 6:
        notes["coins"] += notes["money_x"]
        jackpot()
        CRATE()
        print(6)
    next_question()
def answr2401():
    if good == 7:
        notes["coins"] += notes["money_x"]
        jackpot()
        CRATE()
        print(7)
    next_question()
def answr7():
    if good == 8:
        notes["coins"] += notes["money_x"]
        jackpot()
        CRATE()
        print(8)
    next_question()


def More_money_x():
    global x_buyer
    if x_buyer >= 4:
        add_perclick_button5.setText("Збільшити множувач монет на 5:КОШТУЄ 50 МОНЕТ")


    if x_buyer >= 20:
        print("Працює")
        add_perclick_button20.setText("Збільшити множувач монет на 20:КОШТУЄ 1500 МОНЕТ")

    if notes["coins"]>10:
        notes["money_x"] += 1
        notes["coins"] -= 10
        print("Успішна покупка!")
        coins_count.setText("Ваші монети:" + str(notes["coins"]))
        x_buyer += 1
    else:
        print("Нехватає коштів!")


def More_money_x5():
    global x_buyer
    print(f"{x_buyer=}")
    if x_buyer >= 20:
        print("Працює")
        add_perclick_button20.setText("Збільшити множувач монет на 20:КОШТУЄ 1500 МОНЕТ")


    if x_buyer >= 5:
        if notes["coins"]>50:
            notes["money_x"] += 5
            notes["coins"] -= 50
            print("Успішна покупка!")
            coins_count.setText("Ваші монети:" + str(notes["coins"]))
            x_buyer += 1
        else:
            print("Нехватає коштів!")
    print(notes["money_x"])



def More_money_x20():
    global x_buyer
    if x_buyer >= 20:
        if notes["coins"]>1500:
            notes["money_x"] += 20
            notes["coins"] -= 1500
            print("Успішна покупка!")
            coins_count.setText("Ваші монети:" + str(notes["coins"]))
            x_buyer += 1
        else:
            print("Нехватає коштів!")
    print(notes["money_x"])





Start.clicked.connect(start_game)
intro.setObjectName("introduction")
Case_count.setObjectName("Cases")
open_case.setObjectName("Open_crate")
coins_count.setObjectName("okk")
ans1.clicked.connect(answr49)
ans2.clicked.connect(answr7)
ans3.clicked.connect(answr23)
ans4.clicked.connect(answr5)
ans5.clicked.connect(answr2_3)
ans6.clicked.connect(answr6)
shop.clicked.connect(gotoshop)
add_perclick_button.clicked.connect(More_money_x)
add_perclick_button5.clicked.connect(More_money_x5)
add_perclick_button20.clicked.connect(More_money_x20)
open_case.clicked.connect(open_crates)
byb_coiner.clicked.connect(bybl_coinik)
byblik_add.clicked.connect(invest)
byblik_lose.clicked.connect(exchange)
byblik_change.clicked.connect(change_curs)
buy_case.clicked.connect(buy_cases)
byblik_add10.clicked.connect(invest10x)
byblik_change10x.clicked.connect(change_curs10x)
byblik_add.setObjectName("Name")
byblik_lose.setObjectName("lost")
byblik_change.setObjectName("changed")
byblik_add10.setObjectName("Addmore")
byblik_change10x.setObjectName("changemore")
app.exec()



