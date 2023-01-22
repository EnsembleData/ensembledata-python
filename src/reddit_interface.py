from base_interface import Interface_IH


class Reddit_I_IH(Interface_IH):

  def get_search(self, keyword, sorting, timing, depth):
    """ Fetch posts from a given keyword, filter by time and sort. """

    end_point = self.req_url+ '/reddit/search'
    payload = {'keyword':keyword, 'sorting':sorting, 'timing':timing, 'depth':depth, 'token':self.token_IH_API}
    
    r = self.send_request(end_point, payload)
    return r 
    
