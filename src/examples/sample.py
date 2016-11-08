import dota2api
import pickle
import json

api = dota2api.Initialise("EEEFEE01B931E78C0AA7BE51AD0AE852")
hist = api.get_match_history(account_id=345593450)
match = api.get_match_details(match_id=2757119438)

print("radiant win:" + str(match['radiant_win']))

# open the file for writing
f = open("out.txt","w")
f.write(json.dumps(match))
