create database Library_Management_System;
use Library_Management_System;
create table Books (book_id int primary Key auto_increment,title varchar(100),author varchar(100),price decimal(8,2),status varchar(20) default 'available');
create table Members (member_id int primary Key auto_increment,name varchar(100),email varchar(100));
create table Borrow (borrow_id int primary Key auto_increment,book_id int,member_id int,borrow_date date,return_date date,foreign key (book_id) references books(book_id),foreign key (member_id) references members(member_id));
show databases;
desc Books;
select* from Books;
select* from Members;
select* from Borrow;
select* from Books where title="mithin";
SELECT b.borrow_id,m.name as member_name,bk.title as book_title,b.borrow_date,b.return_date from borrow b join members m on b.member_id = m.member_id join books bk on b.book_id = bk.book_id where b.return_date is not null; #view returned books 
select* from books where title like '%python%';
select* from books where status = 'available';
select* from books order by book_id desc limit 10;
select* from borrow where return_date is null or return_date >= CURDATE();  #not returned 
select borrow_id, book_id, member_id, return_date from borrow where return_date < CURDATE();  #overdue 
select  b.borrow_id, m.name as member_name, bk.title as book_title, b.borrow_date, b.return_date from borrow b join members m on b.member_id = m.member_id join books bk on b.book_id = bk.book_id where b.return_date < CURDATE(); #overdue to view full record 
select b.borrow_id, m.name as member_name, bk.title as book_title, b.borrow_date, b.return_date from borrow b join members m on b.member_id = m.member_id join books bk on b.book_id = bk.book_id where b.return_date is null or CURDATE() <= b.return_date; # not returned