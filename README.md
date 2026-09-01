# Student Record Management System

## Objective

This project is a simple Student Record Management System made using Python.

It stores student information and reads student records from TXT, CSV, and JSON files.

## Features

- Store student ID, name, department and semester
- Store marks of three subjects
- Calculate total marks
- Calculate average marks
- Check Pass or Fail
- Read TXT files
- Read CSV files
- Read JSON files
- Use command-line arguments

## Technologies Used

- Python
- CSV
- JSON
- Argparse
- Object-Oriented Programming
- 
## Project Structure

- student-record-system
  - student.py
  - manager.py
  - main.py
  - file_handler.py
  - data
    - students.txt
    - students.csv
    - students.json

## How to Run

For TXT:

python main.py --file data/students.txt --format txt

For CSV:

python main.py --file data/students.csv --format csv

For JSON:

python main.py --file data/students.json --format json

## Sample Data

The project contains 5 student records.
