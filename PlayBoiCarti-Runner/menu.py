from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from LvL.Lvl1 import *
from LvL.Lvl2 import *
from pygame import *
from LvL.Lvl3 import *
import json
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QPushButton, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QPen
class MyMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PlayBoiCarti Runner")
        self.screen_rect = QDesktopWidget().availableGeometry()
        width = 900
        height = 500
        x = (self.screen_rect.width() - width) / 2
        y = (self.screen_rect.height() - height) / 2
        self.setFixedSize(900, 500)
        self.TextTitle = QLabel("TextTitle")
        self.TextTitlee = QPixmap("TitleText.png")
        self.TextTitlee = self.TextTitlee.scaledToWidth(300 ,100)
        self.TextTitle.setPixmap(self.TextTitlee)
        self.Img = QLabel("Img")
        self.image = QPixmap("Whole_Lotta_Red.png")
        self.image = self.image.scaledToWidth(500)
        self.Img.setPixmap(self.image)
        self.PlayButton = QPushButton("Грати", self)
        self.SettingsButton = QPushButton("Налаштування", self)

        self.mainLine = QHBoxLayout(self)
        self.vLine = QVBoxLayout()
        self.vLine1 = QHBoxLayout()
        self.vLine2 = QHBoxLayout()
        self.vLine3 = QHBoxLayout()

        self.mainLine.addWidget(self.Img)
        self.vLine.addLayout(self.vLine3)
        self.vLine.addLayout(self.vLine2)
        self.vLine.addLayout(self.vLine1)
        self.mainLine.addLayout(self.vLine)
        
        self.vLine.addStretch()
        self.vLine.addWidget(self.TextTitle)
        self.vLine.addStretch()
        self.vLine.addWidget(self.PlayButton)
        self.vLine.addWidget(self.SettingsButton)
        self.vLine.addStretch()

        self.levelExit = QPushButton("<", self)
        self.levelExit.setFixedSize(40, 40)
        self.levelExit.hide()
        self.level1_button = QPushButton("1", self)
        self.level1_button.hide()
        self.level2_button = QPushButton("2", self)
        self.level2_button.hide()
        self.level3_button = QPushButton("3", self)
        self.level3_button.hide()

        self.mainLine.addWidget(self.level1_button)
        self.mainLine.addWidget(self.level2_button)
        self.mainLine.addWidget(self.level3_button)

        self.PlayButton.clicked.connect(self.show_levels)
        self.levelExit.clicked.connect(self.exit)
        self.level1_button.clicked.connect(lvl1)
        self.level2_button.clicked.connect(lvl2)
        self.level3_button.clicked.connect(lvl3)

        self.levelExit.setObjectName("levelExit")
        self.level1_button.setObjectName("level1_button")
        self.level2_button.setObjectName("level2_button")
        self.level3_button.setObjectName("level3_button")
        self.PlayButton.setObjectName("playButton")
        self.SettingsButton.setObjectName("settingsButton")

        initial_json = """
        {
            "HeroSpeed": 5,
            "MonsterSpeed": 2,
            "MusicVolumeLvl": 0.1
        }
        """
        self.json_data = json.loads(initial_json)
        self.HeroSpeed = QLineEdit("5")
        self.HeroSpeed.setFixedSize(270, 370)
        self.HeroSpeed.hide()
        self.MonsterSpeed = QLineEdit("2")
        self.MonsterSpeed.setFixedSize(270, 370)
        self.MonsterSpeed.hide()
        self.MusicVolumeLvl = QLineEdit("0.1")
        self.MusicVolumeLvl.setFixedSize(270, 370)
        self.MusicVolumeLvl.hide()
        self.update_button = QPushButton('Оновити')
        self.update_button.hide()
        self.exitsettings = QPushButton("<", self)
        self.exitsettings.setGeometry(10, 10, 25, 25)
        self.exitsettings.hide()

        self.O = QWidget()
        self.O.setFixedHeight(20)
        self.O.hide()
        self.HeroSpeedText = QLabel("Швидкість персонажа")
        self.HeroSpeedText.hide()
        self.MonsterSpeedText = QLabel("Швидкість монстра")
        self.MonsterSpeedText.hide()
        self.MusicVolumeLvlText = QLabel("Гучність музики")
        self.MusicVolumeLvlText.hide()

        def update_json():
            input_HeroSpeed = self.HeroSpeed.text() 
            input_MonsterSpeed = self.MonsterSpeed.text() 
            input_MusicVolumeLvl = self.MusicVolumeLvl.text() 
            self.json_data['HeroSpeed'] = int(input_HeroSpeed)
            self.json_data['MonsterSpeed'] = int(input_MonsterSpeed)
            self.json_data['MusicVolumeLvl'] = float(input_MusicVolumeLvl)
            with open('LvL/SettingsC.json', 'w') as json_file:
                    json.dump(self.json_data, json_file)
        self.update_button.clicked.connect(update_json)
        
        self.vLine1.addWidget(self.HeroSpeed)
        self.vLine1.addWidget(self.MonsterSpeed)
        self.vLine1.addWidget(self.MusicVolumeLvl)
        self.vLine2.addWidget(self.HeroSpeedText)
        self.vLine2.addWidget(self.MonsterSpeedText)
        self.vLine2.addWidget(self.MusicVolumeLvlText)
        self.vLine3.addWidget(self.O)
        self.vLine.addWidget(self.update_button)

        self.SettingsButton.clicked.connect(self.show_settings)
        self.exitsettings.clicked.connect(self.exit)

        self.HeroSpeed.setObjectName("HeroSpeed")
        self.MonsterSpeed.setObjectName("MonsterSpeed")
        self.MusicVolumeLvl.setObjectName("MusicVolumeLvl")
        self.HeroSpeedText.setObjectName("HeroSpeedText")
        self.MonsterSpeedText.setObjectName("MonsterSpeedText")
        self.MusicVolumeLvlText.setObjectName("MusicVolumeLvlText")
        self.exitsettings.setObjectName("exitsettings")
        self.update_button.setObjectName("update_button")

        self.save_state_signal = pyqtSignal()

        def closeEvent(self, event):
            self.save_state_signal.emit()
            event.accept()

        def open_pygame_window(self):
            self.save_state_signal.emit()
            lvl1()
            self.show()

    def show_settings(self):
        self.HeroSpeed.show()
        self.MonsterSpeed.show()
        self.MusicVolumeLvl.show()
        self.update_button.show()
        self.TextTitle.hide()
        self.Img.hide()
        self.PlayButton.hide()
        self.SettingsButton.hide()
        self.levelExit.hide()
        self.level1_button.hide()
        self.level2_button.hide()
        self.level3_button.hide()
        self.exitsettings.show()
        self.HeroSpeedText.show()
        self.MonsterSpeedText.show()
        self.MusicVolumeLvlText.show()
        self.O.show()
    
    def show_levels(self):
        self.TextTitle.hide()
        self.Img.hide()
        self.PlayButton.hide()
        self.SettingsButton.hide()
        self.levelExit.show()
        self.level1_button.show()
        self.level2_button.show()
        self.level3_button.show()
        self.HeroSpeed.hide()
        self.MonsterSpeed.hide()
        self.MusicVolumeLvl.hide()
        self.update_button.hide()
        self.exitsettings.hide()
        self.HeroSpeedText.hide()
        self.MonsterSpeedText.hide()
        self.MusicVolumeLvlText.hide()
        self.O.hide()

    def exit(self):
        self.TextTitle.show()
        self.Img.show()
        self.PlayButton.show()
        self.SettingsButton.show()
        self.levelExit.hide()
        self.level1_button.hide()
        self.level2_button.hide()
        self.level3_button.hide()
        self.HeroSpeed.hide()
        self.MonsterSpeed.hide()
        self.update_button.hide()
        self.MusicVolumeLvl.hide()
        self.update_button.hide()
        self.exitsettings.hide()
        self.HeroSpeedText.hide()
        self.MonsterSpeedText.hide()
        self.MusicVolumeLvlText.hide()
        self.O.hide()


if __name__ == "__main__":
    app = QApplication([])
    menu = MyMenu()
    app.setStyleSheet("""
        QPushButton#playButton {
            border: 2px solid black;
            font-size: 15px;
            padding: 15px 2px;
            margin-right: 50px;
        }
        QPushButton#levelExit {
            font-size: 10px;
            width: 40px;
            height: 40px;
            margin: 10px 0px 0px 10px;
            font-weight: bold;
            background-image: url("Exit");
            background-repeat: no-repeat; 
            background-position: center;
        }
        QPushButton#settingsButton {
            border: 2px solid black;
            font-size: 15px;
            padding: 15px 2px;
            margin-right: 50px;
        }
        QPushButton#level1_button {
            border: none;
            font-weight: bold;
            background-image: url("lvl_1");
            background-repeat: no-repeat; 
            background-position: center;
            padding: 200px 50px;
            margin-right: 10px;
        }
        QPushButton#level2_button {
            border: none;
            font-weight: bold;
            background-image: url("lvl_2");
            background-repeat: no-repeat; 
            background-position: center;
            padding: 200px 50px;
            margin-right: 10px;
        }
        QPushButton#level3_button {
            color: rgba(217, 217, 217, 0.01);
            border: none;
            font-weight: bold;
            background-image: url("lvl_3");
            background-repeat: no-repeat; 
            background-position: center;
            padding: 200px 50px;
        }
        QPushButton#level1_button:hover {
            margin-top: -20px;
        }
        QPushButton#level2_button:hover {
            margin-top: -20px;
        }
        QPushButton#level3_button:hover {
            margin-top: -20px;
        }
        QWidget {
            background-color: white;
        }
        QLineEdit#HeroSpeed {
            border: none;
            font-size: 200px;
        }
        QLineEdit#MonsterSpeed {
            border: none;
            font-size: 200px;
        }
        QLineEdit#MusicVolumeLvl {
            border: none;
            font-size: 200px;
        }
        QLabel#HeroSpeedText {
            font-size: 10px;
            border-bottom: 1px solid black;
        }
        QLabel#MonsterSpeedText {
            font-size: 10px;
            border-bottom: 1px solid black;
        }
        QLabel#MusicVolumeLvlText {
            font-size: 10px;
            padding: 2px;
            border-bottom: 1px solid black;
        }
        QPushButton#update_button {
            border: 2px solid black;
            padding: 5px;
        }
        QPushButton#exitsettings {
            background-image: url("Exit");
            background-repeat: no-repeat; 
            background-position: center;
        }
    """)
    menu.show()
    app.exec_()
