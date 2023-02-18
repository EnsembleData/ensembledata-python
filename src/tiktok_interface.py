from base_interface import Interface_IH


class Tiktok_I_IH(Interface_IH):

  def get_hashtag_posts(self, name, cursor):
    """ Fetch posts containing a given hashtag (according to Tiktok internal sorting).

A single call to this endpoint returns a maximum of 20 posts. The cursor can be incremented to fetch more posts. cursor=0 will fetch posts 1-20, cursor=20 will fetch posts 21-40 and so on. The maximum cursor which can be input is around 4000-5000 depending on the hashtag. """

    end_point = self.req_url+ '/tt/hashtag/posts'
    payload = {'name':name, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_hashtag_recent_posts(self, name, days):
    """ Fetch all the posts for a given hashtag and filter out any that are not from within the last N days.

This is a convenience endpoint which internally calls the 'Search Hashtag' endpoint repeatedly (iterating the cursor) to collect all the posts for a given hashtag in one api call. Additionally, any posts which were created more than N days ago are filtered out. max_depth is the total number of calls which need to be made to the 'Search Hashtag' endpoint to collect all the posts. The maximum value of max_depth is 250, given that 1 call retrieves 20 posts and a maximum of 5000 posts can be retrieved. The cost is divided by 4 to provide a 75% discount over manually making all the separate calls to the 'Search Hashtag' endpoint. """

    end_point = self.req_url+ '/tt/hashtag/recent-posts'
    payload = {'name':name, 'days':days, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_keyword_full_search(self, name, period, country='de'):
    """ Fetch posts for a given keyword according to filter based on time. This API manages automatically the pagination for our API keyword/search """

    end_point = self.req_url+ '/tt/keyword/full-search'
    payload = {'name':name, 'period':period, 'country':country, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_keyword_search(self, name, cursor, period, sorting, country='de', match_exactly=False, get_author_stats=False):
    """ Fetch posts for a given keyword according to filter based on time and sorting. Returns a maximum of 20 posts per call. """

    end_point = self.req_url+ '/tt/keyword/search'
    payload = {'name':name, 'cursor':cursor, 'period':period, 'sorting':sorting, 'country':country, 'match_exactly':match_exactly, 'get_author_stats':get_author_stats, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_posts(self, username, depth, oldest_createtime, start_cursor=0, alternative_method=False):
    """ Fetch user posts from the username. Depth 1 returns the 10 most recent chunk of posts, depth N returns the N * 10 most recent chunk of posts. """

    end_point = self.req_url+ '/tt/user/posts'
    payload = {'username':username, 'depth':depth, 'start_cursor':start_cursor, 'oldest_createtime':oldest_createtime, 'alternative_method':alternative_method, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_posts_from_secuid(self, secUid, depth, oldest_createtime, start_cursor=0, alternative_method=False):
    """ Fetch user posts from the secondary user ID. Depth 1 returns the 10 most recent chunk of posts, depth N returns the N * 10 most recent chunk of posts. """

    end_point = self.req_url+ '/tt/user/posts-from-secuid'
    payload = {'secUid':secUid, 'depth':depth, 'start_cursor':start_cursor, 'oldest_createtime':oldest_createtime, 'alternative_method':alternative_method, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_info(self, username):
    """ Fetch user information and statistics from the username. The data returned includes country, language, biography, profile picture, engagement statistics etc. """

    end_point = self.req_url+ '/tt/user/info'
    payload = {'username':username, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_info_from_secuid(self, secUid):
    """ Fetch user information and statistics from the secondary user ID. The data returned includes country, language, biography, profile picture, engagement statistics etc. """

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
    """ Fetch comments for a given post. Each request returns a chunk of 30 comments. The API pagination has to be managed using the cursor starting from 0. """

    end_point = self.req_url+ '/tt/post/comments'
    payload = {'aweme_id':aweme_id, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_post_comments_replies(self, aweme_id, comment_id, cursor):
    """ Fetch the replies to a comments for a given post. Each request returns a chunk of 30 replies to a comment. The API pagination has to be managed using the cursor starting from 0. """

    end_point = self.req_url+ '/tt/post/comments-replies'
    payload = {'aweme_id':aweme_id, 'comment_id':comment_id, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_music_posts(self, music_id, cursor):
    """ Fetch the videos which have a particular piece of music in the background. The music_id has to be found from other APIs. """

    end_point = self.req_url+ '/tt/music/posts'
    payload = {'music_id':music_id, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_music_info(self, name, cursor, sorting, filter_by):
    """ Fetch information about music based on a string. """

    end_point = self.req_url+ '/tt/music/info'
    payload = {'name':name, 'cursor':cursor, 'sorting':sorting, 'filter_by':filter_by, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_followers(self, id, secUid, cursor):
    """ Fetch followers for a given user. Each request returns a chunk of 100 followers. The API pagination has to be managed using the cursor starting from 0. """

    end_point = self.req_url+ '/tt/user/followers'
    payload = {'id':id, 'secUid':secUid, 'cursor':cursor, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
