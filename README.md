# Cash Register Application (Django ORM)
Aadit Singla: 100906986
Pratham Patel: 100920625
Joao Pedro Minari Prates: 100903075

## Overview
This project implements a standalone version of the Cash Register Application using the Django Object Relational Mapper (ORM).  
Although Django is primarily a web framework, this assignment demonstrates how its ORM can be used without running a web server, allowing database functionality inside a local Python application.

The goal is to replicate the same functionality as the previous assignment but now using Django’s ORM for data storage and retrieval.

=========================================================================================

## Objectives
The following two aspects are implemented using the Django ORM framework:

1. Database Population: Populating the database with product UPC codes, names, and prices.  
2. Product Scanning: Scanning a product (via user input) and displaying its name and price if found in the database.

=========================================================================================

## Project Structure
- .github → GitHub Classroom files  
- db/ → Contains ORM model and migrations  
  - models.py → Defines Product model (upc, name, price)  
  - __init__.py → Marks db as a Python package  
  - migrations/ → Auto-generated Django migration files  
- .gitignore → Files to ignore in version control  
- db.sqlite3 → SQLite database file (already contains sample data and schema)  
- main.py → Main script (populates DB and scans products)  
- manage.py → Default Django management file  
- settings.py → Django ORM configuration (SQLite setup)  
- README.md → Project documentation  

======================================================================================

## Features Implemented

1. Database Population  
   - The Product model (in db/models.py) defines three fields:  
     - upc: Product UPC code  
     - name: Product name  
     - price: Product price  
   - The populate_products() function in main.py inserts predefined product entries into the database using Django ORM.

2. Product Scanning  
   - The user enters a product’s UPC code in the input box.  
   - The system searches for the product using:
         product = Product.objects.filter(upc=entered_upc).first()
   - If found, the program displays the product name and price.  
   - If not found, a message such as “Product not found” appears.


==============================================================================

## Setup Instructions

### Requirements
Before running the program, make sure the following are installed:
Python 3.x
Django
tkinter


### Steps to Run
1. Since the database (db.sqlite3) and migrations are already included, no migration steps are required.  
2. Simply run the program:
   python main.py

Expected behavior:

Uses the pre-populated database of sample products.
Allows scanning of products by UPC.
Displays the product name and price if found.

Use the following sample data for testing:
| UPC Code     | Product Name      | Price ($) |
| ------------ | ----------------- | --------- |
| 123456789012 | Milk              | 2.49      |
| 987654321098 | Bread             | 3.19      |
| 111111111111 | Eggs              | 4.79      |
| 222222222222 | Butter            | 5.25      |
| 333333333333 | Cheese            | 6.49      |
| 444444444444 | Apples (1 lb bag) | 3.99      |
| 555555555555 | Bananas (1 lb)    | 1.59      |
| 666666666666 | Orange Juice      | 4.29      |
| 777777777777 | Cereal            | 5.99      |
| 888888888888 | Toothpaste        | 2.89      |
| 999999999999 | Soap Bar          | 1.49      |
| 101010101010 | Shampoo           | 6.75      |


SCREEN DUMPS 
<img width="526" height="588" alt="image" src="https://github.com/user-attachments/assets/7233d747-ebde-4c47-b9da-6817f7e4f60b" />
<img width="515" height="594" alt="image" src="https://github.com/user-attachments/assets/88c58b1d-c006-40f1-9f5b-af606be667b8" />
<img width="520" height="594" alt="image" src="https://github.com/user-attachments/assets/0798d691-89fc-41c1-b001-04b07218483d" />



