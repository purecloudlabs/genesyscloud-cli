import click
from . import printer
from . import api_client
import json
import websockets
import asyncio
import ssl 
@click.group()
def notifications():
    """Functions to subscribe to web socket notifications"""
    pass

@notifications.command()
@click.argument('topics', nargs=-1)
def subscribe(topics):
    client = api_client.ApiClient()
    channel = client.post("/api/v2/notifications/channels", {})
    wss_uri = channel['connectUri']
    wss_id = channel['id']

    entities = []
    for topic in topics:
        entities.append({
            'id': topic
        })

    res = client.post("/api/v2/notifications/channels/{}/subscriptions".format(wss_id), entities)

    asyncio.get_event_loop().run_until_complete(websocket_listener(wss_uri))


async def websocket_listener(wss_uri):
    ssl_context = ssl.SSLContext()
    ssl_context.verify_mode = ssl.CERT_NONE
    ssl_context.check_hostname = False

    async with websockets.connect(wss_uri, ssl=ssl_context) as websocket:
        while True:
            result = await websocket.recv()
            results = json.loads(result)

            printer.print_data(results)
            print('-----------------------------')

def register(cli):
    cli.add_command(notifications)