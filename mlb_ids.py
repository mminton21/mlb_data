import requests, json

url = "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='2020'"
response = requests.request("GET", url)

teams = response.json()
print(teams)
