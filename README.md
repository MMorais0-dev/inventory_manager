# Inventory Manager

A Python command-line app for managing product inventory. Built as a personal project while learning Python and preparing for a Home Depot software engineering internship.

## Features

- Add products with name, quantity, and price
- Adding an existing product increases its quantity instead of creating a duplicate
- Rejects invalid input (empty names, letters in number fields, negative values)
- View the full inventory with formatted prices
- Remove products by name (not case-sensitive)
- Saves to a CSV file after every change, so data is kept between sessions

## How to Run

1. Install Python 3
2. Clone the repository:
```
   git clone https://github.com/MMorais0-dev/inventory_manager.git
   cd inventory_manager
```
3. Run the app:
```
   python inventory.py
```

## Why I Built This

I work in Order Fulfillment at Home Depot and see every day how much accurate inventory matters to retail operations. I built this project to practice Python by solving a problem I deal with at work.

## What I Learned

- Python functions, loops, and dictionaries
- Reading and writing CSV files
- Validating user input and handling errors
- Git and GitHub version control

## Planned

- SKU numbers for each product
- Low-stock report
- A Java Spring Boot version with a PostgreSQL database