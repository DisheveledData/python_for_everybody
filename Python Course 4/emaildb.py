import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #either create file or find and prep to use
cur = conn.cursor() #how we communicate

cur.execute('DROP TABLE IF EXISTS Counts') #no file but if there were could clear it

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''') #creates 2 things but we pretend it is a dictionary

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) #? prevents sql injection functions as a place holder to be replaced by email in a one tuple
    row = cur.fetchone() #gives the email back in variable row
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,)) #if row is not there then insert into counts a new count of 1 with that email
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,)) #else just always add one inside sql with one atomic statment
    conn.commit() #commits from memory to disk often limits speed

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' #order in decending counts

for row in cur.execute(sqlstr): #prints name and top down for top 10
    print(str(row[0]), row[1])

cur.close()
