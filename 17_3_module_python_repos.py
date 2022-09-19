import requests
from plotly.graph_objs import Bar
from plotly import offline

class API_CnE:
	"""Class for API Call and Evaluation."""
	def __init__(self, url=None, headers=None):
		"""Init API variables."""
		self.url_origin = url
		self.headers = headers
		self.call_flag = False
		#Checks if url is existing
		self.check_url()

	def check_url(self):
		"""Simple check if url is existing."""
		if self.url and self.headers :
			self.call_flag = True
		else
			print("Please pass url and headers.")

	def start(self):
		"""Starts all programs."""
		while self.call_flag:
			self.create_repo_dict_all(self.call_api()["items"])

	def call_api(self, url=self.url_origin):
		"""Calls API and gets response."""
		self.r = requests.get(url, headers=self.headers)
		self.check_status_code()
		return r.json()

	def create_repo_dict_all(self, repo_dicts):
		"""Simple method to create a complete dictionary of all entries."""
		#repo_links -> xaxis, shows url via hyperlink
		#stars -> yaxis, shows most starred repos
		#labels -> hovertext, shows repo owner and description
		repo_links, stars, labels = [], [], []
		for repo_dict in repo_dicts:
			repo_dict = self.create_repo_dict_single(repo_dict)
			repo_links.append(repo_dict[0])
			stars.append(repo_dict[1])
			labels.append(repo_dict[2])

	def create_repo_dict_single(self, repo_dict):
		"""
		Simple method to crawl infos from a single dictionary entry.
		Returns info to outer method.
		"""
		repo_name = repo_dict["name"]
		repo_url = repo_dict["html_url"]
		repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
		star = repo_dict["stargazers_count"]
		owener = repo_dict["owner"]["login"]
		description = repo_dict["description"]
		label = f"{owner}<br />{description}"

		return [repo_link, star, label]

	def check_status_code(self)
		"""Checks if Status Code is 200."""
		if self.r.status_code == 200:
			pass
		else
			print(f"API Call inconsistent. Status Code: {self.r.status_code}")
			self.call_flag = False