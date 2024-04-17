import customer_details,profit_page,order,database
from PyQt5.QtGui import QColor, QPalette
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CakeDetailsApp(QWidget):

    back_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MERWANS - Cake Details")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()
        self.setFixedSize(1200, 615) 
        self.center()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(173, 216, 230))
        self.setPalette(palette)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        center_p = screen.center()
        window.moveCenter(center_p)
        self.setGeometry(window)
        
    def initUI(self):
        main_layout = QHBoxLayout(self)

        # Left Side Layout
        left_layout = QVBoxLayout()

        # Cake Details Section
        cake_details_layout = QGridLayout()
        cake_details_layout.addWidget(QLabel("<font size=5>Cake Name:"), 0, 0)
        cake_details_layout.addWidget(QLabel("<font size=5>Cake Egg:"), 1, 0)
        cake_details_layout.addWidget(QLabel("<font size=5>Description:"), 2, 0)
        cake_details_layout.addWidget(QLabel("<font size=5>Weight:"), 3, 0)
        cake_details_layout.addWidget(QLabel("<font size=5>Quantity:"), 4, 0)
        cake_details_layout.addWidget(QLabel("<font size=5>Price:"), 5, 0)

        self.cake_name_edit = QLineEdit()
        self.cake_name_edit.setFixedSize(250,30)
        cake_details_layout.addWidget(self.cake_name_edit, 0, 1)

        self.cake_egg_yes = QRadioButton("Yes")
        self.cake_egg_no = QRadioButton("No")
        self.cake_egg_yes.setStyleSheet(" font-size : 16px")
        self.cake_egg_no.setStyleSheet(" font-size : 16px")
        self.egg_layout = QHBoxLayout()
        self.egg_layout.addWidget(self.cake_egg_yes)
        self.egg_layout.addWidget(self.cake_egg_no)
        cake_details_layout.addLayout(self.egg_layout, 1, 1)

        self.cake_description_edit = QTextEdit()
        self.cake_description_edit.setFixedSize(250,300)
        cake_details_layout.addWidget(self.cake_description_edit, 2, 1)

        self.cake_weight_combo = QComboBox()
        self.cake_weight_combo.setFixedSize(50,30)
        self.cake_weight_combo.setStyleSheet("font-size: 16px;")
        self.cake_weight_combo.addItems(["0.5", "1", "1.5", "2", "2.5", "3"])
        cake_details_layout.addWidget(self.cake_weight_combo, 3, 1)

        self.cake_quantity_edit = QLineEdit()
        self.cake_quantity_edit.setFixedSize(250,30)
        cake_details_layout.addWidget(self.cake_quantity_edit, 4, 1)

        self.cake_price_edit = QLineEdit()
        self.cake_price_edit.setFixedSize(250,30)
        cake_details_layout.addWidget(self.cake_price_edit, 5, 1)

        left_layout.addLayout(cake_details_layout)

        # Button Section
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add")
        edit_button = QPushButton("Edit")
        back_button = QPushButton("Back")

        add_button.setStyleSheet(" color: black ; font-size : 16px ; background-color : lightpink")
        edit_button.setStyleSheet(" color: black ; font-size : 16px  ; background-color : lightpink")
        back_button.setStyleSheet(" color: black ; font-size : 16px  ; background-color : lightpink")
        #button size
        add_button.setFixedSize(120,30)
        edit_button.setFixedSize(120,30)
        back_button.setFixedSize(120,30)

        
        button_layout.addWidget(add_button)
        # button_layout.addWidget(edit_button)
        button_layout.addWidget(back_button)
        left_layout.addLayout(button_layout)

        main_layout.addLayout(left_layout)

        # Right Side Layout
        right_layout = QVBoxLayout()

        # Table Section
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setFixedSize(800, 550)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Egg", "Description", "Weight", "Quantity", "Price"])
        right_layout.addWidget(self.table)

        header = self.table.horizontalHeader()
        header.setStyleSheet("background-color: lightblue;")

        #fetching all details
        data_list = database.fetch_cake()
        self.populate_table(data_list)

        # Create a spacer item and add it to the layout
        right_layout.addStretch()

        # Refresh Button
        refresh_button = QPushButton("Refresh")
        refresh_button.setFixedSize(120,30)
        right_layout.addWidget(refresh_button)
        refresh_button.setStyleSheet(" color: black ; font-size : 16px  ; background-color : lightpink")
        
        

        main_layout.addLayout(right_layout)


        #buttons connections
        add_button.clicked.connect(self.save)
        edit_button.clicked.connect(self.edit)
        back_button.clicked.connect(self.back_to_cake_shop)
        refresh_button.clicked.connect(self.refresh)

    def populate_table(self, data):
        if data is None:
            row_count = 0
        else:
            row_count = len(data)
            self.table.setRowCount(row_count)

            for row, row_data in enumerate(data):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(row, col, item)

    #functons for buttons
    def save(self):
        name = self.cake_name_edit.text()  
        if self.cake_egg_yes.clicked:
            egg = 'EGG'
        else:
            egg = 'EGGLESS'
        description = self.cake_description_edit.toPlainText()
        weight = float(self.cake_weight_combo.currentText())
        quantity = int(self.cake_quantity_edit.text())
        price = float(self.cake_price_edit.text())
        database.insert_cake(name,egg,description,weight,quantity,price)

        self.cake_name_edit.clear()
        if egg == 'EGG':
            self.cake_egg_yes.setChecked(False)
        else:
            self.cake_egg_no.setChecked(False)
        self.cake_description_edit.clear()
        self.cake_quantity_edit.clear()
        self.cake_price_edit.clear()
        self.refresh()

    def edit(self):
        pass

    def refresh(self):
        data = database.fetch_cake()
        if data is None:
            row_count = 0
        else:
            row_count = len(data)
            self.table.setRowCount(row_count)

            for row, row_data in enumerate(data):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(row, col, item)
            print('Refresh button clicked')
        

    def back_to_cake_shop(self):
        # Emit the back_clicked signal when the back button is clicked
        print('back button clicked')
        self.back_clicked.emit()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CakeDetailsApp()
    window.show()
    sys.exit(app.exec_())
