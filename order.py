import cakedetails,profit_page,customer_details,database
import sys
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class OrderDetailsApp(QWidget):  

    back_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Order Details")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()
        self.resize(1200, 600) 
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

        # Order Details Section
        order_details_layout = QGridLayout()
        order_details_layout.addWidget(QLabel("<font size=5>Cake Name:"), 0, 0)
        order_details_layout.addWidget(QLabel("<font size=5>Customer Phone No:"), 1, 0)
        order_details_layout.addWidget(QLabel("<font size=5>Weight Available:"), 2, 0)
        order_details_layout.addWidget(QLabel("<font size=5>Cake Quantity:"), 3, 0)
        

        self.cake_name_combo = QComboBox()
        data = database.fetch_cake()
        cake_set = {'som',} 
        cake_data  = []
        for i in data:
            cake_set.add(i[1])  

        cake_set.remove('som')

        for i in cake_set:
            cake_data.append(i)
        self.cake_name_combo.addItems(cake_data)
        self.cake_name_combo.setFixedSize(50,30)
        order_details_layout.addWidget(self.cake_name_combo, 0, 1)

        self.customer_phone_edit = QLineEdit()
        self.customer_phone_edit.setFixedSize(250,30)
        order_details_layout.addWidget(self.customer_phone_edit, 1, 1)

        self.weight_available_combo = QComboBox()
        self.weight_available_combo.addItems(["0.5", "1", "1.5", "2", "2.5", "3"])
        self.weight_available_combo.setFixedSize(50,30)       
        self.weight_available_combo.setStyleSheet(" color: black ; font-size : 16px ")

        order_details_layout.addWidget(self.weight_available_combo, 2, 1)

        

        self.cake_quantity_edit = QLineEdit()
        self.cake_name_combo.setFixedSize(250,30)
        order_details_layout.addWidget(self.cake_quantity_edit, 3, 1)


        left_layout.addLayout(order_details_layout)

        # Button Section
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add")
        edit_button = QPushButton("Edit")
        back_button = QPushButton("Back")
        add_button.setStyleSheet(" color: black ; font-size : 16px ; background-color : lightpink")
        edit_button.setStyleSheet(" color: black ; font-size : 16px ; background-color : lightpink")
        back_button.setStyleSheet(" color: black ; font-size : 16px ; background-color : lightpink")


        #button sizes
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
        self.table.setHorizontalHeaderLabels(["Cake ID", "Cake Name", "Customer Name", "Customer Phone No", "Weight", "Quantity", "Total Price"])
        right_layout.addWidget(self.table)
        header = self.table.horizontalHeader()
        header.setStyleSheet("background-color: lightblue;")

        # Create a spacer item and add it to the layout
        right_layout.addStretch()

        # Refresh Button
        refresh_button = QPushButton("Refresh")
        refresh_button.setFixedSize(120,30)
        right_layout.addWidget(refresh_button)
        refresh_button.setStyleSheet(" color: black ; font-size : 16px ; background-color : lightpink")


        main_layout.addLayout(right_layout)
        #update weigths
        self.update_sub_combo_box()

        add_button.clicked.connect(self.save)
        edit_button.clicked.connect(self.edit)
        refresh_button.clicked.connect(self.refresh)
        back_button.clicked.connect(self.back_to_cake_shop)

        #functons for buttons
    def save(self):
        data = database.fetch_cake()
        cake_name = self.cake_name_combo.currentText()
        cake_weight = float(self.weight_available_combo.currentText())
        
        for i in data:
            if cake_name == i[1] and cake_weight == i[4]:
                cake_id = i[0]
                price = i[6]

        data_customer = database.fetch_customer()
        customer_phone = int(self.customer_phone_edit.text())

        for i in data_customer:
            if customer_phone == i[5] :
                print('yessssssss')
                customer_name = i[1]
        print(data_customer)
        print(customer_phone)
        
        print ('dwddhdqhdqd',customer_name)

        quantity = int(self.cake_quantity_edit.text())
        total = quantity*price
        
        
        database.insert_order(cake_id,cake_name,customer_name,customer_phone,cake_weight,quantity,total)

        self.customer_phone_edit.clear()
        self.cake_quantity_edit.clear()
        self.refresh()

    def edit(self):
        pass

    def refresh(self):
        data = database.fetch_order()
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
        

    def update_sub_combo_box(self):
        data = database.fetch_cake()
        # Clear the sub combo box
        self.weight_available_combo.clear()

        # Get the current text of the main combo box
        main_text = self.cake_name_combo.currentText()

        # Populate sub combo box based on the main combo box selection
        weight = []
        quantity = []
        for i in data:
            if main_text == i[1] and i[5] != 0:
                weight.append(i[4])
                quantity.append(i[5])
        if quantity is None:
            self.weight_available_combo.addItems(["Not available"])
        else:
            weight_str = []
            for i in weight:
                weight_str.append(str(i)) 
            self.weight_available_combo.addItems(weight_str)
            




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrderDetailsApp()
    window.show()
    sys.exit(app.exec_())
