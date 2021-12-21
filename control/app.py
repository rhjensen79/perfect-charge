import os
import time
import json
import requests
import logging

chargevalue = 5.4

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
    url = "https://api.easee.cloud/api/chargers/"+ id +"/state"
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    chargerOpMode = data["chargerOpMode"]
    totalPower = data["totalPower"]
    logging.info("--- chargerOpMode ---")
    logging.info(chargerOpMode)
    logging.info("---------")
    return (chargerOpMode)



while __name__ == "__main__":
    # Set logging
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' , level=os.environ.get("LOGLEVEL", "INFO"))
    
    token = (get_token())
    charger_id = (get_charger(token))

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


            if charger_state(token, charger_id) == 2 or 6:
                logging.info ("Charger Ready")
                if value <= chargevalue:
                    logging.info("Price is right - Starting Charge")
                    charger_control(token, charger_id, "start_charging")

                else:
                    logging.info("Price is too high - Pausing Charge")
                    charger_control(token, charger_id, "pause_charging")
            else:
                logging.info ("Charger not ready")

    except:
        logging.warning ("File not found")

    time.sleep(300)
