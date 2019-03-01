import sqlite3

def create_connection(db_file)
try: 
    conn = sqlite3.conenct(db_file)
    return conn
except Error as e:
    print(e)
return None

def select_all_tasks(conn)
cur=conn.cursor()
cur.execute()



