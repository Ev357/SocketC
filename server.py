import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        data = message[::-1]
        await websocket.send(data)

start_server = websockets.serve(handler, "0.0.0.0", 10000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
