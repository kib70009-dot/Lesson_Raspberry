from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# MongoDB connection
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.get_database("todo_db")
collection = db.get_collection("todos")

class Todo(BaseModel):
    name: str
    description: Optional[str] = None

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/todos/")
def create_todo(todo: Todo):
    todo_dict = todo.dict()
    result = collection.insert_one(todo_dict)
    return {"id": str(result.inserted_id)}

@app.get("/todos/")
def read_todos():
    todos = []
    for todo in collection.find():
        todo["_id"] = str(todo["_id"])
        todos.append(todo)
    return todos

@app.get("/todos/{todo_id}")

def read_todo(todo_id: str):

    todo = collection.find_one({"_id": ObjectId(todo_id)})

    if todo:

        todo["_id"] = str(todo["_id"])

        return todo

    return {"error": "Todo not found"}



@app.put("/todos/{todo_id}")



def update_todo(todo_id: str, todo: Todo):



    todo_dict = todo.dict()



    result = collection.update_one({"_id": ObjectId(todo_id)}, {"$set": todo_dict})



    if result.modified_count == 1:



        return {"status": "success"}



    return {"error": "Todo not found"}







@app.delete("/todos/{todo_id}")



def delete_todo(todo_id: str):



    result = collection.delete_one({"_id": ObjectId(todo_id)})



    if result.deleted_count == 1:



        return {"status": "success"}



    return {"error": "Todo not found"}




