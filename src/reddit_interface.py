from base_interface import Interface_IH


class Reddit_I_IH(Interface_IH):

	def get_posts_from_keyword(self, keyword, depth = 1, sorting="new",timing="all"):	
		"""Fetch list of results (and meta-information) containing the keyword

		Args:
			keyword (string): keyword name
			depth (int, optional): search depth. Higher depth-> more posts are retrieved
			sort (string, optional): sorting order. Possibilities: "relevance" "hot" "new" "top" "comments"
			timing (string, optional): filter by post date. 

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/reddit/search'
		payload = {'keyword':keyword, 'depth':depth, 'sorting':sorting, 'timing':timing, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r	


