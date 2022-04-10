import sqlite3

class NounDB:
	"""Simple CRUD with SQLITE"""
	def __init__(self, file):
		self.conn = sqlite3.connect(file)
		self.cursor = self.conn.cursor()

	# Inserting values
	def insert(self, name, phone):
		consult = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
		self.cursor.execute(consult, (name, phone))
		self.conn.commit()

	# Updating values
	def edit(self, name, phone, id):
		consult = 'UPDATE OR IGNORE agenda SET nome=?, telefone=?, WHERE id=?'
		self.cursor.execute(consult, (name, phone, id))
		self.conn.commit()

	# Deleting values
	def delete(self, id):
		consult = 'DELETE FROM agenda WHERE id=?'
		self.cursor.execute(consult, (id))
		self.conn.commit()

	# Listing and viewing values
	def list(self):
		self.cursor.execute('SELECT * FROM agenda')

		# Interating on table rows
		for line in self.cursor.fetchall():
			print(line)

	# Searching engine
	def search(self, value):
		consult = 'SELECT * FROM agenda WHERE nome LIKE ?'
		self.cursor.execute(consult, (f'%{value}%',))

		# Interating on the table searching for the value
		for line in self.cursor.fetchall():
			print(line)

	# Closing database
	def close(self):
		self.cursor.close()
		self.conn.close()

# Class instance
if __name__ == '__main__':
	agenda = NounDB('agenda.db')
	agenda.insert('Athirson Silva', 60)
	agenda.list()