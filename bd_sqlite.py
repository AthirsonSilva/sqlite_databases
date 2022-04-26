import sqlite3

connection = sqlite3.connect('../database.sqlite')
cursor = connection.cursor()

# Creating clients database
# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS client (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,name TEXT NOT NULL,weight REAL NOT NULL)')
# # Inserting values
# cursor.execute(
#     'INSERT INTO client (name, weight) VALUES (?, ?)', ('Brabo', 75))
# cursor.execute('INSERT INTO client (name, weight) VALUES (:name, :weight)', {
#                'name': 'Dummy name', 'weight': 69})

# # Updating values
# cursor.execute(
# 		'UPDATE client SET weight=:weight WHERE id=:id',
# 		{'weight': 50, 'id': 2}
# 	)

# # Delete stuff
# cursor.execute(
# 		'DELETE FROM client WHERE id=:id',
# 		{'id': 2}
# 	)

# Commiting changes
connection.commit()

# Selecting data from table
cursor.execute('SELECT * FROM client')

# Fetching info
for line in cursor.fetchall():
    print(line)

cursor.close()
connection.close()
