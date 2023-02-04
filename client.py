import asyncio
import websockets

async def client():
    async with websockets.connect("ws://localhost:10000") as websocket:
        await websocket.send("Hello, server!")
        response = await websocket.recv()
        print(response)

asyncio.run(client())
