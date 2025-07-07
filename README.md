
# 🧁 Cake Shop Management System

## 📝 Project Description

The **Cake Shop Management System** is a desktop-based Python application developed to assist cake shop owners in maintaining a structured and digital record of cake-related data. The system aims to replace inefficient manual methods of record-keeping with a user-friendly interface that allows smooth data entry, editing, and real-time access to inventory information. Through its well-structured design, the system reduces data inconsistency, minimizes human error, and enhances operational efficiency. It ...

## 🎯 Problem Statement

Traditional cake shops often face challenges such as:

- Inaccurate or lost records  
- Manual computation errors in pricing and stock  
- No centralized database to track all cake information  
- Time-consuming tracking of stock availability and profits  

**This system addresses these issues by:**

- Providing a digital interface for structured data entry  
- Enabling persistent storage through MongoDB  
- Supporting features like add, edit, refresh, and navigation  
- Ensuring seamless inventory and record management  

## 🛠️ Tools & Technologies Used

| Category         | Tool / Technology              |
|------------------|--------------------------------|
| Programming      | Python                         |
| GUI Library      | PyQt5 (QtWidgets, QtCore, QtGui)|
| Database         | MongoDB (with PyMongo)         |
| Version Control  | Git & GitHub                   |
| Platform         | Desktop Application            |

## 🔧 Module Overview & Functions

### 📍 1. Main GUI (`CakeDetailsApp`)

Responsible for the main user interface that handles cake-related operations.

**Features:**

- **Cake Name Field** – Input field for entering cake name  
- **Egg/Eggless Option** – Radio buttons to select if the cake contains egg  
- **Cake Description** – Multi-line text input for cake details  
- **Weight Dropdown** – Dropdown list to choose cake weight (0.5 to 3 kg)  
- **Quantity Field** – Input field to specify quantity available  
- **Price Field** – Input field to enter price per unit  
- **Cake Table View** – Displays all cake records from the database  
- **Dynamic UI Design** – Auto-resizes and color-coded interface with PyQt5 palette customization  

### 📍 2. Database Module (`database.py`)

Handles all MongoDB database interactions using `pymongo`.

**All Functions:**

- `insert_cake(name, egg, description, weight, quantity, price)`  
  Inserts a new cake record into MongoDB  
- `fetch_cake()`  
  Retrieves all cake documents and returns as a list  
- `update_cake(id, new_data)`  
  Updates an existing cake document based on its ID  
- `delete_cake(id)`  
  Deletes a specific cake record by ID  
- `connect_to_db()`  
  Establishes and returns the MongoDB connection  

### 📍 3. Button Functions in Main UI

**All Buttons & Their Roles:**

- **Add** – Inserts new cake data into the database after form validation  
- **Edit** – (Function placeholder) Intended to update existing cake records  
- **Back** – Emits a custom signal (`back_clicked`) to return to the main/home window  
- **Refresh** – Re-fetches data from the database and updates the table  

### 📍 4. Other Modules

- **`customer_details.py`** – Manages customer-related data (name, contact, orders placed)  
- **`order.py`** – Handles customer orders and total price calculations  
- **`profit_page.py`** – Displays total profit based on quantity sold and price  
- **`main.py` (if present)** – Launches the application and handles navigation between modules  

## ✅ Features Summary

- Add New Cakes with Details  
- Egg/Eggless Option with Radio Buttons  
- Store and View Cake Inventory  
- Refresh Table to See Live Changes  
- MongoDB Integration for Persistent Storage  
- Modular Python Code for Scalability  
- Responsive GUI with PyQt5 Layouts and Styling  
- Navigation with Signal Handling  

## 📌 Conclusion

The **Cake Shop Management System** offers a powerful, modular, and intuitive solution to streamline cake inventory management. Built using Python, PyQt5, and MongoDB, it provides real-time access to cake records, a smooth graphical interface, and efficient database interactions. This system reduces manual workload, ensures data accuracy, and improves shop operations. It reflects best practices in software development, modularity, and UI/UX design — making it ideal for real-world deployment in local cake ...
