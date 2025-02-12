# client.py
from aiocoap import Context, Message, GET
import asyncio

async def get_temperature():
    context = await Context.create_client_context()

    request = Message(code=GET, uri='coap://127.0.0.1:5683/temperature')

    try:
        response = await context.request(request).response
        print(f"Response: {response.payload.decode()}")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    asyncio.run(get_temperature())