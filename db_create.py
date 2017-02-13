import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as conn:

	c = conn.cursor()

	c.execute("""
		CREATE TABLE tasks
		(
			task_id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL, 
			due_date TEXT NOT NULL, 
			priority INTEGER NOT NULL,
			status INTEGER NOT NULL
		)
	""")

	c.execute("""
		INSERT INTO tasks (name, due_date, priority, status)
		VALUES("Go do something fun", "03/25/2015", 10, 1)
	""")

	c.execute("""
		INSERT INTO tasks (name, due_date, priority, status)
		VALUES("Take dog to vet", "03/10/2015", 10, 1)
	""")