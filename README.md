**This is a Teacher Management System using Python's Tkinter for the GUI and MySQL (via pymysql) as the database.**

Features of the Program :-

1) Add Teacher: Adds a teacher's details (UID, Name, Email, Contact, Subject) into the database.

2) Update Teacher: Updates an existing teacher's details.

3) Delete Teacher: Deletes a teacher’s record.

4) Clear Fields: Clears all input fields.

5) Search Teacher: Searches for teachers by UID or Name.

6) Display All Teachers: Fetches and displays all teacher records from the database.

7) Send Email: Sends an email to the selected teacher.

8) Navigation Between Pages: Switches between Manage Teacher and Search Teacher pages.

**Set Up MySQL Database**

Open MySQL and create a database called preexam:

CREATE DATABASE preexam;

**Create the teachers table:**

CREATE TABLE teachers (

    uid_no VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    contactno VARCHAR(15),
    subject VARCHAR(50)
);


**How the Program Works**
1) When you run the program, a GUI window opens.

2) You can add, update, delete, and search for teacher records.

3) Clicking "Next" switches to the Search Page.

4) Clicking "Back" switches back to the Manage Teacher Page.

5) Clicking "Send Mail" sends an email (you need to configure the sender email properly).

