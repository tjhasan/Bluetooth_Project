#This program checks to see if certain values are present in other log files.
import json
import sys
from os import error, name
import os, os.path

#don't check values that are already stored in this array.
checked_values = []
found = False

for i in range(1,41):
    print("**************Common Values Found in Testlog "+ str(i) + "**************")
    with open('.\Value Tracker\Android\\'+ str(i) +'.json') as f:
        current_JSON = json.load(f)
    for entry in current_JSON:
        if('btatt.value' in entry['_source']['layers']['btatt']):
            current_Value = entry['_source']['layers']['btatt']['btatt.value']
            if current_Value not in checked_values:
                #checked_values.append(current_Value)
                k = i
                found = False
                for k in range(i+1, 41):
                    with open('.\Value Tracker\Android\\'+ str(k) +'.json') as g:
                        comparison_JSON = json.load(g)
                        for entry2 in comparison_JSON:
                            if('btatt.value' in entry2['_source']['layers']['btatt']):
                                comparison_Value = entry2['_source']['layers']['btatt']['btatt.value']
                                if(comparison_Value == current_Value):
                                    print(comparison_Value + " originating in testlog "+ str(i) +" found in testlog " + str(k))
                                    found = True
                if found:
                    print('')
    print("************************************************************")