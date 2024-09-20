

from PyQt5.QtWidgets import *
import requests

{

    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}

p = requests.get(url)
if p.status_code == 200:
    data = p.json()
    print(data)
else:
    print(" Ну ти і лох")
