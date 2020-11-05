import json
from os import error
from typing import cast

# This is my local json folder. You will need to adjust this to match your own file directory structure.
with open('./Capture_Files/Apple/Cindy_Apple_Airpods.json', encoding='ISO-8859-1') as f:
    input = json.load(f)

addr = "Advertising Address for Device"

Followed_Addrs = []
IDK_First = []
IDK_Second = []

for entry in input:  # Initialize values
    if 'beacon' not in entry['_source']['layers']:
        addr = entry['_source']['layers']['btle']['btle.advertising_address']
        temp = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data']['btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')
        IDK_First.append(temp[3:6])
        IDK_Second.append(temp[7:])
        Followed_Addrs.append(addr)
    break

for entry in input:
    if 'beacon' not in entry['_source']['layers'] and 'btmesh' not in entry['_source']['layers']:

        incomingAddr = entry['_source']['layers']['btle']['btle.advertising_address']
        temp = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data']['btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')

        temp_IDK_First = temp[3:6]
        temp_IDK_Second = temp[7:]

        if incomingAddr == addr:
            if temp_IDK_First not in IDK_First:
                IDK_First.append(temp_IDK_First)
            if temp_IDK_Second not in IDK_Second:
                IDK_Second.append(temp_IDK_Second)
        else:
            if (temp_IDK_First in IDK_First or temp_IDK_Second in IDK_Second) and (incomingAddr not in Followed_Addrs):
                print("Tracking ", addr, "to ", incomingAddr)
                Followed_Addrs.append(incomingAddr)
                addr = incomingAddr
