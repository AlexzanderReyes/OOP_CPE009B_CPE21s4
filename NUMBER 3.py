import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import pyqtSlot

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Window settings
        self.setWindowTitle('Midterm in OOP')
        self.setGeometry(100, 100, 400, 200)
        
        # Layout
        layout = QVBoxLayout()

        # Fullname input
        self.fullname_label = QLabel('Enter your fullname:')
        self.fullname_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.fullname_label)

        self.fullname_input = QLineEdit(self)
        layout.addWidget(self.fullname_input)

        # Button to display fullname
        self.display_button = QPushButton('Click to display your fullname', self)
        self.display_button.setFont(QFont('Arial', 12))
        self.display_button.clicked.connect(self.display_fullname)
        layout.addWidget(self.display_button)

        # Label to show the displayed fullname
        self.display_label = QLabel('', self)
        self.display_label.setFont(QFont('Arial', 12))
        self.display_label.setStyleSheet("color: red;")  # Set font color to red
        layout.addWidget(self.display_label)

        # Set layout
        self.setLayout(layout)

    @pyqtSlot()
    def display_fullname(self):
        # Get the text from the input field and display it
        fullname = self.fullname_input.text()
        self.display_label.setText(fullname)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())