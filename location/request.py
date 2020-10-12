import sqlite3
import json
from models import Location

def get_all_locations():
  with sqlite3.connect("./Kennel.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""SELECT * FROM Location""")
    locations=[]
    dataset=db_cursor.fetchall()
    for row in dataset:
      location=Location(row['id'], row['name'], row['address'])
      locations.append(location.__dict__)
  return json.dumps(locations)

def get_single_location(id):
  with sqlite3.connect("./Kennel.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""SELECT * FROM Location WHERE id=?""", (id,))
    data=db_cursor.fetchone()
    location=Location(data['id'], data['name'], data['address'])
    return json.dumps(location.__dict__)

def  create_location(location):
  max_id=LOCATIONS[-1]["id"]
  new_id=max_id+1
  location["id"]=new_id
  LOCATIONS.append(location)
  return location

def delete_location(id):
  location_index=-1
  for index, location in enumerate(LOCATIONS):
    if location["id"]==id:
      location_index=index
  if location_index >=0:
    LOCATIONS.pop(location_index)

def update_location(id, new_location):
  for index, location in enumerate(LOCATIONS):
    if location["id"]==id:
      LOCATIONS[index]=new_location
      break