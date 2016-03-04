from __future__ import print_function

import json
from whatever.utils import do_something


def lambda_handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    print(message)
    do_something()
