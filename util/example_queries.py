import sqlite3

conn = sqlite3.connect(database='Database/MyClimb.db')
cursor = conn.cursor()
# cursor.execute('''SELECT T.RouteName, T.ClimberName, R.Location 
#                FROM "Ticks" T 
#                JOIN Routes R on R.RouteName = T.Routename''')
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# climbers = [
#     ('Doug Reed', '4/2/53'), 
#     ('Hans Kraus', '11/28/05'), 
#     ('Fritz Wiessner', '2/26/00'),
#     ('Eric Horst', '4/5/64')]
# cursor.executemany('''
# INSERT INTO Climbers (ClimberName, DOB) VALUES (?, ?)
# ''', climbers)

cursor.execute('''
UPDATE Climbers
SET DOB = ?
WHERE ClimberName = ?
''', ('1/12/80', 'Porter Jarrad'))

# Commit the transaction
# conn.commit()
# Commit the transaction
conn.commit()
conn.close()
