import json
import numpy as np
import time

def write_to_json_file(filename, an_object):
    with open(filename,'w') as file:
        json.dump(an_object, file, indent=2, separators=(',',':'))

ccm = {
"ccm_01" :[
    {
        "temperature": "23",
        "moisture": "40",
        "brithness": "80",
        "distance": "900"
    }
]
}

written_data = write_to_json_file('api.json', ccm)

i = 0

#while (i < 1):
simu_temp = np.random.randint(0, 100)

#time.sleep(1)
    

