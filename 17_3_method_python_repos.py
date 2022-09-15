import requests
from plotly.graph_objs import Bar
from plotly import offline

class API_CnE:
	"""Class for API Call and Evaluation."""
	def __init__(self, url=None):
		"""Init API variables."""
		self.url = url
		self.url_flag = False

	def check_url(self):
		"""Simple check if url is existing."""
		if self.url == None:
			print("Please pass url.")
		else
			self.url_flag = True