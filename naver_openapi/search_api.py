import sys
import urllib
import http


def _utf8(v):
    if isinstance(v, unicode):
        v = v.encode('utf-8')
    #assert isinstance(v, str)

    return v


class Search(object):

    def __init__(self, key=None):
        self.host = 'http://openapi.naver.com/search'
        self.key = key
        (major, minor, micro, releaselevel, serial) = sys.version_info
        self.user_agent = "Python/%d.%d.%d naver_openapi_search/%s" % \
            (major, minor, micro, '?')

    def rank(self, target='rank', query='nexearch'):
        """
        @parameter target : rank / ranktheme
        @parameter query : nexearch / [themes]
        """
        if target == 'rank':
            if query != 'nexearch':
                raise Exception

        elif target == 'ranktheme':
            themes = ['movie', 'people', 'foreignactor', 'perform']
            themes += ['drama', 'broadcast', 'book']

            if query not in themes:
                raise Exception

        else:
            raise Exception

        params = dict(target=target, query=query)

        data = self._call(self.host, params)

        return data

    def book(self, target='book', query='', display=10, start=1, details=None):
        """
        @parameter display : maximum number is 100
        @parameter start : maximum number is 1000
        @parameter details : uses when target is book_adv, type must be dict
        """
        if target == 'book':
            pass

        elif target == 'book_adv':
            if details is None:
                raise Exception

            if len(details) == 0:
                raise Exception

            detail_keys = ['d_titl', 'd_auth', 'd_cont', 'd_isbn']
            """
            Parameter must include one above options
            when you uses advanced search.
            """
            detail_keys += ['d_dafr', 'd_dato', 'd_catg']
            for key in details:
                if key not in detail_keys:
                    raise Exception

        else:
            raise Exception

        params = dict(target=target, query=query, display=display, start=start)

        if target == 'book_adv':
            for key, value in details.items():
                params[key] = value

        data = self._call(self.host, params)

        return data

    def shop(self, target='shop', query='', display=10, start=1, sort='sim'):
        """
        @parameter sort : sorting options, [sim, date, asc, dsc]
        """
        if target != 'shop':
            raise Exception

        if sort not in ['sim', 'date', 'asc', 'dsc']:
            raise Exception

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def cafe(self, target='cafe', query='', display=10, start=1, sort='sim'):
        """
        @parameter sort : sorting options, [sim, member, newarticles, rank]
        """
        if target != 'cafe':
            raise Exception

        if sort not in ['sim', 'member', 'newarticles', 'rank']:
            raise Exception

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def recmd(self, target='recmd', query=''):
        if target != 'recmd':
            raise Exception

        params = dict(target=target, query=query)

        data = self._call(self.host, params)

        return data

    def kin(self, target='kin', query='', display=10, start=1, sort='sim'):
        """
        @parameter sort : sorting options, [sim, date, count, point]
        """
        if target != 'kin':
            raise Exception

        if sort not in ['sim', 'date', 'count', 'point']:
            raise Exception

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def movie(self, target='movie', query='', display=10, start=1, genre=None,
              country=None, yearfrom=None, yearto=None):
        """
        @parameter genre : str, range(1, 29), see http://goo.gl/RraCGu
        @parameter country : 
        @parameter yearfrom :
        @parameter yaerto : 
        """
        pass

    def car(self):
        pass

    def cafearticle(self):
        pass

    def adult(self):
        pass

    def image(self):
        pass

    def movieman(self):
        pass

    def encyc(self):
        pass

    def webkr(self):
        pass

    def errata(self):
        pass

    def doc(self):
        pass

    def local(self):
        pass

    def blog(self):
        pass

    def news(self):
        pass

    def shortcut(self):
        pass

    def _call(self, host, params):
        params['key'] = self.key

        encoded_params = []
        for key, value in params.items():
            encoded_params.append((key, _utf8(value)))

        params = dict(encoded_params)

        request = '%(host)s?%(params)s' % {
            'host': host,
            'params': urllib.urlencode(params),
        }

        code, data = http.get(request, self.user_agent)

        print code, data

        return data
