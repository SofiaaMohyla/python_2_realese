from PyQt5.QtWidgets import *
import requests



def kripta_window():
    window = QDialog()
    window.resize(800, 700)
    gut = QPushButton("Розрахувати")
    line5 = QLineEdit()
    line6 = QLineEdit()
    line7 = QLineEdit()


    main_line = QVBoxLayout()


    main_line.addWidget(line5)
    main_line.addWidget(line6)
    main_line.addWidget(line7)
    main_line.addWidget(gut)



    window.setStyleSheet("""
            QLineEdit
            {
                border-style: inset;
                border-width: 5px;
                border-radius: 9px   
            }
        """)









    def fuic():
        bit = line5.text()
        usdt = line6.text()

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
            print(f"Поточний курс BTC до USD: {rate}")
        else:
            print(f"Помилка запиту: {response.status_code}")

    gut.clicked.connect(fuic)
    window.setLayout(main_line)
    window.show()
    window.exec()