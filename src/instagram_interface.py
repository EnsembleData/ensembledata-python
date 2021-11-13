from base_interface import Interface_IH


class Instagram_I_IH(Interface_IH):

	def get_posts_from_hashtag(self, hashtag, depth = 1):
		"""Fetch latest posts from an hashtag

		Args:
			hashtag (string): hashtag name
			depth (int): depth search parameter.

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""					
		end_point = self.req_url+ '/instagram/hashtag/posts'
		payload = {'tag':hashtag, 'depth':depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r

	def get_posts_from_userid(self, user_id, depth = 1):	
		"""Fetch posts of a user given its user_id 
		(starting from the most recent ones)

		Args:
			user_id (string): user_id of the user
			depth (int): depth posts retrieved.

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""			
		end_point = self.req_url+ '/instagram/user/posts-from-userid'
		payload = {'user_id':user_id, 'depth':depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r	

	def get_posts_from_username(self, username, depth = 1):	
		"""Fetch posts of a user given its username 
		(starting from the most recent ones)

		Args:
			username (string): username of the user
			depth (int): depth posts retrieved.

		Returns:
			dictionary: content of the response
			bool: True if the request succeeded 
		"""					
		end_point = self.req_url+ '/instagram/user/posts'
		payload = {'username':username, 'depth':depth, 'token':self.token_IH_API}

		r = self.send_request(end_point, payload)
		return r

	def get_comments_from_shortcode(self, shortcode, depth):	
		end_point = self.req_url+ '/instagram/post/comments'
		payload = {'shortcode':shortcode, 'token':self.token_IH_API, 'depth':depth}

		r = self.send_request(end_point, payload)
		return r	


	def get_post_from_shortcode(self, shortcode ):
		end_point = self.req_url+ '/instagram/post/info'
		payload = {'shortcode':shortcode, 'token':self.token_IH_API}
		
		r = self.send_request(end_point, payload)
		return r

	def get_igtv(self, user_id, depth = 1):	
		end_point = self.req_url+ '/instagram/user/igtv'
		payload = {'user_id':user_id, 'depth':depth, 'token':self.token_IH_API}
        
		r = self.send_request(end_point, payload)
		return r	
		
	def search(self, keyword):	
		end_point = self.req_url+ '/instagram/search'
		payload = {'keyword':keyword, 'token':self.token_IH_API}
        
		r = self.send_request(end_point, payload)
		return r	
    
	def get_likes(self, shortcode, depth = 1):	
		end_point = self.req_url+ '/instagram/post/likes'
		payload = {'shortcode':shortcode, 'token':self.token_IH_API, 'depth':depth}
        
		r = self.send_request(end_point, payload)
		return r	
    
	def get_followers(self, user_id):	
		end_point = self.req_url+ '/instagram/user/followers'
		payload = {'user_id':user_id, 'token':self.token_IH_API}
        
		r = self.send_request(end_point, payload)
		return r

	def get_following(self, user_id):	
		end_point = self.req_url+ '/instagram/user/following'
		payload = {'user_id':user_id, 'token':self.token_IH_API}
        
		r = self.send_request(end_point, payload)
		return r

	def get_reels(self, user_id, depth = 1):	
		end_point = self.req_url+ '/instagram/user/reels'
		payload = {'user_id':user_id, 'token':self.token_IH_API, 'depth':depth}
        
		r = self.send_request(end_point, payload)
		return r

	def get_recentstories(self, user_id):	
		end_point = self.req_url+ '/instagram/user/recent-stories'
		payload = {'user_id':user_id, 'token':self.token_IH_API}
        
		r = self.send_request(end_point, payload)
		return r

	def get_user_info(self, username):	
		end_point = self.req_url+ '/instagram/user/info'
		payload = {'username':username, 'token':self.token_IH_API}
        
		r = self.send_request(end_point, payload)
		return r

	def get_user_detailed_info(self, username):	
		end_point = self.req_url+ '/instagram/user/detailed-info'
		payload = {'username':username, 'token':self.token_IH_API}
        
		r = self.send_request(end_point, payload)
		return r

	def get_user_detailed_info_id(self, user_id):	
		end_point = self.req_url+ '/instagram/user/detailed-info-from-userid'
		payload = {'user_id':user_id, 'token':self.token_IH_API}
        
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