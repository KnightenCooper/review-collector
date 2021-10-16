# Overview

My goal with this program was to gain an understanding of how to use sqlite3 to create a database that is used by a Python review application. I am currently a 
software engineering student and wanted to deepen my knowledge of Python and databases.

This software is linked to a single database called data. The database has a table that stores a review's primary key, title, description, and a integer rating. 
My program integrates with a SQL relational database using sqlite3. Users of my program can insert, modify, delete, get statistics, and view all the reviews within 
the database. The statistics the user can access are the average rating, smallest rating, and largest rating. 

The user interacts with my program by using a commandline interface. The program asks the user to type 'i' to a insert review, 'm' to modify a review, 'd' to delete 
a review, 'r' to retrieve all reviews, 's' to view statistics, and 'end' to end the program. Depending on what the user inputs, the program will then ask for the 
necessary inputs to accomplish the selected task. If the user picks delete a review, then the program will display all reviews with their primary keys and prompt the user to input the
primary key of the review they want deleted.

[Software Demo Video](http://youtu.be/a16IqWIB_10?hd=1)

# Relational Database

The database I am using is created by my program and saved locally. The database is called data and interacts with the python application using the sqlite3 module.

The structure of the database is very simple. The reviews database contains a single table called reviews. The reviews table has 4 columns. The first 
column is the primary key. The second column is the title of the review. The third column is the description of the review. The fourth column is the rating of the review.
All the data is text except the rating and the primary key are both numbers. 

# Development Environment

The tools I am using to develop this software are VS Code run on a Windows machine.

I used the Python programming language with sqlite3 and sys imported. I used sqlite3 to interact with the database and sys to end the program.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [SQLite Tutorial](https://www.sqlitetutorial.net)
* [Python Documentation](https://docs.python.org/3.8/library/sqlite3.html)
* [Tutorials Point](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

# Future Work

* I would love to add an actual GUI. Interacting with the database using the commandline works, but isn't very user friendly.
* I would like to add more tables to the database. I think it would be amazing if each review was linked to a business, or if this software was applied to a marketplace.
* I would like to connect this to a webpage that allows users to leave reviews on products and connects with a login to identify who is leaving the review.
