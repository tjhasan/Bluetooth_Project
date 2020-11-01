import json
from os import error
from typing import cast

# This is my local json folder. You will need to adjust this to match your own file directory structure.
with open('.\Capture_Files\Apple\Cindy_Test.json') as f:
    input = json.load(f)

addr = "Advertising Address for Device"

A_nearby = []  # Identifying Tokens for Device
A_handoff = []
Followed_Addrs = []
nearby = ''
handoff = ''

counter = 0

for entry in input:  # Initialize values
    if 'beacon' not in entry['_source']['layers']:
        addr = entry['_source']['layers']['btle']['btle.advertising_address']
        temp = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data'][
            'btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')

        if len(temp) == 14:
            handoff = temp
        elif len(temp) == 5:
            nearby = temp
        elif len(temp) == 19:
            nearby = temp[:5]
            handoff = temp[5:]
        A_nearby.append(nearby)
        A_handoff.append(handoff)
    break

for entry in input:
    if 'beacon' not in entry['_source']['layers'] and 'btmesh' not in entry['_source']['layers']:

        try:
            incomingAddr = entry['_source']['layers']['btle']['btle.advertising_address']
            temp = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data'][
                'btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')
        except KeyError:
            print(counter)
        if len(temp) == 14:
            handoff = temp
        elif len(temp) == 5:
            nearby = temp
        elif len(temp) == 19:
            nearby = temp[:5]
            handoff = temp[5:]

        if incomingAddr == addr:
            if nearby not in A_nearby:
                A_nearby.append(nearby)
            if handoff not in A_handoff:
                A_handoff.append(handoff)

        else:
            if nearby in A_nearby or handoff in A_handoff:
                if addr not in Followed_Addrs:
                    print("Following ", addr, " -> ", incomingAddr)
                    addr = incomingAddr
                    Followed_Addrs.append(addr)
        counter += 1
