import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        await websocket.send(message[::-1])

start_server = websockets.serve(handler, "0.0.0.0", 10000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
