from PyQt5.QtWidgets import *
import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
p = requests.get(url)
if p.status_code == 200:
    data = p.json()
    print(data)
else:
    print(" Ну ти і лох")
