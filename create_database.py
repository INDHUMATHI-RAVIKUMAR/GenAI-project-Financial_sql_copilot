import sqlite3

connection = sqlite3.connect("financial_data.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS financial_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    quarter TEXT,
    department TEXT,
    revenue REAL,
    expenses REAL,
    profit REAL
)
""")

data = [
    (2024, "Q1", "Sales", 1200000, 800000, 400000),
    (2024, "Q2", "Sales", 1350000, 850000, 500000),
    (2024, "Q3", "Sales", 1500000, 900000, 600000),
    (2024, "Q4", "Sales", 1700000, 1000000, 700000),

    (2025, "Q1", "Sales", 1800000, 1050000, 750000),
    (2025, "Q2", "Sales", 1950000, 1100000, 850000),
    (2025, "Q3", "Sales", 2100000, 1200000, 900000),
    (2025, "Q4", "Sales", 2300000, 1300000, 1000000),

    (2024, "Q1", "Marketing", 500000, 300000, 200000),
    (2024, "Q2", "Marketing", 550000, 320000, 230000),
    (2024, "Q3", "Marketing", 600000, 350000, 250000),
    (2024, "Q4", "Marketing", 650000, 370000, 280000),

    (2025, "Q1", "Marketing", 700000, 400000, 300000),
    (2025, "Q2", "Marketing", 750000, 420000, 330000),
    (2025, "Q3", "Marketing", 800000, 450000, 350000),
    (2025, "Q4", "Marketing", 850000, 470000, 380000)
]

cursor.executemany("""
INSERT INTO financial_data
(year, quarter, department, revenue, expenses, profit)
VALUES (?, ?, ?, ?, ?, ?)
""", data)

connection.commit()
connection.close()

print("Database created successfully!")