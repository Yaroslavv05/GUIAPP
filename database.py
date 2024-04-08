import sqlite3

'''
Код створює клас Database, який використовується для роботи з базою даних SQLite. Він має методи для створення таблиці, 
вибірки всіх даних, отримання останнього ідентифікатора, вставки нових даних та очищення таблиці.
'''

class Database:
    def __init__(self, db_name='calculations.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS calculations (
                                id INTEGER PRIMARY KEY,
                                side_a REAL,
                                side_b REAL,
                                figure TEXT,
                                area REAL,
                                count_figures INTEGER)''')
        self.connection.commit()

    def fetch_all(self):
        self.cursor.execute('''SELECT * FROM calculations''')
        return self.cursor.fetchall()

    def get_last_id(self):
        self.cursor.execute('''SELECT MAX(id) FROM calculations''')
        last_id = self.cursor.fetchone()[0]
        return last_id if last_id is not None else 0

    def insert_data(self, side_a, side_b, figure, area, count_figures):
        self.cursor.execute('''INSERT INTO calculations (id, side_a, side_b, figure, area, count_figures)
                                VALUES (?, ?, ?, ?, ?, ?)''', (self.get_last_id() + 1, side_a, side_b, figure, area, count_figures))
        self.connection.commit()

    def clear_table(self):
        self.cursor.execute('''DELETE FROM calculations''')
        self.connection.commit()
