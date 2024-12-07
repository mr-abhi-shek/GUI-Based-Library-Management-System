
# Library Management System

This project is a Library Management System built using Python and customtkinter for the GUI. It allows for managing books, members, and library transactions.

## Requirements and Installation

### 1. Install Required Libraries

Make sure you have Python installed on your machine. Then, install the required libraries by running:

```bash
pip install customtkinter mysql-connector-python pillow
```

### 2. Setting Up the MySQL Database

1. **Open MySQL** on your local machine and log in to your MySQL shell.
2. **Create a database** for the Library Management System:

    ```sql

    	CREATE DATABASE library_database;
	USE library_database;

    ```

3. **Set Up Tables**: Below is the specific structure for the 'books' table provided:

    - **Books Table**:

        ```sql

CREATE TABLE books (
    Title VARCHAR(30) NOT NULL,
    Author VARCHAR(30) NOT NULL,
    Publisher VARCHAR(30) NOT NULL,
    Publication_Date DATE NOT NULL,
    Genre VARCHAR(30) NOT NULL,
    Language VARCHAR(30) NOT NULL,
    Number_of_Pages INT NOT NULL,
    Edition VARCHAR(30) NOT NULL,
    Number_of_Books INT NOT NULL,
    Price INT NOT NULL,
    Book_ID VARCHAR(15) PRIMARY KEY,
    Cover_Image VARCHAR(255) NOT NULL
);

        ```

    - **profiles Table**:

        ```sql

CREATE TABLE profiles (
    Member_ID VARCHAR(15) PRIMARY KEY,
    Password VARCHAR(15) NOT NULL,
    Role VARCHAR(6),
    Name VARCHAR(30),
    Contact_Number BIGINT,
    Email VARCHAR(20),
    DOB DATE,
    Communication_Address VARCHAR(30),
    Registration_Date DATE,
    profile_image VARCHAR(255),
    gender VARCHAR(10) NOT NULL,
    Occupation VARCHAR(20) NOT NULL
);

        ```

    - **books_issue Table**:

        ```sql

CREATE TABLE books_issue (
    member_id VARCHAR(15),
    book_id VARCHAR(15),
    Issue_Date DATE,
    Due_Date DATE,
    Status VARCHAR(50),
    Token_Number VARCHAR(15) PRIMARY KEY,
    return_date VARCHAR(15)
);

        ```

4. **Database Configuration in the Project**: Ensure that the database connection details (host, user, password, database) in your project files match your MySQL setup.

## Running the Project

After completing the steps above, you can run the project by executing:

```bash
python Admin_Dashboard.py
```

This command will open the main dashboard window of the Library Management System.

---

## Additional Notes

- Ensure that the image paths in the database are correctly set to display cover images.
- Icons and images are located in the `icon` folder.
- The structure of additional features can be modified as per the project's requirements.

---
