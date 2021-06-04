#Database layer for CIS3145 by James Porter

#get imports for database layer
import sqlite3
import sys
import os
from contextlib import closing
#get business tier objects
from business import Task

conn = None

#db connection
def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            DB_FILE = "task_list_db.sqlite"
        else:
            HOME = os.environ["HOME"]
            DB_FILE = HOME + "task_list_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.execute("DROP TABLE IF EXISTS Task;")
        conn.execute("CREATE TABLE Task(taskID INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT NOT NULL, completed INTEGER NOT NULL);")
        conn.execute('''INSERT INTO Task(description, completed)VALUES('Get bike fixed',1),('Call your mom',1),('Buy toothbrush',0),('Do homework',0);''')
        
        conn.row_factory = sqlite3.Row
        
#db close connection
def close():
    if conn:
        conn.close()
        
#method to write rows to list from query results
def make_task(row):
    for each in row:
        print(row)
    return Task(row["taskID"], row["description"], row["completed"])

#method to return completed tasks
def get_completed_tasks():
    query = '''SELECT * FROM Task
                WHERE completed = 1;'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
        i = 0
    for row in results:
        i += 1
        print(i,row[1],"(DONE!)")

#method to return incomplete tasks
def get_incomplete_tasks():
    query = '''SELECT * FROM Task
                WHERE completed = 0;'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
        i = 0
    for row in results:
        i += 1
        print(i,row[1])
    print("\n")
        
#method to add a task
def add_task(description):
    query = '''INSERT INTO Task (description, completed)
                VALUES (?, ?);'''
    with closing(conn.cursor()) as c:
        c.execute(query, (description, 0))
        conn.commit()
#method to delete a task
def delete_task(taskID):
    query = '''DELETE FROM Task
                WHERE taskID = ?;'''
    with closing(conn.cursor()) as c:
        c.execute(query, (str(taskID)))
        conn.commit()
        
#method to update a task's status from incomplete to completed
def update_task_status(taskID):
    query = '''UPDATE Task
                SET completed = 1
                WHERE taskID = ?;'''
    with closing(conn.cursor()) as c:
        c.execute(query, (str(taskID)))
        conn.commit()
