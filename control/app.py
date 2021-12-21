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
    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        data = json.loads(response.text)
        logging.info("---")
        logging.info("Token recieved")
        logging.info("---")
        return(data["accessToken"])
    except:
        logging.warning("Error getting token")


def get_charger(token):
    url = "https://api.easee.cloud/api/chargers"
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    id = data[0]["id"]
    logging.info("--- Charger ID ---")
    logging.info(id)
    logging.info("---------")
    return(id)

def charger_control(token, id, command):
    # Commands 
    # - start_charging
    # - stop_charging
    # - pause_charging
    # - resume_charging

    url = "https://api.easee.cloud/api/chargers/"+ id +"/commands/" + command
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("POST", url, headers=headers)
    logging.info("--- Charger Reponse ---")
    logging.info(response.text)
    logging.info("---------")
    return (response)


def charger_state(token, id):
    url = "https://api.easee.cloud/api/chargers/"+ id +"/" + command
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("GET", url, headers=headers)
    logging.info(response.text)


def charger_session(token, id):
    url = "https://api.easee.cloud/api/chargers/"+ id +"/sessions/ongoing"
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("GET", url, headers=headers)
    logging.info(response.text)


while __name__ == "__main__":
    # Set logging
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' , level=os.environ.get("LOGLEVEL", "INFO"))
    
    token = (get_token())
    charger_id = (get_charger(token))
    #charger_control(token, charger_id, "pause_charging")
    #charger_state(token, charger_id, "state")
    charger_session(token, charger_id)

    try:
        with open ("data/value.json") as jsonfile:
            jsonObject = json.load(jsonfile)
            result = jsonObject['result']
            jsonfile.close()

            for r in result:
                value = (r['value'])
                logging.info("Current price   : " + str(value))

                start = (r['start'])
                logging.info("Start Time      : " + str(start))

                end = (r['end'])
                logging.info("End Time        : " + str(end))
    except:
        logging.warning ("File not found")


    time.sleep(60)
