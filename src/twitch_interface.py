from base_interface import Interface_IH


class Twitch_I_IH(Interface_IH):

  def get_search(self, keyword, depth, type):
    """ Fetch results (videos / channels / games) from a given keyword. """

    end_point = self.req_url+ '/twitch/search'
    payload = {'keyword':keyword, 'depth':depth, 'type':type, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_videos(self, username, depth):
    """ Fetch a list of videos from the given channel. """

    end_point = self.req_url+ '/twitch/user/videos'
    payload = {'username':username, 'depth':depth, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_followers(self, username):
    """ Fetch the number of followers for the given channel. """

    end_point = self.req_url+ '/twitch/user/followers'
    payload = {'username':username, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
