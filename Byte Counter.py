import json
from os import error
from typing import cast

# This is my local json folder. You will need to adjust this to match your own file directory structure.
with open('./Capture_Files/Garmin/Apple/Control/JSON/CNTROL_JSON_10.json', encoding='ISO-8859-1') as f:
    input = json.load(f)

total_length = 0

for entry in input:  # Initialize values
    length = int(entry['_source']['layers']['frame']['frame.len']) * 2
    total_length += length

print("")
print("Total bytes: ", total_length)
print("")
