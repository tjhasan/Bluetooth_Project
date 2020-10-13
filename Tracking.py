# import random
# import time

# timeout = 5 #tMax - The amount of time we will wait.
# timer = 0 #Timeout - Current amount of elapsed time

# while timer < timeout:
#     time.sleep(0.985)
#     timer += 1
#     if random.randint(0,1) == 1:
#         timer = 0

import json

with open('.\Capture_Files\\10-13-Test.json') as f:
    input = json.load(f)

addr = "Advertising Address for D"
A = [] #Identifying Tokens for D

for entry in input: #Initialize values
    if 'beacon' not in entry['_source']['layers']: 
        addr = entry['_source']['layers']['btle']['btle.advertising_address']
        A.append(entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data']['btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":",'')[-46:])
    break

print("Start Address: ", addr)
print("Start ID Tokens: ", A)
print('')

for entry in input: #Go through all JSON entries
    if 'beacon' not in entry['_source']['layers']: #Ignoring beacon signals

        #get the incoming address and identification token
        incomingAddr = entry['_source']['layers']['btle']['btle.advertising_address']
        incomingID = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data']['btcommon.eir_ad.entry']['btcommon.eir_ad.entry.data'].replace(":",'')[-46:]
        
        #if the new address is the same as the old address, but with a different identification token, then remember the new token
        if incomingAddr == addr:
            if incomingID not in A:
                A.append(incomingID)
        #If the incoming address is unknown, but uses an old token, then track the new address.
        else:
            if incomingID in A:
                addr = incomingAddr

print("End Address: ", addr)
print("End ID Tokens: ", A)
print('')
