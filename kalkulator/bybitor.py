import requests
from PyQt5.QtWidgets import *


def bybito_window():
    window = QDialog()
    window.resize(400, 300)

    gut = QPushButton("Розрахувати")
    line5 = QLineEdit()
    line6 = QLineEdit()
    line7 = QLineEdit()
    line8 = QLineEdit()

    main_line = QVBoxLayout()

    main_line.addWidget(line5)
    main_line.addWidget(line6)
    main_line.addWidget(line7)
    main_line.addWidget(line8)
    main_line.addWidget(gut)

    window.setStyleSheet("""
                QLineEdit
                {
                    border-style: inset;
                    border-width: 5px;
                    border-radius: 9px   
                }
                
                QPushButton
                {
                    background-color: #ff2206;  
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

    # Замість 'YOUR_API_KEY' вставте свій ключ API з CoinAPI

    def fuic():
        bit = line5.text()
        usdt = line6.text()
        kilkist = int(line7.text())

        api_key = "892301DD-2E60-4DBE-B804-5BA33A5E6D4B"
        url = f'https://rest.coinapi.io/v1/exchangerate/{bit}/{usdt}'
        headers = {
            'X-CoinAPI-Key': api_key
        }

        response = requests.get(url, headers=headers)

        # Перевірка статусу відповіді
        if response.status_code == 200:
            data = response.json()
            rate = data['rate']  # Отримання курсу з відповіді
            line8.setText(str(data["rate"] * kilkist))
        else:
            print(" Ні")

    gut.clicked.connect(fuic)
    window.setLayout(main_line)
    window.show()
    window.exec()

