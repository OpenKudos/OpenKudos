import json
import web3 as w3
import requests


__all__ = ['KudosContract', 'Kudos']

class KudosContract:
    def __init__(self, network, address, abi):
        self.w3 = w3.Web3(w3.HTTPProvider(network))
        self.contract = self.w3.eth.contract(address=address, abi=abi)
        self.last_id = self.contract.functions.getLatestId().call()

    def get_by_id(self, kudos_id):
        return self.contract.functions.getKudosById(kudos_id).call()

    def get_token_uri(self, kudos_id):
        return self.contract.functions.tokenURI(kudos_id).call()

    def __iter__(self):
        self.step = 1
        return self

    def __next__(self):
        if self.step <= self.last_id:
            token_uri = self.get_token_uri(self.step)
            r = requests.get(token_uri)
            self.step += 1
            return Kudos(self.step, r.json())
        else:
            raise StopIteration


class Kudos:
    def __init__(self, kudos_id, data):
        self.attributes =  data.get('attributes', [])
        self.background_color = data.get('background_color', '')
        self.description = data.get('description', '')
        self.external_url = data.get('external_url', '')
        self.image_url = data.get('image', '')
        self.name = data.get('name', '')

        self.id  = kudos_id

