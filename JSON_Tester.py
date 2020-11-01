import json
from os import error
from typing import cast

with open('./Capture_Files/Apple/Cindy_Test.json') as f:
    input = json.load(f)

A_nearby = []  # Identifying Tokens for Device
A_handoff = []
Followed_Addrs = []
nearby = ''
handoff = ''
counter = 0

for entry in input:
    if 'beacon' not in entry['_source']['layers'] and 'btmesh' not in entry['_source']['layers']:

        try:
            incomingAddr = entry['_source']['layers']['btle']['btle.advertising_address']
            temp = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data'][
                'btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')
        except KeyError:
            print("Error occured at packet: ", counter)
        counter += 1