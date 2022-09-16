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
		repo_links, stars, labels = [], [], []
		for repo_dict in repo_dicts:
			repo_links


	def create_repo_dict_single(self,):
		"""Simple method to create dictionary for a single entry."""

	def check_status_code(self)
		"""Checks if Status Code is 200."""
		if self.r.status_code == 200:
			pass
		else
			print(f"API Call inconsistent. Status Code: {self.r.status_code}")
			self.call_flag = False