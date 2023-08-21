import sqlite3 as sql


class DbActions:
    def __init__(self):
        self.conn = sql.connect('DB/db')
        self.cursor = self.conn.cursor()

    # Insert user to database
    def insertUser(self, name, password, permission):
        self.cursor.execute("INSERT INTO users (name, password, permission) VALUES (?, ?, ?)",
                            (name, password, permission))
        self.conn.commit()
        self.conn.close()

    # Get user from database
    def getUser(self, name):
        self.cursor.execute("SELECT * FROM Users WHERE name = ?", (name,))
        return self.cursor.fetchone()

    def getUserPermission(self, name):
        self.cursor.execute("SELECT permission FROM Users WHERE name = ?", (name,))
        return self.cursor.fetchone()

    # Update user permissions
    def updateUser(self, name, permission):
        self.cursor.execute("UPDATE users SET permission = ? WHERE name = ?", (permission, name))
        self.conn.commit()
        self.conn.close()
