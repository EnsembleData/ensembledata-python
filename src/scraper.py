from instagram_interface import Instagram_I_ED
from tiktok_interface import Tiktok_I_ED
from reddit_interface import Reddit_I_ED
from youtube_interface import Youtube_I_ED
from twitch_interface import Twitch_I_ED

class ED_scraper:
	def __init__(self, token_ED_API, req_url = 'https://www.ensembledata.com/apis'):
		self.ig = Instagram_I_ED(token_ED_API, req_url)
		self.tt = Tiktok_I_ED(token_ED_API, req_url)
		self.r = Reddit_I_ED(token_ED_API, req_url)
		self.yt = Youtube_I_ED(token_ED_API, req_url)
		self.twc = Twitch_I_ED(token_ED_API, req_url)
