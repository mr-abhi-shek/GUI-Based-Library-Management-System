# GUI Based Library Management System

## 📚 Project Overview

The **Library Management System** is a GUI-based application developed using Python and MySQL. It simplifies library operations by allowing users to manage books, members, and transactions efficiently. The system includes features for adding, editing, deleting, searching, and managing book and member records, along with issuing and returning books.

## ✨ Features

- **Book Management:** Add, edit, delete, and search books with detailed information like title, author, genre, and more.
- **Member Management:** Register, update, delete, and search member profiles.
- **Issue & Return:** Handle book issuance and returns with transaction records.
- **User Roles:** Support for admin roles to manage the system.
- **Interactive Dashboard:** View and manage all system activities from a central dashboard.

## 🖼️ Screenshots

| **Login Window** | **Admin Dashboard** |
|-------------------|----------------------|
| ![Login](screenshots/login_window.png) | ![Dashboard](screenshots/admin_dashboard.png) |

| **Add Book** | **Update Book** |
|--------------|------------------------|
| ![Add Book](screenshots/add_book.png) | ![Update Book](screenshots/update_book.png) |

| **Delete Book** | **Search Book** |
|--------------|------------------------|
| ![Add Book](screenshots/delete_book.png) | ![Update Book](screenshots/search_book.png) |

| **Add Member** | **Update Member** |
|--------------|------------------------|
| ![Add Book](screenshots/add_member.png) | ![Update Book](screenshots/update_member.png) |

| **Delete Member** | **Search Member** |
|--------------|------------------------|
| ![Delete Member](screenshots/delete_member.png) | ![Search Member](screenshots/search_member.png) |

| **Issue Book** | **Return Book** |
|--------------|------------------------|
| ![Issue Book](screenshots/issue_book.png) | ![Return Book](screenshots/return_book.png) |


## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mr-abhi-shek/GUI-Based-Library-Management-System.git
   
2. Navigate to the project directory:
   ```bash
   cd GUI-Based-Library-Management-System

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt

4. Set up the MySQL database:
   -Create a database named library_database.
   -Import the provided SQL dump file to set up tables.

5. Run the application:
   ```bash
   python Login_Activity.py

🚀 Usage
Login: Enter admin credentials to access the system.
Dashboard: Navigate through the features to manage books, members, and transactions.
Logout: Securely log out after use.


## 🗂️ Folder Structure

Library-Management-System/
├── Add_Book_Window.py
├── Add_Member_Window.py
├── Admin_Dashboard.py
├── Delete_Book_Window.py
├── Delete_Member_Window.py
├── Edit_Book_Window.py
├── Edit_Member_Window.py
├── icon/
├── Issue_Book_Window.py
├── Login_Activity.py
├── Populate_Member_Info.py
├── README.md
├── Return_Book_Window.py
├── Search_Book_Window.py
├── Search_Member_Window.py
├── requirements.txt
├── useable_module.py
└── screenshots/
