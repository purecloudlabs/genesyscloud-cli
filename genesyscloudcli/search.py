from . import api_client
import click
from . import printer
from click.decorators import option

@click.command()
@click.argument("term")
@click.option('--full', is_flag=True, default=False)
def search(term, full):
    """Search Genesys Cloud"""
    page_size = click.get_current_context().meta['page_size']
    page = click.get_current_context().meta['page']
    client = api_client.ApiClient()

    if page < 1:
        page = 1

    query = {
        "pageSize": page_size,
        "pageNumber": page,
        "types": [
            "users",
            "groups",
            "locations"
        ],
        "sortOrder": "SCORE",
        "query": [
            {
            "type": "TERM",
            "fields": [
                "address",
                "addressVerified",
                "addresses",
                "dateModified",
                "department",
                "description",
                "email",
                "emergencyNumber",
                "id",
                "name",
                "presence",
                "profileSkills",
                "routingStatus",
                "state",
                "station",
                "title",
                "type"
            ],
            "operator": "AND",
            "value": term
            }
        ]
        }

    response = client.post("/api/v2/search?profile=false", query)["results"]
    
    if full:
        printer.print_data(response)
    else:
        printer.print_name_id_data(response)
        
def register(cli):
    cli.add_command(search)