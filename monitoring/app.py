import streamlit as st
import json

monitoringdata = {}
monitoringdata['data'] = []

st.title("Perfect Charge")
st.write("This is the perfect charge monitoring/Control page")

try:
    with open ("data/monitoring.json") as jsonfile:
                jsonObject = json.load(jsonfile)
                data = jsonObject['data']
                jsonfile.close()
                for d in data:
                    chargevalue = (d['chargevalue'])
except:
    chargevalue = 3.0

print (chargevalue)
# Get Chargevalue input
chargevalue = st.number_input("Charging will happen at this price or below : ",chargevalue)

# Get all variables and save them in file

monitoringdata['data'].append({
    'chargevalue': chargevalue
})
with open("data/monitoring.json", "w") as f:
    json.dump(monitoringdata, f)
f.close()
