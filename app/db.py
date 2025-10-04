import sqlite3

def init_db(conn):
    file = "passwords.db"

    try:
        #conn = sqlite3.connect(file)
        print("Database Sqlite3 connected successfully")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS entities (id INTEGER PRIMARY KEY, name VARCHAR UNIQUE, created_at DATETIME)")
        cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, entity_id integer, secret VARCHAR, created_at DATETIME, FOREIGN KEY(entity_id) REFERENCES entities(id))")
        conn.commit()
    except Exception as e:
        print(f"Database Sqlite3 not created successfully, e: {e}")
def add_entity(conn, entity):
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO entities(name, created_at) VALUES ("'''+entity+'''", CURRENT_DATE)''')
        conn.commit()
        print(f"Record inserted for: {entity}")
    except Exception as e:
        print(f"Error inserting entity: {entity}. Error: {e}")
def get_entity_id(conn, entity_name):
    cursor = conn.cursor()
    cursor.execute('''SELECT id from entities WHERE name = "'''+entity_name+'''"''')
    row = cursor.fetchone()
    print("Getting entity id")
    if row is not None:
        return row
    else:
        return -1
    
def add_password(conn, entity, password):
    entity_id, = get_entity_id(conn, entity)
    print(entity_id)
    if entity_id <0:
        return "Error: The entity does nto exist!"

    try:
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO passwords(entity_id, secret, created_at) VALUES ("''' + password + '''", CURRENT_DATE)''')
        conn.commit()
        return f"password {cursor.lastrowid} for entity {entity} added successfully"
    except:
        return "Error adding the password!"
def get_passwords():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords")
    rows = cursor.fetchall()
    return rows

