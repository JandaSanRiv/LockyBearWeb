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
        entity_id, = get_entity_id(conn,entity)
        if entity_id>0:
            return {"response": 200, "id": entity_id, "name": entity}
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO entities(name, created_at) VALUES ("'''+entity+'''", CURRENT_DATE)''')
        #conn.commit()
        print(f"Record inserted for: {entity}")
        return {"response": 201, "id": cursor.lastrowid, "name": entity }
    except Exception as e:
        print(f"Error inserting entity: {entity}. Error: {e}!")
        return {"response": 400, "id": -1, "name": entity }
def get_entity_id(conn, entity_name):
    cursor = conn.cursor()
    cursor.execute('''SELECT id from entities WHERE name = "'''+entity_name+'''"''')
    row = cursor.fetchone()
    print("Getting entity id")
    if row is not None:
        return row
    else:
        return -1,#because it's a tuple
def add_password(conn, entity, password):
    entity_id, = get_entity_id(conn, entity)
    print(entity_id)
    if entity_id <0:
        print("Error: The entity does not exist!")
        return {"response": 404, "entity": entity, "password": password}

    if get_password_id(conn, entity)[0]>0:
        print("Warning: The password already exists!")
        return {"response": 404, "entity": entity, "password": password}
    try:
        print("adding password!")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO passwords(entity_id, secret, created_at) VALUES ("''' + str(entity_id) + '''","''' + password + '''", CURRENT_DATE)''')
        conn.commit()
        print(f"Password {cursor.lastrowid} for entity {entity} added successfully")
        return {"response": 201, "id": cursor.lastrowid, "name": entity }
    except Exception as e:
        print(f"Error inserting password: {password}, entity: {entity}. Error: {e}")
        return {"response": 400, "id": -1, "name": password, "entity":entity}
def get_password_id(conn, entity_id):
    cursor = conn.cursor()
    cursor.execute('''SELECT id from passwords WHERE entity_id = "'''+entity_id+'''"''')
    row = cursor.fetchone()
    print("Getting entity id")
    if row is not None:
        return row
    else:
        return -1,#because it's a tuple
def get_entities(conn):
    entities = []
    cursor = conn.cursor()
    cursor.execute('''SELECT * from entities''')
    rows = cursor.fetchall()
    print("Getting entities")
    if rows:
        print("There are entities")
        for row in rows:
            print(row)
            entities.append({"id": row[0], "name": row[1]})
    return entities


def get_passwords(conn):
    passwords = []
    cursor = conn.cursor()
    cursor.execute('''SELECT * from passwords''')
    rows = cursor.fetchall()
    print("Getting passwords")
    if rows:
        print("There are passwords")
        for row in rows:
            print(row)
            passwords.append({"entity_id": row[0], "secret": row[1], "created_at": row[2]})
    return passwords

