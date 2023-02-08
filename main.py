from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from app.api import api
from app.server import server

app = FastAPI(title='HBM+ Api')

@app.get("/calculate/{time}/{accuracy}")
def calculate(time: int, accuracy: int):
  response = {'sucess': True, 'value' : api.calculate(time, accuracy)}
  return JSONResponse(response)

@app.websocket("/ws")
def websocketEndpoint(websocket: WebSocket):
  return server.websocketEndpoint(websocket)
