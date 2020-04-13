import requests, json

url = "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='2020'"
response = requests.request("GET", url)

teams = response.json()
teamandid = teams['team_all_season']['queryResults']['row']

#print(teamandid[0]['name_display_full'])
i = 0
team_pair = []

while i < len(teamandid):
   tmname = teamandid[i]['name_display_full']
   tmid = teamandid[i]['mlb_org_id']
   team_pair.append({"team_name":tmname, "team_id":tmid})
   i += 1

print(team_pair)
