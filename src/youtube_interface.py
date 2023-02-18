from base_interface import Interface_IH


class Youtube_I_IH(Interface_IH):

  def get_search(self, keyword, depth):
    """ Fetch videos from a given keyword. Depth 1 returns ~ 20 videos, Depth N returns ~ 20 * N videos. """

    end_point = self.req_url+ '/youtube/search'
    payload = {'keyword':keyword, 'depth':depth, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_channel_videos(self, browseId, depth):
    """ Fetch videos for a given channel. Depth 1 returns ~ 25 videos, Depth N returns ~ 25 * N videos. """

    end_point = self.req_url+ '/youtube/channel/videos'
    payload = {'browseId':browseId, 'depth':depth, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_channel_shorts(self, browseId, depth):
    """ Fetch Youtube Shorts for a given channel. Depth 1 returns ~ 50 videos, Depth N returns ~ 50 * N videos. """

    end_point = self.req_url+ '/youtube/channel/shorts'
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
    """ Fetch the number of followers for a channel. """

    end_point = self.req_url+ '/youtube/channel/followers'
    payload = {'browseId':browseId, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_channel_name_to_id(self, name):
    """ Get the channel ID from the channel name. """

    end_point = self.req_url+ '/youtube/channel/name-to-id'
    payload = {'name':name, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
