"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='BETEP2112')

try:
    with conn:
        with open('north_data/employees_data.csv', 'r') as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for row in csvreader:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO employees (first_name, last_name, title, birth_date, notes)"
                    "VALUES (%s, %s, %s, %s, %s)",
                    (row[0], row[1], row[2], row[3], row[4])
                )

        with open('north_data/customers_data.csv', 'r') as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for row in csvreader:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                    (row[0], row[1], row[2])
                )

        with open('north_data/orders_data.csv', 'r') as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for row in csvreader:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)"
                    "VALUES (%s, %s, %s, %s, %s)",
                    (row[0], row[1], row[2], row[3], row[4])
                )

finally:
    conn.close()
