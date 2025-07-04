from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []

# decorators
@app.get('/')
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get('/teas')
def get_teas():
    return teas

@app.post('/teas', status_code=201)
def create_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.get('/teas/{tea_id}')
def get_tea(tea_id: int):
    for tea in teas:
        if tea.id == tea_id:
            return tea
    return {"error": "Tea not found"}, 404

@app.put('/teas/{tea_id}')
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}, 404

@app.delete('/teas/{tea_id}')
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted =  teas[index]
            return deleted
    return {"error": "Tea not found"}, 404