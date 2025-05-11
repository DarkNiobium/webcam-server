import asyncio
import websockets
import os

connected_clients = set()

async def handle_client(websocket, path):
    print(f"[+] Подключился клиент: {websocket.remote_address}")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"[{websocket.remote_address}] {message}")
            # Здесь можно обрабатывать сообщения или отправлять ответ
            # await websocket.send("Принято")
    except websockets.exceptions.ConnectionClosed:
        print(f"[-] Клиент отключился: {websocket.remote_address}")
    finally:
        connected_clients.remove(websocket)

port = int(os.environ.get("PORT", 10000))
start_server = websockets.serve(handle_client, "0.0.0.0", port)

print(f"[*] Сервер запущен на порту {port}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
