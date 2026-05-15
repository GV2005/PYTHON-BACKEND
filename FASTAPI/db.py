from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import sqlite3
from typing import Optional

app=FastAPI()
conn=sqlite3.connect("test.db",check_same_thread=False)
cursor=conn.cursor()

#  TABLE CREATION 

cursor.execute('''
    create table if not exists items(
        item_id integer primary key autoincrement,
        name text not null,
        desc text            
    )
    ''')

#   CREATE


class item(BaseModel):
    name:str
    desc:str


@app.post("/itmes/create")

def create_item(i:item):
    try:
        cursor.execute("Insert into items (name,desc) values (?,?)",(i.name,i.desc))
        conn.commit()
        return {"message":"items added successfully"}

    except Exception as e:
        return HTTPException(status_code=400,detail=f"unable to add bcz {e}")

@app.get("/itmes/read")

def read_item():
    try:
        cursor.execute("select * from items")
        rows=cursor.fetchall()

        return [{"id":r[0],"name":r[1],"desc":r[2]} for r in rows]

    except Exception as e:
        return HTTPException(status_code=400,detail=f"unable to fetch bcz {e}")

@app.get("/itmes/readone/{name}")

def read_one(name:str):
    try:
        cursor.execute("select * from items where name=?",(name,))
        row=cursor.fetchone()

        if row is None:
            return HTTPException(status_code=400,detail="Itom not found")

        return {"id":row[0],"name":row[1],"description":row[2]}

    except Exception as e:
        return HTTPException(status_code=402,detail=f"unable to fetch bcz {e}")
    
@app.put("/itmes/update/{item_id}")

def update_item(item_id:int,i:item):
    try:
        cursor.execute("update items set name=?,desc=? where item_id=?",(i.name,i.desc,item_id))
        conn.commit()
        return {"message":"Item updated successfully"}

    except Exception as e:
        return HTTPException(status_code=402,detail=f"unable to update bcz {e}")
    
@app.delete("/itmes/delete/{name}")

def delete_item(name:str):
    try:
        cursor.execute("delete from items where name=?",(name,))
        conn.commit()
        return {"message":"Item deleted successfully"}

    except Exception as e:
        return HTTPException(status_code=402,detail=f"unable to delete bcz {e}")
