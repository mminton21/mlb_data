import requests
import json

url = "https://mlb-data.p.rapidapi.com/json/named.roster_40.bam"

querystring = {"team_id":"'121'"}

headers = {
    'x-rapidapi-host': "mlb-data.p.rapidapi.com",
    'x-rapidapi-key': "e678ee0d49msh35e80f3e5ca0777p1ac77bjsna582895c8dde"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
full_data = response.json()
mlb_40 = full_data['roster_40']['queryResults']['row']

i = 0
while mlb_40[i]['name_full']:
    print(mlb_40[i]['name_full'])
    i += 1

#print(mlb_40[0]['name_full'])
