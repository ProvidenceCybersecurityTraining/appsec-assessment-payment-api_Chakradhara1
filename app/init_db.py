import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("payments.db")
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS payments")

# Create users table
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    role TEXT
)
""")

# Create payments table
cursor.execute("""
CREATE TABLE payments (
    id INTEGER PRIMARY KEY,
    username TEXT,
    amount INTEGER,
    status TEXT
)
""")

# Insert data into users table
cursor.execute("INSERT INTO users VALUES (1, 'admin', 'Admin@123', 'admin')")
cursor.execute("INSERT INTO users VALUES (2, 'alice', 'Alice@123', 'user')")
cursor.execute("INSERT INTO users VALUES (3, 'bob', 'Bob@123', 'user')")

# Insert data into payments table
cursor.execute("INSERT INTO payments VALUES (1, 'alice', 5000, 'processed')")
cursor.execute("INSERT INTO payments VALUES (2, 'bob', 7500, 'pending')")
cursor.execute("INSERT INTO payments VALUES (3, 'admin', 99999, 'approved')")

# Commit changes and close connection
conn.commit()
conn.close()

print("Database initialized successfully")