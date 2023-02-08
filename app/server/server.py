import random
import asyncio
from ..util import util
from datetime import datetime

async def websocketEndpoint(websocket):
  await websocket.accept()
  while True:
    try:
      await asyncio.sleep(2)
      resp = {'value': util.calculateValue(random.uniform(1000, 15000), None), 'time': datetime.now().strftime("%H:%M:%S")}
      await websocket.send_json(resp)
      
    except Exception as e:
      print('error:', e)
      break

    