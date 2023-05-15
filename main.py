import requests
from requests import get
from pprint import PrettyPrinter

URL = "https://prod.addigy.com/api/"
JSON = "devices"

printer = PrettyPrinter()

headers = {
    "client-id": "",
    "client-secret": ""
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


