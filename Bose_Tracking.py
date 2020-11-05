import json
from os import error
from typing import cast

with open('./Capture_Files/Bose/2020-10-29-Bose-Speaker.json') as f:
    input = json.load(f)

addr = "Advertising Address for Device"
A = []  # Identifying Tokens for Device
counter = 0

for entry in input:  # Initialize values
    if 'beacon' not in entry['_source']['layers']:
        addr = entry['_source']['layers']['btle']['btle.advertising_address']
        A.append(entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data'][
            'btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')[-8:])
    break

# print("Starting Address: ", addr)
# print("Keys: ", A)
for entry in input:
    # Ignoring beacon signals
    if 'beacon' not in entry['_source']['layers'] and 'btmesh' not in entry['_source']['layers']:

    # get the incoming address and identification token
        try:
            incomingAddr = entry['_source']['layers']['btle']['btle.advertising_address']
            incomingID = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data'][
                'btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')[-8:]
        except KeyError:
            print(incomingAddr, counter)
        # if the new address is the same as the old address, but with a different identification token, then remember the new token
        if incomingAddr == addr:
            if incomingID not in A:
                A.append(incomingID)
        # If the incoming address is unknown, but uses an old token, then track the new address.
        else:
            if incomingID in A:
                print("Changing ", addr, " -> ", incomingAddr)
                addr = incomingAddr
        counter += 1
        # print(counter)

# print("Ending Address: ", addr)
# print("Keys: ", A)