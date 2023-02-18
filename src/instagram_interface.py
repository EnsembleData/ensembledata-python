from base_interface import Interface_IH


class Instagram_I_IH(Interface_IH):

  def get_user_posts(self, user_id, depth, oldest_timestamp, chunk_size=10, start_cursor=''):
    """ Fetch user posts from the user ID. Depth 1 returns C results where C in chunk_size, depth N returns N * C results. """

    end_point = self.req_url+ '/instagram/user/posts'
    payload = {'user_id':user_id, 'depth':depth, 'oldest_timestamp':oldest_timestamp, 'chunk_size':chunk_size, 'start_cursor':start_cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_posts_from_username(self, username, depth, oldest_timestamp, chunk_size=10, start_cursor=''):
    """ Fetch user posts from username using additional parameters. Depth 1 returns C results where C in chunk_size, depth N returns N * C results. """

    end_point = self.req_url+ '/instagram/user/posts-from-username'
    payload = {'username':username, 'depth':depth, 'oldest_timestamp':oldest_timestamp, 'chunk_size':chunk_size, 'start_cursor':start_cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_basic_info(self, user_id):
    """ Fetch basic user information from the user ID. """

    end_point = self.req_url+ '/instagram/user/basic-info'
    payload = {'user_id':user_id, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_info(self, username):
    """ Fetch user info from the username. """

    end_point = self.req_url+ '/instagram/user/info'
    payload = {'username':username, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_detailed_info(self, username):
    """ Fetch detailed user info from the username. """

    end_point = self.req_url+ '/instagram/user/detailed-info'
    payload = {'username':username, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_followers(self, user_id):
    """ Fetch number of followers from a user ID. """

    end_point = self.req_url+ '/instagram/user/followers'
    payload = {'user_id':user_id, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_following(self, user_id):
    """ Fetch number of following from a user ID. """

    end_point = self.req_url+ '/instagram/user/following'
    payload = {'user_id':user_id, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_igtv(self, user_id, depth):
    """ Fetch the user IGTV from the user ID. Depth 1 returns 10 results, depth N returns N * 10 results. """

    end_point = self.req_url+ '/instagram/user/igtv'
    payload = {'user_id':user_id, 'depth':depth, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_reels(self, user_id, depth, include_feed_video=True):
    """ Fetch the user Reels from the user ID. Depth 1 returns 10 results, depth N returns N * 10 results. """

    end_point = self.req_url+ '/instagram/user/reels'
    payload = {'user_id':user_id, 'depth':depth, 'include_feed_video':include_feed_video, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_post_details(self, code):
    """ Fetch post information and statistics from shortcode. """

    end_point = self.req_url+ '/instagram/post/details'
    payload = {'code':code, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_hashtag_posts(self, name, cursor):
    """ Fetch most recent posts containing hashtag. Each cursor returns ~ 30 posts """

    end_point = self.req_url+ '/instagram/hashtag/posts'
    payload = {'name':name, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
