import sqlite3 as sql


class DbActions:
    def __init__(self):
        self.conn = sql.connect('DB/db.db')
        self.cursor = self.conn.cursor()

    # Insert user to database
    def insertUser(self, name, password):
        self.cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
        self.conn.commit()
        self.conn.close()

    # Get user from database
    def getUser(self, name):
        self.cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        return self.cursor.fetchone()

    # Update user permissions
    def updateUser(self, name, permission):
        self.cursor.execute("UPDATE users SET permission = ? WHERE name = ?", (permission, name))
        self.conn.commit()
        self.conn.close()
