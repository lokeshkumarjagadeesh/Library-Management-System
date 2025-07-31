
#  Library Management System

A simple and interactive command-line Library Management System built using **Python** and **MySQL**. This system helps manage books, members, and borrowing activities efficiently. It also supports importing books from CSV and tracking overdue or returned books.

##  Technologies Used

- **Programming Language:** Python  
- **Database:** MySQL  
- **Libraries:** `mysql-connector-python`, `csv`, `datetime`

##  Key Features

- Add, view, search, and delete books
- Add and view members
- Borrow and return books with date validation
- Track overdue and returned books
- Import book data directly from a CSV file
- Command-line menu interface for smooth user interaction

##  Database Structure

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

##  How It Works

1. **Start the program**: The menu-driven CLI lets you navigate through various features.
2. **Book Management**: Add, view, search by title, delete books, and import from CSV.
3. **Member Management**: Add and view registered members.
4. **Borrowing System**: Issue books and return them with dates tracked.
5. **Tracking Tools**: Monitor overdue and returned books with easy reports.


##  How to Run

1. Ensure MySQL is running and a database is created.
2. Install `mysql-connector-python` if not already:
   
   `
   pip install mysql-connector-python
   `
3. Run the Python script (`.py`) and follow the CLI menu.

---

##  Screenshots 
