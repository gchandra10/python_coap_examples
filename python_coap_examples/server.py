# temperature_server.py
from aiocoap import Message,Context
from aiocoap.resource import Resource, Site
import asyncio

class TemperatureResource(Resource):
    def __init__(self):
        super().__init__()
        self.temp = 25.0

    async def render_get(self, request):
        payload = f"Temperature: {self.temp}°C".encode('utf8')
        return Message(payload=payload)

async def main():
    # Create resource tree
    root = Site()
    root.add_resource(['temperature'], TemperatureResource())

    # Bind to specific IP and port
    bind = ('127.0.0.1', 5683)  # localhost and default CoAP port
    await Context.create_server_context(root, bind=bind)
    
    print(f"Server started on coap://{bind[0]}:{bind[1]}")
    
    # Keep server running
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())