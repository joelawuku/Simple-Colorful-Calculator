import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ColorfulCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Colorful Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.initUI()

    def initUI(self):
        # Create the main layout
        self.layout = QVBoxLayout()

        # Display line
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 20))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("background-color: #ffffff; color: #000000; border: 2px solid #000000; border-radius: 10px; padding: 5px;")
        self.layout.addWidget(self.display)

        # Button grid layout
        self.grid_layout = QGridLayout()

        # Button labels
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        # Add buttons to the grid layout
        for label, row, col in buttons:
            button = QPushButton(label)
            button.setFont(QFont("Arial", 14))
            button.setStyleSheet(self.getButtonStyle(label))
            button.clicked.connect(self.onButtonClick)
            self.grid_layout.addWidget(button, row, col)

        self.layout.addLayout(self.grid_layout)

        # Set the main layout
        self.setLayout(self.layout)

    def getButtonStyle(self, label):
        # Define styles for buttons
        if label in {'+', '-', '*', '/'}:
            return "background-color: #ffcccb; color: #000000; border-radius: 5px; padding: 10px;"
        elif label == '=':
            return "background-color: #90ee90; color: #000000; border-radius: 5px; padding: 10px;"
        elif label == 'C':
            return "background-color: #add8e6; color: #000000; border-radius: 5px; padding: 10px;"
        else:
            return "background-color: #f0e68c; color: #000000; border-radius: 5px; padding: 10px;"

    def onButtonClick(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = ColorfulCalculator()
    calculator.show()
    sys.exit(app.exec_())
