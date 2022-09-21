import unittest
from module_python_repos_17_3 import API_CnE

class TestAPICnE(unittest.TestCase):
	"""Tests for the class API_CnE."""
	
	def test_status_code(self):
		"""Test status code from the API Call if the call is consistent."""
		url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
		headers = {"Accept": "application/vnd.github.v3+json"}
		#sc -> status code of API call
		response_sc = 200
		api_call = API_CnE(url, headers)
		api_call.call_api()
		self.assertTrue(response_sc == api_call.r.status_code)

	def test_number_returned_items(self):
		"""Tests the number of items returned."""
		url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
		headers = {"Accept": "application/vnd.github.v3+json"}
		expected_items = 30
		api_call = API_CnE(url, headers)
		self.assertTrue(expected_items == len(api_call.call_api()["items"]))

	def test_minimum_number_returend_items(self):
		"""Tests if a minimum threshold returned items is reached."""
		url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
		headers = {"Accept": "application/vnd.github.v3+json"}
		expected_items = 25
		api_call = API_CnE(url, headers)
		self.assertTrue(len(api_call.call_api()["items"]) >= expected_items)

if __name__ == "__main__":
	unittest.main()