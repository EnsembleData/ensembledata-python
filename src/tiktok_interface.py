from base_interface import Interface_IH


class Tiktok_I_IH(Interface_IH):

	def get_posts_from_hashtag(self, hashtag, cursor = 0):	
		"""Fetch list of most popular posts related to this hashtag 
		with information about users

		Args:
			hashtag (string): hashtag name
			cursor (int, optional): Starts with zero to get the first chunk of post.
			Use the otputted cursor as input for next API call, to get next chunk.

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/tt/hashtag/posts'
		payload = {'name':hashtag, 'cursor':cursor, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r	

	def get_user_info(self, name):	
		"""Get profile information of a user	

		Args:
			name (string): username (a.k.a. handle)

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""        
		end_point = self.req_url+ '/tt/user/info'
		payload = {'username':name, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r

	def get_user_posts(self, username, depth = 1):	
		"""Get the latest posts of a user given the username

		Args:
			username (string): username (a.k.a. handle)

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""                
		end_point = self.req_url+ '/tt/user/posts'
		payload = {'username':username, 'depth': depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r

	def get_user_posts_secuid(self, secUid, depth = 1):	
		"""Get the latest posts of a user given the Secuid

		Args:
			username (string): username (a.k.a. handle)

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""   
		end_point = self.req_url + "/tt/user/posts-from-secuid"
		payload = {'secUid':secUid, 'depth': depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r

	def get_recent_posts_from_hashtag(self, hashtag, days = 10):	
		"""Fetch list of recent posts (using the hashtag name) with information 
		about users.

		Args:
			hashtag (string): hashtag name
			days (int, optional): number of last days to retrieve. Defaults to 10.

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""

		end_point = self.req_url+ '/tt/hashtag/recent-posts'
		payload = {'name':hashtag, 'days':days, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r     

	def get_post_from_keyword(self, keyword, period = 0, sorting = 0, cursor = 0):	
		"""Get the results of a keybard search (posts, etc.)

		Args:
			keyword (string): keyword (hashtag, name, etc.) to search
			period (string): how many days. Options: "0" "1" "7" "30" "90" "180"
			sorting (bool): sorting order. Either 0 or 1
			cursor (int): At the beginning set to 0. Then it is given by the previous call.

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""		
		end_point = self.req_url+ '/tt/keyword/search'
		payload = {'name':keyword, 'period':period, "sorting":sorting, "cursor":cursor, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r  

	def get_comments(self, aweme_id, cursor = 0):	
		"""Fetch latest comments of a post

		Args:
			aweme_id (string): aweme_id of a post 
			cursor (int): At the beginning set to 0. Then it is given by the previous call.

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""				
		end_point = self.req_url+ '/tt/post/comments'
		payload = {"aweme_id":aweme_id, "cursor":cursor, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r  

	def get_comment_replies(self, aweme_id, comment_id, cursor = 0):	
		"""Fetch latest replies of a comment (of a post)

		Args:
			aweme_id (string): aweme_id of a post 
			comment_id (string): comment_id of a comment of that post
			cursor (int): At the beginning set to 0. Then it is given by the previous call.

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""			
		end_point = self.req_url+ '/tt/post/comments-replies'
		payload = {"aweme_id":aweme_id, "comment_id":comment_id, "cursor":cursor, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r  