import os
import requests
import json
import datetime
import pandas as pd
import time

# Set environment variables
barry_token = os.getenv('BARRY_TOKEN')
barry_meter_id = os.getenv('BARRY_METER_ID')

barry_token = "Bearer "+ barry_token
url = "https://jsonrpc.barry.energy/json-rpc#get-spot-price"

api_date_format = '%Y-%m-%dT%H:%M:%SZ'
now = datetime.datetime.now()
later = (datetime.timedelta(hours = 1)) + now

# Calculate start and end times
start_time = (now.strftime("%Y")+"-"+now.strftime("%m")+"-"+now.strftime("%d")+"T"+now.strftime("%H")+":00:00Z")
end_time = (later.strftime("%Y")+"-"+later.strftime("%m")+"-"+later.strftime("%d")+"T"+later.strftime("%H")+":00:00Z")
# TODO : Fix error when time = 00:00 


payload = json.dumps({
  "method": "co.getbarry.api.v1.OpenApiController.getTotalHourlyPrice",
  "id": 0,
  "jsonrpc": "2.0",
  "params": [
    barry_meter_id,
    start_time,
    end_time
  ]
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': barry_token,
}

while __name__ == "__main__":
    
    # Get the data from the API
    response = requests.request("POST", url, headers=headers, data=payload)

    print (response.text)
    f = open("data/value.json", "w")
    f.write (response.text)
    f.close()

    # List files in data directory as test during development
    arr = os.listdir('data')
    print ("Files in data directory")
    print (arr)

    #df = json.loads(response.text)    
    #df_nested_list = pd.json_normalize(df, record_path=['result'])

    
    #if (df_nested_list['value'][0]) > 3:
    #  print ("Do not charge")
    #else: 
    #  print ("Charge")
    time.sleep(300)

   
  
    #exit()

    # Test action run 8