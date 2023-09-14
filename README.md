# Python SQLite Student Database

## Description

This project is a simple Python program that interacts with a SQLite database to manage student records. It creates a table for student information, inserts data, performs queries, updates grades, and deletes records. It serves as a basic example of using SQLite in Python.

## Installation

To run this project locally, you'll need Python and the SQLite library installed on your system. 
Then you will need to follow these steps:

1. Navigate to your desired directory using the `cd` command:

   ```bash
   cd C:\Users\user\work_folder_location

1. Clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/FinnlyFox/SQLite3-showcase.git

1. Navigate to the project folder using the `cd` command:

   ```bash
   cd SQLite3-showcase

1. Then run the program

   ```bash
   python database_manip.py

## Usage

Please note, before running the program that you have accurately changed the path of the db variable to fit your file system

After you have successfully installed and run the program, it will do the following and print the results of each action to the screen:

1. #### Create Table: The program creates an SQLite table named python_programming to store student information.

1. #### Insert Data: It inserts sample student data into the table.

1. #### Query Data: You can retrieve data for students with grades between 60 and 80.

1. #### Update Grade: The program allows you to update the grade of a specific student. For example, it updates the grade for 'Carl Davis' to 65.

1. #### Delete Record: It deletes a specific student record. In this example, it deletes the record for 'Dennis Fredrickson'.

1. #### Update Grades: The program updates the grades of students with IDs less than 55 to 100.

1. #### Drop Table: Finally, the program drops the python_programming table.

## Credits
This project was created by Joel Whyle.
