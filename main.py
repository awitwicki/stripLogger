import os
import time
from urllib.request import urlopen, Request

ip = os.getenv('STRIP_IP_ADDRESS')
token = os.getenv('STRIP_TOKEN')
interval = int(os.getenv('INTERVAL', '30'))

from miio import PowerStrip

strip = PowerStrip(ip=ip, token=token)

def influx_query(query_str: str):
    try:
        request_url = 'http://localhost:8086/write?db=bots'
        request_headers = {'Content-Type': 'application/Text'}

        httprequest = Request(
            request_url,
            data=query_str.encode('utf-8'),
            headers=request_headers,
            method="POST"
            )

        urlopen(httprequest)
    except Exception as e:
        print(e)


while True:
    try:
        status = strip.status()
        load_power = status.load_power

        data_str = f'iot,room=living_room,device=power_strip load_power={load_power}'

        print(data_str)
        influx_query(data_str)

    except Exception as e:
        print(e)

    time.sleep(interval)
