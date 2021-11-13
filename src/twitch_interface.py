from base_interface import Interface_IH


class Twitch_I_IH(Interface_IH):

	def search_keyword(self, keyword, depth = 1, type_c="videos"):	
		"""Fetch list of videos/channels/games given a keyword

		Args:
			keyword (string): keyword name
			depth (int, optional): search depth. Higher depth-> more posts are retrieved
			type (int, optional): Either videos, channels or games .
		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/twitch/search'
		payload = {'keyword':keyword, 'depth':depth, 'token':self.token_IH_API, 'type':type_c}

		r = self.send_request(end_point, payload)
		return r	

	def get_user_videos(self, username, depth = 1):	
		"""Fetch list of videos/channels/games given a keyword

		Args:
			username (string): account username
			depth (int, optional): search depth. Higher depth-> more posts are retrieved
		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/twitch/user/videos'
		payload = {'username':username, 'depth':depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r
