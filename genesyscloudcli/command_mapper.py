
class CommandMapper:

    def __init__(self):
        #register mappings of commands to URIs
        [
            ['queue', 'list', "GET", '/api/v2/routing/queues'],
            ['queue', 'get', "GET", '/api/v2/routing/queues/{}'],
            ['division', 'list', "GET", '/api/v2/authorization/divisions'],
            ['division', 'get', "GET", '/api/v2/authorization/divisions/{}'],
            ['division', 'list', "GET", '/api/v2/presencedefinitions'],
            ['division', 'get', "GET", '/api/v2/presencedefinitions/{}'],
            ['campaign', 'list', "GET", '/api/v2/outbound/campaigns'],
            ['campaign', 'get', "GET", '/api/v2/outbound/campaigns/{}'],
            ['contactlist', 'list', "GET", '/api/v2/outbound/contactlists'],
            ['contactlist', 'get', "GET", '/api/v2/outbound/contactlists/{}'],
            ['group', 'list', "GET", '/api/v2/groups'],
            ['group', 'get', "GET", '/api/v2/groups/{}'],
            ['skill', 'list', "GET", '/api/v2/routing/skills'],
            ['skill', 'list', "GET", '/api/v2/routing/skills/{}'],
            ['locations', 'list', "GET", '/api/v2/locations'],
            ['locations', 'list', "GET", '/api/v2/locations/{}'],
            ['user', 'list', "GET", '/api/v2/users'],
            ['user', 'get', "GET", '/api/v2/users/{}']
        ]
