import os
import time
import json
import requests
import logging


chargestatus = 0
controldata = {}


# Get token
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
        logging.info("--- Token recieved ---")
        return(data["accessToken"])
    except:
        logging.warning("Error getting token")

# Get charger id
def get_charger(token):
    url = "https://api.easee.cloud/api/chargers"
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    id = data[0]["id"]
    logging.info("--- Charger ID ---")
    logging.info(id)
    return(id)


# Set/Toggle the stete of the charger
def charger_control(token, id, command):
    url = "https://api.easee.cloud/api/chargers/"+ id +"/commands/" + command
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("POST", url, headers=headers)
    logging.info("--- Charger Reponse ---")
    logging.info(response.text)
    return (response)


# Get the charging/connected state of the charger
def charger_state(token, id):
    url = "https://api.easee.cloud/api/chargers/"+ id +"/state"
    headers = {"Authorization": "Bearer "+ token}
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    chargerOpMode = data["chargerOpMode"]
    logging.info("--- chargerOpMode ---")
    logging.info(chargerOpMode)
    return (chargerOpMode)



while __name__ == "__main__":
    # Set logging Config
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' , level=os.environ.get("LOGLEVEL", "INFO"))
    
    # Get chargevalue
    try:
        with open ("data/monitoring.json") as jsonfile:
                    jsonObject = json.load(jsonfile)
                    data = jsonObject['data']
                    jsonfile.close()
                    for d in data:
                        chargevalue = (d['chargevalue'])
                    #logging.info("--- chargevalue ---")
                    #logging.info(chargevalue)
    except:
        chargevalue = 3.0
        #logging.info ("Could not read file with chargevalue - setting to default value")

    # Get token
    token = (get_token())
    # Get Charger ID
    charger_id = (get_charger(token))

    # Open file and read latest value data
    try:
        with open ("data/value.json") as jsonfile:
            jsonObject = json.load(jsonfile)
            result = jsonObject['result']
            jsonfile.close()

            for r in result:
                value = (r['value'])
                #logging.info("Current price   : " + str(value))
                start = (r['start'])
                #logging.info("Start Time      : " + str(start))
                end = (r['end'])
                #logging.info("End Time        : " + str(end))

            # Get Charger state
            chargerstate = charger_state(token, charger_id)
            #print (chargerstate)
            if value <= chargevalue:
                if chargerstate == 0:
                    #logging.info("Price is right - But Charger is Offline - Skipping")
                    chargestatus = 0
                elif chargerstate == 1:
                    #logging.info("Price is right - But Charger is Disconnected - Skipping")
                    chargestatus = 0
                elif chargerstate == 3:
                    #logging.info("Price is right - But Charging is already in progress")
                    chargestatus = 1
                elif chargerstate == 4:
                    #logging.info("Price is right - But Charging is Complete - Skipping")
                    chargestatus = 0
                else:
                    charger_control(token, charger_id, "toggle_charging")
                    #logging.info("Price is right - Starting charge")
                    chargestatus = 1
            elif value > chargevalue:
                if chargerstate == 1:
                    #logging.info("Price is too high - But Charger is already Disconnected - Skipping")
                    chargestatus = 0
                elif chargerstate == 3:
                    #logging.info("Price is too high - Pausing Charge")
                    charger_control(token, charger_id, "toggle_charging")
                    chargestatus = 0
                else:
                    #logging.info("Price is too high - But charger is already stopped")
                    chargestatus = 0
            
    except:
        logging.warning ("File not found!!!")

    # Get all variables and save them in file
    controldata['data'] = []
    controldata['data'].append({
        'chargestatus': chargestatus,
        'chargerstate': chargerstate,
        'price': value,
        'start': start,
        'end': end
    })
    with open("data/control.json", "w") as f:
        json.dump(controldata, f)
    f.close()


    # Wait 5 minutes for next run
    logging.info("Waiting 5 minute for next run")
    time.sleep(300)
