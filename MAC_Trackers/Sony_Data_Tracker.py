import json
from os import error
from typing import cast

with open('./Capture_Files/Sony/Sony_Siri.json', encoding='ISO-8859-1') as f:
    input = json.load(f)

packet_Number = 0
current_Data = ''
tracking_Data = ''
time = ''

print()

for entry in input:
    current_Data = entry['_source']['layers']['btle']['btcommon.eir_ad.advertising_data']['btcommon.eir_ad.entry']['btcommon.eir_ad.entry.service_data']
    time = entry['_source']['layers']["frame"]["frame.time_relative"]

    if current_Data != tracking_Data:
        print("Time:", time, "seconds. Data changed:", tracking_Data, "-->", current_Data)
        tracking_Data = current_Data
    packet_Number += 1

print()
