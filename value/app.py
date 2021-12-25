import os
import requests
import json
import datetime
import pandas as pd
import time
import logging

# Set environment variables
barry_token = os.getenv('BARRY_TOKEN')
barry_meter_id = os.getenv('BARRY_METER_ID')

barry_token = "Bearer "+ barry_token
url = "https://jsonrpc.barry.energy/json-rpc#get-spot-price"

while __name__ == "__main__":
    # Set logging
    #logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' , level=os.environ.get("LOGLEVEL", "INFO"))
    
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
    
    # Get the data from the API
    response = requests.request("POST", url, headers=headers, data=payload)

    print (response.text)
    f = open("data/value.json", "w")
    f.write (response.text)
    f.close()

    # List files in data directory as test during development
    arr = os.listdir('data')
    #logging.info ("Files in data directory")
    #logging.info (arr)

    time.sleep(300)

   
    #exit()