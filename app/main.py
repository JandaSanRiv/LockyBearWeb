import sqlite3
from xml.dom.minidom import Entity

from fastapi import FastAPI
import db
conn = sqlite3.connect("passwords.db")

app = FastAPI()
@app.on_event("startup")
def on_startup():
    #This runs once then the app starts
    db.init_db(conn)
    addRecord()
    print("Database initialized")
    print(db.get_passwords())



def addRecord():
    db.add_entity(conn,"frog")
    #db.add_entity(conn,"duck")
    #db.add_password(conn, "horse", "newPWD")
    #db.add_password(conn, "duck", "oldPWD2")
"""@app.get("/")
async def root():
    return {"message": "Hello World"}"""
"""
@app.post("/api/entities")
async def entities(body: {}):
    return body
@app.get("/api/entities")
async def entities(entities_list: {}):
    return entities_list
@app.post("/api/passwords")
async def passwords(entity: str, password: str):
    return password

@app.get("/api/passwords/{entity}")
async def entities(entity: str, password: str):
    return {entity, password}"""
