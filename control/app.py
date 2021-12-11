import os
import time
import json

while __name__ == "__main__":

    try:
        with open ("data/value.json") as jsonfile:
            jsonObject = json.load(jsonfile)
            result = jsonObject['result']
            jsonfile.close()

            for r in result:
                value = (r['value'])
                print ("Current price   : " + str(value))
                start = (r['start'])
                print ("Start Time      : " + str(start))
                end = (r['end'])
                print ("End Time        : " + str(end))
    except:
        print ("File not found")


    time.sleep(60)
