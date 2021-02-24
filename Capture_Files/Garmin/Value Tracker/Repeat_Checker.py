#This program checks to see if certain values are repeated within the same logfile and at what times.
import json
import sys
from os import error, name
import os, os.path

#don't check values that are already stored in this array.
checked = []
counter = 0
for i in range(1,2):
    with open('.\Value Tracker\Android\\'+ str(i) +'.json') as f:
        current_JSON = json.load(f)
    for entry in current_JSON:
        if('btatt.value' in entry['_source']['layers']['btatt']):
            current_Value = entry['_source']['layers']['btatt']['btatt.value']
            if current_Value not in checked:
                checked.append(current_Value)
                with open('.\Value Tracker\Android\\'+ str(i) +'.json') as f:
                    temp_JSON = json.load(f)
                for entry2 in temp_JSON:
                    if'btatt.value' in entry2['_source']['layers']['btatt']:
                        temp_Value = entry2['_source']['layers']['btatt']['btatt.value']
                        if temp_Value == current_Value:
                            counter += 1
                if counter > 1:
                    print("The value: " + current_Value + " appears " + str(counter) + " time(s).")
                counter = 0