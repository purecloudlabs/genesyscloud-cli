from . import api_client
import click
from . import printer
from click.decorators import option

@click.command()
def organization():
    """Get organization details"""
    client = api_client.ApiClient()
    response = client.get("/api/v2/organizations/me")
    printer.print_data(response)
  
        
def register(cli):
    cli.add_command(organization)