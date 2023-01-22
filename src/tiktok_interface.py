from base_interface import Interface_IH


class Tiktok_I_IH(Interface_IH):

  def get_hashtag_posts(self, name, cursor):
    """ Fetch most relevant posts from a given hashtag. This Tiktok API returns max 5000 posts with this API. """

    end_point = self.req_url+ '/tt/hashtag/posts'
    payload = {'name':name, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_hashtag_info(self, name):
    """ Fetch information about an hashtag. """

    end_point = self.req_url+ '/tt/hashtag/info'
    payload = {'name':name, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_hashtag_recent_posts(self, name, days):
    """ Fetch all posts from the /hashtag/posts API (Tiktok returns max 5000) and only filter the ones from the last N days. """

    end_point = self.req_url+ '/tt/hashtag/recent-posts'
    payload = {'name':name, 'days':days, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_keyword_search(self, name, cursor, period, sorting, country='de', match_exactly=False, get_author_stats=False):
    """ Fetch posts from a given keyword and filter them by time. """

    end_point = self.req_url+ '/tt/keyword/search'
    payload = {'name':name, 'cursor':cursor, 'period':period, 'sorting':sorting, 'country':country, 'match_exactly':match_exactly, 'get_author_stats':get_author_stats, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_posts(self, username, depth, oldest_createtime, start_cursor=0, alternative_method=False):
    """ Fetch user posts from the username. """

    end_point = self.req_url+ '/tt/user/posts'
    payload = {'username':username, 'depth':depth, 'start_cursor':start_cursor, 'oldest_createtime':oldest_createtime, 'alternative_method':alternative_method, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_posts_from_secuid(self, secUid, depth, oldest_createtime, start_cursor=0, alternative_method=False):
    """ Fetch user posts from the secondary user ID. """

    end_point = self.req_url+ '/tt/user/posts-from-secuid'
    payload = {'secUid':secUid, 'depth':depth, 'start_cursor':start_cursor, 'oldest_createtime':oldest_createtime, 'alternative_method':alternative_method, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_info(self, username):
    """ Fetch user information and statistics from the username. """

    end_point = self.req_url+ '/tt/user/info'
    payload = {'username':username, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_info_from_secuid(self, secUid):
    """ Fetch user information and statistics from the secondary user ID. """

    end_point = self.req_url+ '/tt/user/info-from-secuid'
    payload = {'secUid':secUid, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_post_info(self, url, alternative_method=False):
    """ Fetch post information and statistics from URL. """

    end_point = self.req_url+ '/tt/post/info'
    payload = {'url':url, 'alternative_method':alternative_method, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_post_comments(self, aweme_id, cursor):
    """ Fetch comments for a given post. """

    end_point = self.req_url+ '/tt/post/comments'
    payload = {'aweme_id':aweme_id, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_post_comments_replies(self, aweme_id, comment_id, cursor):
    """ Fetch the replies to a comments for a given post. """

    end_point = self.req_url+ '/tt/post/comments-replies'
    payload = {'aweme_id':aweme_id, 'comment_id':comment_id, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_suggested(self, secUid, cursor):
    """ Fetch the users similar to the given one. """

    end_point = self.req_url+ '/tt/user/suggested'
    payload = {'secUid':secUid, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_music_posts(self, music_id, cursor):
    """ Fetch the posts containing a particular music. """

    end_point = self.req_url+ '/tt/music/posts'
    payload = {'music_id':music_id, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_music_info(self, name, cursor, sorting, filter_by):
    """ Fetch the info from a music string. """

    end_point = self.req_url+ '/tt/music/info'
    payload = {'name':name, 'cursor':cursor, 'sorting':sorting, 'filter_by':filter_by, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_followers(self, id, secUid, cursor):
    """ Fetch followers for a given user. """

    end_point = self.req_url+ '/tt/user/followers'
    payload = {'id':id, 'secUid':secUid, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
