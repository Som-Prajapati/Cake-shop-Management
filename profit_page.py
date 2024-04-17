import sys,database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QPalette
import cakedetails,profit_page,customer_details
from PyQt5.QtCore import *


class ProfitPageApp(QWidget):

    back_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Profit Page")
        self.setGeometry(100, 100, 400, 300)
        self.resize(600, 400) 
        self.center()
        self.initUI()

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

    def back_to_cake_shop(self):
        # Emit the back_clicked signal when the back button is clicked
        print('back button clicked')
        self.back_clicked.emit()
        
    def initUI(self):
        main_layout = QGridLayout(self)

        total_cakes,remaining_cakes,sold_cakes,profit =  self.calculator()
        # Display Labels
        total_cakes_label = QLabel(f"Total Cakes: {total_cakes}")
        remaining_cakes_label = QLabel(f"Remaining Cakes: {remaining_cakes}")
        sold_cakes_label = QLabel(f"Sold Cakes: {sold_cakes}")
        total_profit_label = QLabel(f"Total Profit Gained: {profit}")

        #display size
        total_cakes_label.setStyleSheet("font-size: 18pt")
        remaining_cakes_label.setStyleSheet("font-size: 18pt")
        sold_cakes_label.setStyleSheet("font-size: 18pt")
        total_profit_label.setStyleSheet("font-size: 18pt")

        # Add Labels to Layout
        main_layout.addWidget(total_cakes_label, 0, 0)
        main_layout.addWidget(remaining_cakes_label, 1, 0)
        main_layout.addWidget(sold_cakes_label, 1, 2)
        main_layout.addWidget(total_profit_label, 3, 0)


        # back butt added
        back_button = QPushButton("Back")
        back_button.setFixedSize(120,30)
        back_button.setStyleSheet(" color: black ; font-size : 16px  ; background-color : lightpink")
        back_button.clicked.connect(self.back_to_cake_shop)
        main_layout.addWidget(back_button, 4, 0)
        
        self.setLayout(main_layout)

    def calculator(self):
        cake_data = database.fetch_cake()
        order_data = database.fetch_order()
        
        
        total_cakes = 0
        for i in cake_data:
            total_cakes += i[5]

        profit = 0
        sold_cakes = 0
        for i in order_data:
            sold_cakes += i[5]
            profit += i[6]

        remaining_cakes = total_cakes - sold_cakes
        return total_cakes,remaining_cakes,sold_cakes,profit

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfitPageApp()
    window.show()
    sys.exit(app.exec_())
