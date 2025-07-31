
# 📚 Library Management System

A simple and interactive command-line Library Management System built using **Python** and **MySQL**. This system helps manage books, members, and borrowing activities efficiently. It also supports importing books from CSV and tracking overdue or returned books.

## 🛠 Technologies Used

- **Programming Language:** Python  
- **Database:** MySQL  
- **Libraries:** `mysql-connector-python`, `csv`, `datetime`

## 🔑 Key Features

- Add, view, search, and delete books
- Add and view members
- Borrow and return books with date validation
- Track overdue and returned books
- Import book data directly from a CSV file
- Command-line menu interface for smooth user interaction

## 🗂️ Database Structure

- **Books**
  - `book_id` (Primary Key)
  - `title`, `author`, `price`, `status`

- **Members**
  - `member_id` (Primary Key)
  - `name`, `email`

- **Borrow**
  - `borrow_id` (Primary Key)
  - `book_id` (Foreign Key)
  - `member_id` (Foreign Key)
  - `borrow_date`, `return_date`

## ⚙️ How It Works

1. **Start the program**: The menu-driven CLI lets you navigate through various features.
2. **Book Management**: Add, view, search by title, delete books, and import from CSV.
3. **Member Management**: Add and view registered members.
4. **Borrowing System**: Issue books and return them with dates tracked.
5. **Tracking Tools**: Monitor overdue and returned books with easy reports.

## 🧪 Sample SQL Commands

```sql
CREATE DATABASE library_management_system;
USE library_management_system;

CREATE TABLE books (
  book_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100),
  author VARCHAR(100),
  price DECIMAL(8,2),
  status VARCHAR(20) DEFAULT 'available'
);

CREATE TABLE members (
  member_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  email VARCHAR(100)
);

CREATE TABLE borrow (
  borrow_id INT PRIMARY KEY AUTO_INCREMENT,
  book_id INT,
  member_id INT,
  borrow_date DATE,
  return_date DATE,
  FOREIGN KEY (book_id) REFERENCES books(book_id),
  FOREIGN KEY (member_id) REFERENCES members(member_id)
);
```

## 📁 CSV File Format

Sample `Books.csv`:
```csv
title,author,price
Python Basics,John Doe,299.99
Data Science 101,Jane Smith,399.50
```

## ✅ How to Run

1. Ensure MySQL is running and a database is created.
2. Install `mysql-connector-python` if not already:
   ```bash
   pip install mysql-connector-python
   ```
3. Run the Python script (`.py`) and follow the CLI menu.

---
