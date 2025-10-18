import sqlite3

from fastapi import FastAPI
import db
conn = sqlite3.connect("passwords5.db", timeout=10)

app = FastAPI()
@app.on_event("startup")
def on_startup():
    #This runs once then the app starts
    db.init_db(conn)
    addRecord()
    conn.commit()
    print("Database initialized")

def addRecord():
    db.add_entity(conn,"UNICORN")
    db.add_entity(conn,"duck")
    db.add_entity(conn,"Dog")

    db.add_password(conn, "UNICORN", "newPWD")
    db.add_password(conn, "duck", "oldPWD2")
    db.add_password(conn, "Dog", "oldPWD3")

    db.add_entity(conn,"GoogleAccount")
    db.add_password(conn, "GoogleAccount", "YouRNice2")
    list_entities = db.get_entities(conn)
    print("entities returned are: ")
    print(list_entities)

    list_passwords = db.get_passwords(conn)
    print("passwords returned are: ")
    print(list_passwords)
@app.get("/")
async def root():
    return {"message": "Hello World"}
"""
@app.get("/api/entities")
async def entities():
    return db.get_entities(conn)

@app.post("/api/entities")
async def entities(body: {}):
    response = db.add_entity(conn,body["entity"])
    return response
@app.post("/api/passwords")
async def passwords(body: {}):
    response = db.add_password(conn,body["entity"],body["password"])
    return response

@app.get("/api/passwords/{entity}")
async def passwords():
    return db.get_passwords(conn)"""
