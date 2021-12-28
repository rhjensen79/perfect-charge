import streamlit as st
import json
import logging


def main():
    st.title("Perfect Charge")
    st.write("This is the perfect charge monitoring/Control page")
    
    
    try:
        with open ("data/monitoring.json") as jsonfile:
            jsonObject = json.load(jsonfile)
            data = jsonObject['data']
            jsonfile.close()
            for d in data:
                chargevalue = (d['chargevalue'])
                logging.info("--- Chargevalue recieved from file ---")
                logging.info(chargevalue)
    except:
        with open("data/monitoring.json", "w") as f:
            chargevalue = 3.0
            f.close()

    # Get Chargevalue input
    chargevalue = st.number_input("Charging will happen at this price or below : ", chargevalue)
    logging.info("--- New Chargevalue input recieved ---")
    logging.info(chargevalue)


    # Get all variables and save them in file
    monitoringdata = {}
    monitoringdata['data'] = []
    #monitoringdata['data'].clear()
    monitoringdata['data'].append({
        'chargevalue': chargevalue
    })
    with open("data/monitoring.json", "w") as f:
        json.dump(monitoringdata, f)
    f.close()
    logging.info("--- Saving Chargevalue ---")
    logging.info(chargevalue)




# Run main program
if __name__ == '__main__':
    try:
        main()
    except:
        logging.warning('Program ended')