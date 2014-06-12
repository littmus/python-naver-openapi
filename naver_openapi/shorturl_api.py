import sys
import urllib
import http


def _utf8(v):
    if isinstance(v, unicode):
        v = v.encode('utf-8')

    return v


class ShortURL(object):
    
    def __init__(self, key):
        self.host = 'http://openapi.naver.com/shorturl.json'
        self.key = key
        (major, minor, micro, releaselevel, serial) = sys.version_info
        self.user_agent = "Python/%d.%d.%d naver_openapi_shorturl/%s" % \
            (major, minor, micro, '?')

    def get_shorturl(self, url=None):
        if url is None:
            raise Exception
        
        params = dict(key=self.key, url=url)

        encoded_params = []
        for key, value in params.items():
            encoded_params.append((key, _utf8(value)))

        params = dict(encoded_params)

        request = '%(host)s?%(params)s' % {
            'host': self.host,
            'params': urllib.urlencode(params),
        }

        code, data = http.get(request, self.user_agent)

        return data



        
