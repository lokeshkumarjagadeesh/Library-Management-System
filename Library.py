import mysql.connector
import csv
from datetime import datetime
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="library_management_system")
cursor = conn.cursor()
def add_books():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    price = float(input("Enter book price: "))
    cursor.execute("insert into books (title, author, price) values (%s, %s, %s)", (title, author, price))
    conn.commit()
    print("Book added successfully.")
def view_books():
    cursor.execute("select * from books")
    for book in cursor.fetchall():
        print(book)
def import_from_csv():
    try:
        with open("D:/Library management system/Books.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                title, author, price = row[0], row[1], float(row[2])
                cursor.execute("insert into books (title, author, price) values (%s, %s, %s)", (title, author, price))
            conn.commit()
            print("Books imported from CSV successfully.")
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"Error occurred: {e}")
def add_members():
    name = input("Enter member name: ")
    email = input("Enter email address: ")
    cursor.execute("insert into members (name, email) values (%s, %s)", (name, email))
    conn.commit()
    print("Member added successfully.")
def view_members():
    cursor.execute("select * from members")
    for member in cursor.fetchall():
        print(member)
def search_books_by_title():
    keyword = input("Enter title or part of it to search: ")
    query = "select * from books where title like %s"
    cursor.execute(query, ('%' + keyword + '%',))
    results = cursor.fetchall()
    if results:
        print("\nMatching books:")
        for book in results:
            print(book)
    else:
        print("No books found with that title.")
def borrow_books():
    view_members()
    member_id = int(input("Enter member ID: "))
    view_books()
    book_id = int(input("Enter book ID: "))
    cursor.execute("""
        select * from borrow 
        where book_id = %s and curdate() <= return_date
    """, (book_id,))
    if cursor.fetchone():
        print("Book is currently borrowed and not yet returned.")
        return
    borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
    return_date = input("Enter return date (YYYY-MM-DD): ")

    borrow_date_obj = datetime.strptime(borrow_date, "%Y-%m-%d").date()
    return_date_obj = datetime.strptime(return_date, "%Y-%m-%d").date()
    if return_date_obj < borrow_date_obj:
        print("Return date cannot be before borrow date.")
        return

    cursor.execute("""
        insert into borrow (book_id, member_id, borrow_date, return_date)
        values (%s, %s, %s, %s)
    """, (book_id, member_id, borrow_date_obj, return_date_obj))
    conn.commit()
    print("Book borrowed successfully.")

def view_borrowed_books():
    cursor.execute("""
        select b.borrow_id, m.name, bk.title, b.borrow_date, b.return_date
        from borrow b
        join members m on b.member_id = m.member_id
        join books bk on b.book_id = bk.book_id
    """)
    for record in cursor.fetchall():
        print(record)
def track_overdue_books():
    today = datetime.today().date()
    cursor.execute("select borrow_id, book_id, member_id, return_date from borrow where return_date < %s", (today,))
    overdue = cursor.fetchall()
    if overdue:
        print("\nOverdue books:")
        for entry in overdue:
            print(f"Borrow ID: {entry[0]}, Book ID: {entry[1]}, Member ID: {entry[2]}, Due: {entry[3]}")
    else:
        print("No overdue books found.")
def delete_book():
    book_id = int(input("Enter book ID to delete: "))
    cursor.execute("delete from books where book_id = %s", (book_id,))
    conn.commit()
    print("Book deleted successfully.")
def return_books():
    borrow_id = int(input("Enter borrow ID for return: "))
    return_date = input("Enter actual return date (YYYY-MM-DD): ")
    cursor.execute("update borrow set return_date = %s where borrow_id = %s", (return_date, borrow_id))
    conn.commit()
    cursor.execute("select book_id from borrow where borrow_id = %s", (borrow_id,))
    book_id = cursor.fetchone()[0]
    cursor.execute("update books set status = 'available' where book_id = %s", (book_id,))
    conn.commit()
    print("Book returned successfully.")
def view_returned_books():
    cursor.execute("""
        select b.borrow_id, m.name, bk.title, b.borrow_date, b.return_date
        from borrow b
        join members m on b.member_id = m.member_id
        join books bk on b.book_id = bk.book_id
        where b.return_date is not null
    """)
    returned = cursor.fetchall()
    print("Returned books:")
    for entry in returned:
        print(f"Borrow ID: {entry[0]}, Member: {entry[1]}, Book: {entry[2]}, Borrowed: {entry[3]}, Returned: {entry[4]}")
def main_menu():
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. View Books")
        print("3. Import Books from CSV")
        print("4. Add Member")
        print("5. View Members")
        print("6. Search Books by Title")
        print("7. Borrow Book")
        print("8. View Borrowed Books")
        print("9. Delete Book")
        print("10. Track Overdue Books")
        print("11. Return Book")
        print("12. View Returned Books")
        print("13. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_books()
        elif choice == '2':
            view_books()
        elif choice == '3':
            import_from_csv()
        elif choice == '4':
            add_members()
        elif choice == '5':
            view_members()
        elif choice == '6':
            search_books_by_title()
        elif choice == '7':
            borrow_books()
        elif choice == '8':
            view_borrowed_books()
        elif choice == '9':
            delete_book()
        elif choice == '10':
            track_overdue_books()
        elif choice == '11':
            return_books()
        elif choice == '12':
            view_returned_books()
        elif choice == '13':
            break
        else:
            print("Invalid choice. Please select a valid option.")

main_menu()
conn.close()
