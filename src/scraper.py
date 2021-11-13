from instagram_interface import Instagram_I_IH
from tiktok_interface import Tiktok_I_IH

class IH_scraper:
	def __init__(self, token_IH_API, req_url = 'https://www.influencerhunters.com/apis'):
		self.ig = Instagram_I_IH(token_IH_API, req_url)
		self.tt = Tiktok_I_IH(token_IH_API, req_url)
