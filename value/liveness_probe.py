import os
from datetime import datetime, timedelta
import sys


file_name = 'data/value.json'
file_mod_time = datetime.fromtimestamp(os.stat(file_name).st_mtime)  
now = datetime.today()
max_delay = timedelta(minutes=10)

if now-file_mod_time > max_delay:
    print ("CRITICAL: {} last modified on {}. Threshold set to {} minutes.".format(file_name, file_mod_time, max_delay.seconds/60))
    sys.exit(1)
else:
    print ("OK. Command completed successfully {} minutes ago.".format((now-file_mod_time).seconds/60))
    sys.exit(0)