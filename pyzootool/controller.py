"""
Central point for pyzootool's control
"""
import httplib2
import hashlib

from pyzootool import items, users

class ZooControl():
    
    def __init__(self, apikey, username=None, password=None):
        """
        Arguments:
            apikey - Zootool.com API Key. REQUIRED
            username - Optional. Required for authenticated requests
            password - Optional. Required for authenticated requests
            
        Creates our httplib2, items and user objects.
        """
        self.apikey = apikey
        self.http = httplib2.Http()
        if username and password:
            hash = hashlib.sha1(password)
            self.http.add_credentials(username, hash.hexdigest())
            
        self.item = items.ZooItem(self.apikey, self.http)
        self.user = users.ZooUser(self.apikey, self.http)
        
    def __unicode__(self):
        if self.http.credentials.credentials:
            return u"ZooControl - Authenticated"
        return u"ZooControl - Unautheneticated"
        
    def __str__(self):
        return self.__unicode__()