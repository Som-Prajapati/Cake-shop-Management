
# APPLICATION GUI
import customer_details,cakedetails,profit_page,order,database
import sys
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import *
class CakeShopHome(QWidget):

    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MERWANS - Home")
        self.setGeometry(0, 0, 400, 400)  
        self.initUI()
        self.resize(600, 400) 
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        center_p = screen.center()
        window.moveCenter(center_p)
        self.setGeometry(window)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(173, 216, 230))
        self.setPalette(palette)
    
    def initUI(self):
        layout = QGridLayout()

        btn_new_customer = QPushButton("New Customer")
        btn_new_customer.clicked.connect(self.new_customer)
        btn_new_customer.setFixedSize(200, 50)
        btn_new_customer.setStyleSheet("background-color: pink; color: black ; font-size : 18px")
        layout.addWidget(btn_new_customer, 0, 0)

        btn_book_cake = QPushButton("Book Cake")
        btn_book_cake.clicked.connect(self.book_cake)
        btn_book_cake.setFixedSize(200, 50)  
        btn_book_cake.setStyleSheet("background-color: pink; color: black ; font-size : 18px")
        layout.addWidget(btn_book_cake, 1, 0)

        btn_cake_details = QPushButton("Cake Details")
        btn_cake_details.clicked.connect(self.cake_details)
        btn_cake_details.setFixedSize(200, 50) 
        btn_cake_details.setStyleSheet("background-color: pink; color: black ; font-size : 18px") 
        layout.addWidget(btn_cake_details, 0,1)

        btn_profit_details = QPushButton("Profit Details")
        btn_profit_details.clicked.connect(self.profit_details)
        btn_profit_details.setFixedSize(200, 50) 
        btn_profit_details.setStyleSheet("background-color: pink; color: black ; font-size : 18px")
        layout.addWidget(btn_profit_details, 1, 1)

        self.setLayout(layout)

    def show_cake_shop_customer(self):
        self.window_customer.close()
        window.show()

    def show_cake_shop_cake(self):
        self.window_cake.close()
        window.show()

    def show_cake_shop_book(self):
        self.window_book.close()
        window.show()

    def show_cake_shop_profit(self):
        self.window_profit.close()
        window.show()

        
    def new_customer(self):
        window.hide()
        self.window_customer = customer_details.CustomerDetailsApp()    
        self.window_customer.show()
        self.window_customer.back_clicked.connect(self.show_cake_shop_customer)
        print("New Customer button clicked")


    def book_cake(self):
        window.hide()
        self.window_book = order.OrderDetailsApp()    
        self.window_book.show()
        self.window_book.back_clicked.connect(self.show_cake_shop_book)
        print("order button clicked")

    def cake_details(self):
        window.hide()
        self.window_cake = cakedetails.CakeDetailsApp()    
        self.window_cake.show()
        self.window_cake.back_clicked.connect(self.show_cake_shop_cake)
        print("New Customer button clicked")

    def profit_details(self):
        window.hide()
        self.window_profit = profit_page.ProfitPageApp()    
        self.window_profit.show()
        self.window_profit.back_clicked.connect(self.show_cake_shop_profit)
        print("New Customer button clicked")

    def back_customer():
        window.show()

class LoginWindow(QWidget):

    
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MERWANS - LOGIN PAGE")
        self.resize(550, 270) 
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


        final_layout = QVBoxLayout()
        layout = QGridLayout()

        
        
    


        self.e_label = QLabel("")
        self.e_label2 = QLabel("")
        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet("font-size: 14pt")
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("background-color: lightGray")
        self.username_input.setFixedSize(200,30)

        layout.addWidget(self.username_label,0,1)
        layout.addWidget(self.username_input,0,2)
        layout.addWidget(self.e_label,0,4)
        layout.addWidget(self.e_label,0,0)

        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("font-size: 14pt")
        self.password_input = QLineEdit()
        self.password_input.setFixedSize(200,30)
        self.password_input.setStyleSheet("background-color: lightGray")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label,1,1)
        layout.addWidget(self.password_input,1,2)

        
        self.login_button = QPushButton("Login")
        self.login_button.setFixedSize(150,40)
        self.login_button.setStyleSheet("background-color: pink; color: black ; font-size : 20px")
        
        self.login_button.clicked.connect(self.login)

        vertical = QHBoxLayout()
        vertical.addWidget(self.login_button)
        final_layout.addLayout(layout)
        final_layout.addLayout(vertical)
        
        self.setLayout(final_layout)
        

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Dummy login validation
        if username == "som" and password == "somharsh":
            QMessageBox.information(self, "Login Successful", "Welcome, " + username + "!")
            login_window.hide()
            window.show()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")



if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = CakeShopHome()
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())


    
