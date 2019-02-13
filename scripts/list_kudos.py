import sys
sys.path.insert(0, '../kudos')

import kudos
import json
import os
import time

from tabulate import tabulate
from progress.bar import Bar


contract_path = os.getenv('CONTRACT_JSON_PATH')
network = os.getenv('NETWORK_URL')

address = os.getenv('ADDRESS_NETWORK', '0x2aEa4Add166EBf38b63d09a75dE1a7b94Aa24163')
limit = int(os.getenv('LIMIT_KUDOS', 10))

if __name__ == '__main__':

    kudos_set = set()
    with open(contract_path) as contract_file:
        json_contract = json.load(contract_file)
        kudos_contract = kudos.KudosContract(network,
                                       address=address,
                                       abi=json_contract['abi'])

        if limit > kudos_contract.last_id:
            limit = kudos_contract.last_id

        bar = Bar('Processing', max=limit)

        for kudos in kudos_contract:
            kudos_set.add((kudos.id, kudos.name, kudos.description[:20] + '...', kudos.image_url[:30] + '...'))

            bar.next()

            if kudos.id > limit:
                break

        bar.finish()

        print(tabulate(kudos_set, headers=['id', 'name', 'description', 'art url']))
        
