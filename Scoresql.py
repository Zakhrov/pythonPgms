import sqlite3

def scoreProcessFn(id2find):
    db=sqlite3.connect("surfersDB.sdb")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    cursor.execute("select * from surfers")
    rows=cursor.fetchall()
    for row in rows:
        if row['id']==id2find:
            s={}
            s['id']=str(row['id'])
            s['name']=str(row['name'])
            s['country']=str(row['country'])
            s['average']=str(row['average'])
            s['board']=str(row['board'])
            s['age']=str(row['age'])
            cursor.close()
            return(s)
    cursor.close()
    return({})
lookup_id=int(input("enter the id"))
surfer=scoreProcessFn(lookup_id)
if surfer:
    print("ID:    " + surfer['id'])
    print("Name:    " + surfer['name'])
    print("Country:    " + surfer['country'])
    print("Avg:    " + surfer['average'])
    print("Game:    " + surfer['board'])
    print("Age:    " + surfer['age'])

