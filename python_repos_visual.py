import json
import requests
from plotly.graph_objs import Bar
from plotly import offline

def dump_json (json_dump):
	"""
	Dumps api call in json file.
	(not included inside the tutorial, twas taken from another chapter)
	"""
	readable_file = "api_dump/github_apicall_visual.json"
	with open(readable_file, "w", encoding="utf-8") as f:
		json.dump(json_dump, f, indent=4)

#Make an API call and store the responses.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Process results
response_dict = r.json()
repo_dicts = response_dict["items"]
dump_json(response_dict)
repo_names, stars = [], []

for repo_dict in repo_dicts:
	repo_names.append(repo_dict["name"])
	stars.append(repo_dict["stargazers_count"])

#Make visualization
data = [{
	"type" : "bar",
	"x" : repo_names,
	"y" : stars
	}]

my_layout = {
	"title" : "Most-Starred Pyhton Projects on GitHub",
	"xaxis" : {"title" : "Repository"},
	"yaxis" : {"title" : "Stars"}
	}

fig = {
	"data" : data,
	"layout" : my_layout,
	}

offline.plot(fig, filename="python_repos.html")