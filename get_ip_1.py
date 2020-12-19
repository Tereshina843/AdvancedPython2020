
import asyncio

from concurrent.futures import FIRST_COMPLETED
from dataclasses import dataclass

import requests
import json


@dataclass
class Service:
    name: str
    url: str
    ip_attribute: str



SERVICES = (
    Service(
        name='ipify', url='https://api.ipify.org?format=json', ip_attribute="ip"
    ),
    Service(
        name='ip-api', url='http://ip-api.com/json', ip_attribute="query"
    ),
)



async def fetch_ip(service):
    response = requests.get(service.url)
    data = response.content
    data_as_dict = json.loads(data)
    ip = data_as_dict[service.ip_attribute]
    return ip


async def asynchronous():

    requests_array = []
    for service in SERVICES:
        requests_array.append(fetch_ip(service))


    done, pending = await asyncio.wait(requests_array, return_when=FIRST_COMPLETED)


    for ip_data in done:
        return ip_data.result()


loop = asyncio.get_event_loop()
ip = loop.run_until_complete(asynchronous())

print(ip)
