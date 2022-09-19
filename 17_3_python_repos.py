from module_python_repos_17_3 import API_CnE

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
github_py = API_CnE(url, headers)
