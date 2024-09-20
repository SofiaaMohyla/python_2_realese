from PyQt6.QtWidgets import*

from n.l import settings

app = QApplication([])
window = QWidget()
window.resize(700,500)
app.setStyleSheet("""     
QWidget {
        background: black;    
         }
     QPushButton {        background: #e9edf2;
        border-style: outset;        min-height: 30px;
        min-width: 100px;     }
     QListWidget {         background: black; color: black;
     }     QTextEdit { 
        background: #e1ede8;     }
      QPushButton {
        color: black;        font-size: 15px;
        font-family: Impact;        border-width: 2px;
        border-color: gray;        border-radius: 5px;
     }
      QPushButton#save_btn {
        color: green;        font-size: 20px;
        font-family: Impact;        border-width: 4px;
        border-color: grey;        border-radius: 5px;
      }
      QLineEdit {
        background-color: white;
        color: black;
        
      }
 """)
main_line = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
h5 = QHBoxLayout()
wikno = QLineEdit()
plus_btn = QPushButton("+")
minys_btn = QPushButton("-")
dilenya_btn = QPushButton(":")
mnogennya_btn = QPushButton("*")
odun_btn = QPushButton("1")
dwa_btn = QPushButton("2")
tru_btn = QPushButton("3")
choturu_btn = QPushButton("4")
five_btn = QPushButton("5")
six_btn = QPushButton("6")
seven_btn = QPushButton("7")
visim_btn = QPushButton("8")
nine_btn = QPushButton("9")
zero_btn = QPushButton("0")
tochka_btn = QPushButton(".")
answer_btn = QPushButton("=")
AC_btn = QPushButton("AC")
sett_btn = QPushButton("n/l")
main_line.addWidget(wikno)
h1.addWidget(seven_btn)
h1.addWidget(visim_btn)
h1.addWidget(nine_btn)
h1.addWidget(dilenya_btn)
main_line.addLayout(h1)
h2.addWidget(choturu_btn)
h2.addWidget(five_btn)
h2.addWidget(six_btn)
h2.addWidget(mnogennya_btn)
main_line.addLayout(h2)
h3.addWidget(odun_btn)
h3.addWidget(dwa_btn)
h3.addWidget(tru_btn)
h3.addWidget(minys_btn)
main_line.addLayout(h3)

h4.addWidget(zero_btn)
h4.addWidget(plus_btn)
h4.addWidget(tochka_btn)
h4.addWidget(answer_btn)
main_line.addLayout(h4)

h5.addWidget(AC_btn)
h5.addWidget(sett_btn)
main_line.addLayout(h5)
def plus_funk():
    text = wikno.text()
    text += '+'
    wikno.setText(text)

plus_btn.clicked.connect(plus_funk)
def minys_funk():
    text = wikno.text()
    text += '-'
    wikno.setText(text)

minys_btn.clicked.connect(minys_funk)
def dilenya_funk():
    text = wikno.text()
    text += ':'
    wikno.setText(text)

dilenya_btn.clicked.connect(dilenya_funk)
def mnogennya_funk():
    text = wikno.text()
    text += '*'
    wikno.setText(text)

mnogennya_btn.clicked.connect(mnogennya_funk)
def odun_funk():
    text = wikno.text()
    text += '1'
    wikno.setText(text)

odun_btn.clicked.connect(odun_funk)
def dwa_funk():
    text = wikno.text()
    text += '2'
    wikno.setText(text)

dwa_btn.clicked.connect(dwa_funk)
def tru_funk():
    text = wikno.text()
    text += '3'
    wikno.setText(text)

tru_btn.clicked.connect(tru_funk)
def choturu_funk():
    text = wikno.text()
    text += '4'
    wikno.setText(text)

choturu_btn.clicked.connect(choturu_funk)
def five_funk():
    text = wikno.text()
    text += '5'
    wikno.setText(text)

five_btn.clicked.connect(five_funk)
def six_funk():
    text = wikno.text()
    text += '6'
    wikno.setText(text)

six_btn.clicked.connect(six_funk)
def seven_funk():
    text = wikno.text()
    text += '7'
    wikno.setText(text)

seven_btn.clicked.connect(seven_funk)
def visim_funk():
    text = wikno.text()
    text += '8'
    wikno.setText(text)

visim_btn.clicked.connect(visim_funk)
def nine_funk():
    text = wikno.text()
    text += '9'
    wikno.setText(text)

nine_btn.clicked.connect(nine_funk)
def zero_funk():
    text = wikno.text()
    text += '0'
    wikno.setText(text)

zero_btn.clicked.connect(zero_funk)
def answer_funk():
    text = wikno.text()
    text = text.replace(":","/")
    text = str(eval(text))
    wikno.setText(text)

answer_btn.clicked.connect(answer_funk)

def tochka_funk():
    text = wikno.text()
    text += '.'
    wikno.setText(text)

tochka_btn.clicked.connect(tochka_funk)
def AC_funk():
    text = wikno.text()
    text = text[:len(text)-1]
    wikno.setText(text)

sett_btn.clicked.connect(settings)
AC_btn.clicked.connect(AC_funk)
window.setLayout(main_line)
window.show()
app.exec()