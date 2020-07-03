import urllib.request, urllib.parse, urllib.error
import json

'''
This program parses through the data from the url given as a input from the user and parses the data if it is in json
format. If not results in None. Each element of the json data is parsed through to achive some goal, in this case, sum
of all the count values under each element 
'''

url = input("Enter the URL: ")
print("Retrieving", url)
data = urllib.request.urlopen(url)
data_decoded = data.read().decode()
print("Retrieved", len(data_decoded), "characters")

sum_count = 0
try:
    js = json.loads(data_decoded)
except:
    js = None

if not js:
    print("==== Failure to retrieve ====")
else:
    for key in js:
        if key == "comments" :
            for items in js[key]:
                sum_count += items["count"]

print("Sum", sum_count)

