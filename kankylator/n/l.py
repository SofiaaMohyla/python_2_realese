from PyQt6.QtWidgets import*
def settings():
    window = QDialog()

    main_line = QVBoxLayout()

    window.setLayout(main_line)
    window.show()
    window.exec()

("""     QWidget {
        background: #ccdaed;     }
     QPushButton {        background: #e9edf2;
        border-style: outset;        min-height: 30px;
        min-width: 100px;     }
     QListWidget {         background: #ccdbd5;
     }     QTextEdit { 
        background: #e1ede8;     }
      QPushButton {
        color: green;        font-size: 15px;
        font-family: Impact;        border-width: 2px;
        border-color: red;        border-radius: 5px;
     }
      QPushButton#save_btn {
        color: green;        font-size: 20px;
        font-family: Impact;        border-width: 4px;
        border-color: red;        border-radius: 5px;
      }
 """)
