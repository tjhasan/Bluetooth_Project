import json
from os import error

# This is my local json folder. You will need to adjust this to match your own file directory structure.
with open('./Capture_Files/Microsoft/Test_file1.json') as f:
    input = json.load(f)

addr = "Advertising Address for Device"
A = []  # Identifying Tokens for Device
counter = 0

# For some reason, beacon devices tend to make their way into the ADV_NONCONN_ID file filter, so I am double checking their exclusion.
for entry in input:  # Initialize values
    if 'beacon' not in entry['_source']['layers']:
        addr = entry['_source']['layers']['btle']['btle.advertising_address']
        # It's easier to remove the ':' from the hex values and save double the projected save bytes from the paper. (saving [-23:] bytes in the paper -> [-46])
        A.append(entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data']
                 ['btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')[-46:])
    break

# print("Starting Address: ", addr)
# print("Keys: ", A)
for entry in input:  # Go through all JSON entries
    # Ignoring beacon signals
    if 'beacon' not in entry['_source']['layers'] and 'btmesh' not in entry['_source']['layers']:

    # get the incoming address and identification token
        try:
            incomingAddr = entry['_source']['layers']['btle']['btle.advertising_address']
            incomingID = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data']['btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":", '')[-46:]
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
