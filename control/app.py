import os
import time
import json
import requests
import logging

def get_token():
    user = os.getenv('EASEE_USER')
    password = os.getenv('EASEE_PASSWORD')
    url = "https://api.easee.cloud/api/accounts/token"
    payload = "{\"userName\":\"" + user + "\",\"password\":\"" + password + "\"}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/*+json"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    data = json.loads(response.text)
    return(data["accessToken"])


def get_charger(token):
    url = "https://api.easee.cloud/api/chargers"
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    id = data[0]["id"]
    return(id)

def control_charger(token, id, command):
    if command == "start":
        command = "start_charging"
        status = "Started Charging"
    else:
        command = "stop_charging"
        status = "Stopped Charging"
    url = "https://api.easee.cloud/api/chargers/"+ id +"/commands/" + command
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("POST", url, headers=headers)
    return (status)



while __name__ == "__main__":
    token = (get_token())
    #charger_id = (get_charger(token))
    #control_charger(token, charger_id, "start")


    try:
        with open ("data/value.json") as jsonfile:
            jsonObject = json.load(jsonfile)
            result = jsonObject['result']
            jsonfile.close()

            for r in result:
                value = (r['value'])
                print ("Current price   : " + str(value))
                logging.info("Current price   : " + str(value))

                start = (r['start'])
                print ("Start Time      : " + str(start))
                logging.info("Start Time      : " + str(start))

                end = (r['end'])
                print ("End Time        : " + str(end))
                logging.info("End Time        : " + str(end))
    except:
        logging.warning ("File not found")


    time.sleep(60)
