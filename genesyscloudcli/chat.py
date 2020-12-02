import click
from . import printer
from . import api_client
from aioconsole import ainput
import websockets
import asyncio
import ssl 
import json

import requests

@click.group()
def chat():
    """Functions to create chat interactions"""    
    pass

@chat.command()
def deployments():    
    """Gets a list of chat deployments"""
    client = api_client.ApiClient()
    printer.print_name_id_data(client.get("/api/v2/widgets/deployments")['entities'])


@chat.command()
@click.argument('queuename')
@click.option('--chatdeployment', default="", help='Name of chat deployment to use, if not specified uses the first one found')
@click.option('--name', default="CLI", help='Name of the person chatting')
def new(queuename, chatdeployment, name):
    """Creates a new chat"""
    client = api_client.ApiClient()

    org = client.get("/api/v2/organizations/me")
    deployments = client.get("/api/v2/widgets/deployments")['entities']

    chat_deployment_config = deployments[0]

    if chatdeployment != "":
        for deployment in deployments:
            if deployment['name'] == chatdeployment:
                chat_deployment_config = deployment

    chat = client.post("/api/v2/webchat/guest/conversations", {
        "organizationId": org['id'],
        "deploymentId" : chat_deployment_config["id"],
        "routingTarget" : {
            "targetType": "queue",
            "targetAddress": queuename
        }, 
        "memberInfo" : {
            "displayName": name
        }
    })

    loop= asyncio.get_event_loop()
    loop.create_task(websocket_listener(chat['eventStreamUri']))
    loop.create_task(message_sender(client.environment, chat['jwt'], chat['id'], chat['member']['id']))
    loop.run_forever()

async def message_sender(environment, jwt, chat_id, member_id):
    while True:
        msg = await ainput("")
        headers = {
            'Authorization': "Bearer " + jwt,
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", "https://api.{}/api/v2/webchat/guest/conversations/{}/members/{}/messages".format(environment, chat_id, member_id), data=json.dumps(
            {
            "body": msg
        }), headers=headers)
    

        if response.status_code > 200:
            printer.print_data(response.json())

      
async def websocket_listener(wss_uri):
    ssl_context = ssl.SSLContext()
    ssl_context.verify_mode = ssl.CERT_NONE
    ssl_context.check_hostname = False

    async with websockets.connect(wss_uri, ssl=ssl_context) as websocket:
        while True:
            result = await websocket.recv()
            results = json.loads(result)

            if 'metadata' in results and results['metadata']['type'] == 'message':
                if len(results['eventBody']['body']) > 0 :
                    print("<<< " + results['eventBody']['body'])

def register(cli):
    cli.add_command(chat)