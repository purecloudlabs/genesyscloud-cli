import json
import yaml
from tabulate import tabulate
from . import configuration
import click

config = configuration.Configuration()

def print_name_id_data(data, **kwargs):
    """Prints only the name and ids from a list of objects"""

    name_ids = []
    for o in data:
        entity = {
                "id": o['id'],
                "name": o['name']
            }

        if 'name' in kwargs:
            entity = {
                "id": o['id'],
                kwargs['name']: o[kwargs['name']]
            }
        
        if '_type' in o:
            entity["type"] = o["_type"]
        
        name_ids.append(entity)

    print_data(name_ids)

def print_data(data):    
    specified_format = click.get_current_context().meta['output']

    if specified_format == '':
        specified_format = config.output_type

    if specified_format == 'yaml':
        print_yaml(data)
    elif specified_format == 'table':
        print_table(data)
    else:
        print_json(data)

def print_json(data):
    print(json.dumps(data, indent=3))

def print_yaml(data):
    print(yaml.dump(data))


def print_table(data, headers=[]):
    print(tabulate(data, headers=headers))
