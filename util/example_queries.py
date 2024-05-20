import sqlite3

conn = sqlite3.connect(database='Database/MyClimb.db')
cursor = conn.cursor()

cursor.execute('''
UPDATE Climbers
SET DOB = ?
WHERE ClimberName = ?
''', ('1/12/80', 'Porter Jarrad'))

conn.commit()
conn.close()
