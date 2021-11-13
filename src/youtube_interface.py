from base_interface import Interface_IH


class Youtube_I_IH(Interface_IH):

	def search_keyword(self, keyword, depth = 1):	
		"""Fetch list of videos containing the keyword

		Args:
			keyword (string): keyword name
			depth (int, optional): search depth. Higher depth-> more posts are retrieved
		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/youtube/search'
		payload = {'keyword':keyword, 'depth':depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r	

	def get_channel_videos(self, browseId, depth = 1):	
		"""Fetch list of videos of a channel

		Args:
			browseId (string): id of the user (you can get it from the search_keyword API response)
			depth (int, optional): search depth. Higher depth-> more posts are retrieved
		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/youtube/channel/videos'
		payload = {'browseId':browseId, 'depth':depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r	

