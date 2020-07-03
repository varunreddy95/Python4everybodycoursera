import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    service_url = "http://py4e-data.dr-chuck.net/json?"
else:
    service_url = "http://py4e-data.dr-chuck.net/json?"

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter the location: ")
    if len(address) < 1:
        break

    #Augmenting the API key, service URL and the address by the user
    parms = dict()
    parms["address"] = address
    if api_key is not False:
        parms["key"] = api_key

    url = service_url + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failed to Retrieve")
        print(data)
        continue

    #print(json.dumps(js, indent=4))
    for key in js:
        if key == "results":
            for item in js[key]:
                print(item["place_id"])




