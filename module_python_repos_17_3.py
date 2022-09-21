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
		self.check_api()

	def check_url(self):
		"""Simple check if url is existing."""
		if self.url_origin and self.headers :
			self.call_flag = True
		else:
			print("Please pass url and headers.")

	def check_api(self):
		"""Simple method to check if api_call is consistent."""
		self.call_api()
		self.check_status_code()

	def check_status_code(self):
		"""Checks if Status Code is 200."""
		if self.r.status_code == 200:
			pass
		else:
			print(f"API Call inconsistent. Status Code: {self.r.status_code}")
			self.call_flag = False

	def crash_api(self):
		"""
		Simple method to lock api response for test. (ddos denial from github)
		"""
		n = 0
		while self.call_flag:
			n += 1
			self.check_api()
			print(n)

	def start(self):
		"""Starts all programs."""
		if self.call_flag:
			self.create_repo_dict_all(self.call_api()["items"])
			self.create_graph()

	def call_api(self):
		"""Calls API and gets response."""
		self.r = requests.get(self.url_origin, headers=self.headers)
		return self.r.json()

	def create_repo_dict_all(self, repo_dicts):
		"""Simple method to create a complete dictionary of all entries."""
		#repo_links -> xaxis, shows url via hyperlink
		#stars -> yaxis, shows most starred repos
		#labels -> hovertext, shows repo owner and description
		self.repo_links, self.stars, self.labels = [], [], []
		
		#Test if api call and info crawling works
		# self.test_dict_call = {
		# 	"repo_links" : [],
		# 	"stars" : [],
		# 	"labels" : [],
		# 	}
		for repo_dict in repo_dicts:
			repo_list = self.create_repo_dict_single(repo_dict)
			self.repo_links.append(repo_list[0])
			self.stars.append(repo_list[1])
			self.labels.append(repo_list[2])

			#Test if api call and info crawling works
			# self.test_dict_call["repo_links"].append(repo_dict[0])
			# self.test_dict_call["stars"].append(repo_dict[1])
			# self.test_dict_call["labels"].append(repo_dict[2])

	def create_repo_dict_single(self, repo_dict):
		"""
		Simple method to crawl infos from a single dictionary entry.
		Returns info to outer method.
		"""
		repo_name = repo_dict["name"]
		repo_url = repo_dict["html_url"]
		repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
		owner = repo_dict["owner"]["login"]
		description = repo_dict["description"]
		label = f"{owner}<br />{description}"
		try:
			star = repo_dict["stargazers_count"]
		except KeyError:
			star = 0
		return [repo_link, star, label]

	def test_api_call(self):
		"""Simple Class to test returned list from API Call."""
		#Above self.create_repo_dict_all() uncomment "#" codelines to work.
		if self.call_flag:
			print(self.url_origin)
			print(self.headers)
			print(self.call_flag)
			self.create_repo_dict_all(self.call_api()["items"])
			print(self.r.status_code)
			print(self.test_dict_call)

	def create_graph(self):
		"""Creates visual overview over from the api call."""
		data = [{
			"type" : "bar",
			"x" : self.repo_links,
			"y" : self.stars,
			"hovertext" : self.labels,
			"marker" : {
				"color" : "rgb(60, 100, 150)",
				"line" : {
					"width" : 1.5,
					"color": "rgb(25, 25, 25)"
					}
				},
			"opacity" : 0.6,
			}]

		my_layout = {
			"title" : "Most-Starred Python Projects on GitHub",
			"titlefont" : {"size" : 28},
			"xaxis" : {
				"title" : "Repository",
				"titlefont" : {"size" : 24},
				"tickfont" : {"size" : 14},
				},
			"yaxis" : {
				"title" : "Stars",
				"titlefont" : {"size" : 24},
				"tickfont" : {"size" : 14},
				}
			}

		#data is for the extracted data and how they will look like
		#my_layout is for the axis and the fonts how they will look like
		fig = {
			"data" : data,
			"layout" : my_layout,
			}

		offline.plot(fig, filename="17_3_python_repos.html")