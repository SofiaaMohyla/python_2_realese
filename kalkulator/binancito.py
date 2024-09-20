from PyQt5.QtWidgets import *
import requests



def binanco_window():
    window = QDialog()
    window.resize(800, 700)


    TEC = QLabel("ТЕХНІЧНА ПЕРЕРВА")
    main_line.addWidget(TEC)

    window.setLayout(main_line)
    window.show()
    window.exec()




