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
    except websockets.exceptions.ConnectionClosed:
        print(f"[-] Клиент отключился: {websocket.remote_address}")
    finally:
        connected_clients.remove(websocket)

async def main():
    port = int(os.environ.get("PORT", 10000))
    async with websockets.serve(handle_client, "0.0.0.0", port):
        print(f"[*] Сервер запущен на порту {port}")
        await asyncio.Future()  # бесконечно висим

if __name__ == "__main__":
    asyncio.run(main())
