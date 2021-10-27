import sqlite3
#Setup
conn = sqlite3.connect('ugh.db')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Summations;

CREATE TABLE "Summations" (
	"Sums"	INTEGER
);
''')


cur.execute('''SELECT Numbers FROM Data''')
yayyy = cur.fetchall()
listy = list()
for thing in yayyy:
    for x in thing:
        listy.append(int(x))
Sum = sum(listy)

cur.execute('''INSERT OR IGNORE INTO Summations (Sums)
    VALUES ( ? )''', ( Sum, ) )

conn.commit()
