from PyQt5.QtWidgets import *
import requests



def menu_window():
    window = QDialog()
    window.resize(400, 300)
    get = QPushButton("Розрахувати")
    line = QLineEdit()
    line2 = QLineEdit()
    line3 = QLineEdit()
    line4 = QLineEdit()


    main_line = QVBoxLayout()


    main_line.addWidget(line)
    main_line.addWidget(line2)
    main_line.addWidget(line3)
    main_line.addWidget(line4)
    main_line.addWidget(get)



    window.setStyleSheet("""
     QLineEdit
                {
                    border-style: inset;
                    border-width: 5px;
                    border-radius: 9px   
                }
                
                QPushButton
                {
                    background-color: #0021c5;  
                }
                
                QLineEdit
                {
                    font-size: 35px;  
                }
                
                 QPushButton
                {
                    font-size: 35px;  
                }
                
                
            """)





    def func():
        val = line.text()
        date = line2.text()
        kilka = int(line3.text())



        url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&date={date}&json"
        p = requests.get(url)
        if p.status_code == 200:
            data = p.json()
            print(data)
            line4.setText(str(data[0]["rate"] * kilka))
        else:
            print(" Ні")


    get.clicked.connect(func)
    window.setLayout(main_line)
    window.show()
    window.exec()