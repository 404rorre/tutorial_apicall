import json
import requests

#Make an API call and store the responses.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
#Store API response in variable
response_dict = r.json()

#Visual help to read api call in indented format as dump.
readable_file = "data/github_apicall.json"
with open(readable_file, "w", encoding="utf-8") as f:
	json.dump(response_dict, f, indent=4)



#Helper
#Control results.
# print(response_dict.keys())
# print(len(response_dict["items"]))

