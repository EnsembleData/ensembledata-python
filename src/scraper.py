from instagram_interface import Instagram_I_IH
from tiktok_interface import Tiktok_I_IH
from reddit_interface import Reddit_I_IH
from youtube_interface import Youtube_I_IH
from twitch_interface import Twitch_I_IH
from twitter_interface import Twitter_I_IH

class IH_scraper:
	def __init__(self, token_IH_API, req_url = 'https://www.influencerhunters.com/apis'):
		self.ig = Instagram_I_IH(token_IH_API, req_url)
		self.tt = Tiktok_I_IH(token_IH_API, req_url)
		self.r = Reddit_I_IH(token_IH_API, req_url)
		self.yt = Youtube_I_IH(token_IH_API, req_url)
		self.twc = Twitch_I_IH(token_IH_API, req_url)
		self.twr = Twitter_I_IH(token_IH_API, req_url)
