import cakedetails,profit_page,order,database
import sys
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CustomerDetailsApp(QWidget):

    back_clicked = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Customer Details")
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

        # Customer Details Section
        customer_details_layout = QGridLayout()
        customer_details_layout.addWidget(QLabel("<font size=5>Customer Name:"), 0, 0)
        customer_details_layout.addWidget(QLabel("<font size=5>Customer Age:"), 1, 0)
        customer_details_layout.addWidget(QLabel("<font size=5>Customer Gender:"), 2, 0)
        customer_details_layout.addWidget(QLabel("<font size=5>Customer Address:"), 3, 0)
        customer_details_layout.addWidget(QLabel("<font size=5>Customer Phone No:"), 4, 0)
        customer_details_layout.addWidget(QLabel("<font size=5>Customer Email:"), 5, 0)

       


        # #size defined for labels
        # customer_details_layout

        self.customer_name_edit = QLineEdit()
        self.customer_name_edit.setFixedSize(250,30)
        customer_details_layout.addWidget(self.customer_name_edit, 0, 1)

        self.customer_age_edit = QLineEdit()
        self.customer_age_edit.setFixedSize(80,30)
        customer_details_layout.addWidget(self.customer_age_edit, 1, 1)

        self.gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        self.other_radio = QRadioButton("Other")
        self.female_radio.setStyleSheet(" font-size : 16px")
        self.male_radio.setStyleSheet(" font-size : 16px")
        self.other_radio.setStyleSheet(" font-size : 16px")
        

        self.gender_layout.addWidget(self.male_radio)
        self.gender_layout.addWidget(self.female_radio)
        self.gender_layout.addWidget(self.other_radio)
        customer_details_layout.addLayout(self.gender_layout, 2, 1)

        self.customer_address_edit = QTextEdit()
        self.customer_address_edit.setFixedSize(250,300)
        customer_details_layout.addWidget(self.customer_address_edit, 3, 1)

        self.customer_phone_edit = QLineEdit()
        self.customer_phone_edit.setFixedSize(250,30)
        customer_details_layout.addWidget(self.customer_phone_edit, 4, 1)

        self.customer_email_edit = QLineEdit()
        self.customer_email_edit.setFixedSize(250,30)
        customer_details_layout.addWidget(self.customer_email_edit, 5, 1)

        left_layout.addLayout(customer_details_layout)

        # Button Section
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add")
        edit_button = QPushButton("Edit")
        back_button = QPushButton("Back")
        #button style 
        #label size
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
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Age", "Gender", "Address", "Phone No", "Email"])
        header = self.table.horizontalHeader()
        header.setStyleSheet("background-color: lightblue;")
        
        self.table.setFixedSize(800, 550)
        right_layout.addWidget(self.table)

        #fetching all details
        data_list = database.fetch_customer()
        self.populate_table(data_list)

        # Create a spacer item and add it to the layout
        right_layout.addStretch()

        # Refresh Button
        refresh_button = QPushButton("Refresh")
        refresh_button.setFixedSize(150 ,30)
        right_layout.addWidget(refresh_button)
        refresh_button.setStyleSheet(" color: black ; font-size : 16px  ; background-color : lightpink")
        main_layout.addLayout(right_layout)

        #buttons connections
        add_button.clicked.connect(self.save)
        edit_button.clicked.connect(self.edit)
        back_button.clicked.connect(self.back_to_cake_shop)
        refresh_button.clicked.connect(self.refresh)

    #populating data table
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
        name = self.customer_name_edit.text()
        age = int(self.customer_age_edit.text())
        if self.female_radio.clicked:
            gender = 'FEMALE'
        elif self.male_radio.clicked:
            gender = 'MALE'
        else : 
            gender = 'OTHER'
        address = self.customer_address_edit.toPlainText()
        phone = int(self.customer_phone_edit.text())
        email = self.customer_email_edit.text()
        database.insert_customer(name,age,gender,address,phone,email)

        self.customer_name_edit.clear()
        self.customer_age_edit.clear()
        if gender == 'FEMALE':
            self.female_radio.setChecked(False)
        else:
            self.male_radio.setChecked(False)
        self.customer_address_edit.clear()
        self.customer_phone_edit.clear()
        self.customer_email_edit.clear()
        self.refresh()

    def edit(self):
        pass

    def refresh(self):
        data = database.fetch_customer()
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
    window = CustomerDetailsApp()
    window.show()
    sys.exit(app.exec_())
