import requests
from requests import get
from pprint import PrettyPrinter

URL = "https://prod.addigy.com/api/"
JSON = "devices"

printer = PrettyPrinter()

headers = {
    "client-id": "6cfd29c20e2f92dfca99814780d5f03bf91b4a69",
    "client-secret": "bfe9c33f547019ea168e942ccc857585734e4908fe5baf76476a3a77d64ac93a33b846aa6c8ca252"
}

data = get(URL + JSON, headers=headers).json()

printer.pprint(data)
