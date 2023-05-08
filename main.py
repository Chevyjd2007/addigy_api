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
response = get(URL + JSON, headers=headers)
data = get(URL + JSON, headers=headers).json()

for device in data:
    device_name = device.get('Device Name')
    MDM_status = device.get('Is MDM Client Stuck')
    online_status = device.get('Online')

    print("Device Name: " + device_name)
    print('Is MDM Client Stuck: ' + str(MDM_status))
    print("Online Status: " + str(online_status))
    print("____________________________________________")

print("Status code: " + str(response.status_code))



