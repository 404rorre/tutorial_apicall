import json
import requests

#Make an API call and store the responses.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
#Store API response in variable
response_dict = r.json()

#Visual help to read api call in indented format as file dump.
#(not included inside the tutorial, twas taken from another chapter)
readable_file = "api_dump/github_apicall.json"
with open(readable_file, "w", encoding="utf-8") as f:
	json.dump(response_dict, f, indent=4)

print(f"Total repositories: {response_dict['total_count']}")

#Explore information about the repositories.
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

#Examine the first repository.
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
# 	print(key)


#Helper 
#Control results.
# print(response_dict.keys())
# print(len(response_dict["items"]))

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
	print(f"Name: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Description: {repo_dict['description']}")
	print("\n")
