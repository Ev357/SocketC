import asyncio
import websockets

async def client():
    async with websockets.connect("wss://socketc.onrender.com") as websocket:
        while True:
            message = input("Enter a message to send: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received response: {response}")

asyncio.run(client())
