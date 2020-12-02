from . import api_client
import click
from . import printer

@click.group()
def analytics():
    """Analytics Data"""
    pass


@analytics.command()
@click.argument("conversation_id")
def conversation(conversation_id):

    client = api_client.ApiClient()
    response = client.get("/api/v2/analytics/conversations/{}/details".format(conversation_id))
    printer.print_data(response)
  
        
def register(cli):
    cli.add_command(analytics)