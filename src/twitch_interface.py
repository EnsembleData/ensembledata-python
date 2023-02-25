from base_interface import Interface_ED


class Twitch_I_ED(Interface_ED):

  def get_search(self, keyword, depth, type):
    """ Fetch results (videos/channels/games) from a given keyword. Depth 1 returns ~ 15 results, depth N returns ~ N * 15 results. """

    end_point = self.req_url+ '/twitch/search'
    payload = {'keyword':keyword, 'depth':depth, 'type':type, 'token':self.token_ED_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_videos(self, username, depth):
    """ Fetch a list of videos from the given channel. Depth 1 returns 10 results, depth N returns ~ N * 10 results. """

    end_point = self.req_url+ '/twitch/user/videos'
    payload = {'username':username, 'depth':depth, 'token':self.token_ED_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
  def get_user_followers(self, username):
    """ Fetch the number of followers for the given channel. """

    end_point = self.req_url+ '/twitch/user/followers'
    payload = {'username':username, 'token':self.token_ED_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
