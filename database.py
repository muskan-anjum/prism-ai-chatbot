import sqlite3

DATABASE_NAME = "leads.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            requirement TEXT NOT NULL,
            budget TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_lead(name, phone, email, requirement, budget):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO leads (name, phone, email, requirement, budget)
        VALUES (?, ?, ?, ?, ?)
    """, (name, phone, email, requirement, budget))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    print("Lead database created successfully.")