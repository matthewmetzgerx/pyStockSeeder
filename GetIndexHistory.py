from classes import FileCollection as fc
import json
from datetime import datetime

try:
    with open('config.json') as config:
        cfg = json.load(config)
except:
    print("You must create a config.json file. An example file is provided: example-config.json")
    print("Edit the file and change the name to config.json")
    exit(0)

header, crumb, cookie = fc.FileCollection.getYahooCrumb()

for support in cfg["indexFiles"]:
    startdate = fc.FileCollection.convert_to_unix(support["startdate"])
    enddate = fc.FileCollection.convert_to_unix(str(datetime.today().strftime('%d-%m-%Y')))
    origin = support["origin"].format(str(startdate),str(enddate),crumb)
    fc.FileCollection.getSupportingFile(origin, support["writeTo"], header, crumb, cookie)



