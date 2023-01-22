from base_interface import Interface_IH


class Youtube_I_IH(Interface_IH):

  def get_search(self, keyword, depth):
    """ Fetch posts from a given keyword. """

    end_point = self.req_url+ '/youtube/search'
    payload = {'keyword':keyword, 'depth':depth, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_channel_videos(self, browseId, depth):
    """ Fetch videos for a given channel. """

    end_point = self.req_url+ '/youtube/channel/videos'
    payload = {'browseId':browseId, 'depth':depth, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_channel_get_short_stats(self, id):
    """ Fetch statistics for a Youtube Short from its ID. """

    end_point = self.req_url+ '/youtube/channel/get-short-stats'
    payload = {'id':id, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_channel_followers(self, browseId):
    """ Fetch followers for a channel. """

    end_point = self.req_url+ '/youtube/channel/followers'
    payload = {'browseId':browseId, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_channel_name_to_id(self, name):
    """ Convert channel name to ID. """

    end_point = self.req_url+ '/youtube/channel/name-to-id'
    payload = {'name':name, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
