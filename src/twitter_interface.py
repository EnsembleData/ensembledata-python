from base_interface import Interface_IH


class Twitter_I_IH(Interface_IH):

	def search_keyword(self, keyword, depth = 1, latest=1):	
		"""Fetch list of twits (and meta-information) containing the keyword

		Args:
			keyword (string): keyword name
			depth (int, optional): search depth. Higher depth-> more posts are retrieved
                        latest(boolean, optional): if True (1) retrieves in chronological (latest first) order
		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/twitter/search'
		payload = {'keyword':keyword, 'depth':depth, 'token':self.token_IH_API, 'latest':latest}

		r = self.send_request(end_point, payload)
		return r	

