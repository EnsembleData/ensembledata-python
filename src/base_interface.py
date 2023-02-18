import requests
from datetime import datetime


class Interface_IH:
	def __init__(self, token_IH_API, req_url = 'https://www.ensembledata.com/apis'):
		self.token_IH_API = token_IH_API
		self.req_url = req_url

	def send_request(self, end_point, payload, n_trials = 2):
		for i in range(n_trials):
			r = requests.get(end_point, params=payload)
			if r.status_code == 200:
				return r.json()["data"], True
			
		return r, False

	def get_used_token(self, date="today"):
		
		if date == "today":
			date = datetime.today().strftime('%Y%m%d')
		
		end_point = self.req_url+ '/customer/get-used-units'
		payload = {'date':date, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r	

