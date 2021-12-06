import os
import requests
import json
import datetime
import pandas as pd

# Set environment variables
barry_token = os.getenv('BARRY_TOKEN')
barry_token = "Bearer "+ barry_token
url = "https://jsonrpc.barry.energy/json-rpc#get-spot-price"

payload = json.dumps({
  "method": "co.getbarry.api.v1.OpenApiController.getTotalHourlyPrice",
  "id": 0,
  "jsonrpc": "2.0",
  "params": [
    "571313174113783269",
    "2021-12-06T00:00:00Z",
    "2021-12-06T01:00:00Z"
  ]
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': barry_token,
}

while __name__ == "__main__":
    response = requests.request("POST", url, headers=headers, data=payload)

    df = json.loads(response.text)    
    df_nested_list = pd.json_normalize(df, record_path=['result'])

    print (df_nested_list)

    exit()