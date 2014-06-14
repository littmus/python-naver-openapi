import sys
import urllib
import http
from exceptions import *


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
        raise APIServiceEndedException

        if target == 'rank':
            if query != 'nexearch':
                raise InvalidAPIArgumentsException

        elif target == 'ranktheme':
            themes = ['movie', 'people', 'foreignactor', 'perform']
            themes += ['drama', 'broadcast', 'book']

            if query not in themes:
                raise InvalidAPIArgumentsException

        else:
            raise InvalidArgumentsException

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
                raise InvalidArgumentsException

            if len(details) == 0:
                raise InvalidArgumentsException

            detail_keys = ['d_titl', 'd_auth', 'd_cont', 'd_isbn']
            """
            Parameter must include one above options
            when you uses advanced search.
            """
            detail_keys += ['d_dafr', 'd_dato', 'd_catg']
            # need to implement category verify
            for key in details:
                if key not in detail_keys:
                    raise InvalidArgumentsException

        else:
            raise InvalidArgumentsException

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
            raise InvalidArgumentsException

        if sort not in ['sim', 'date', 'asc', 'dsc']:
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def cafe(self, target='cafe', query='', display=10, start=1, sort='sim'):
        """
        @parameter sort : sorting options, [sim, member, newarticles, rank]
        """
        raise APIServiceEndedException

        if target != 'cafe':
            raise InvalidArgumentsException

        if sort not in ['sim', 'member', 'newarticles', 'rank']:
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def recmd(self, target='recmd', query=''):
        raise APIServiceEndedException

        if target != 'recmd':
            raise InvalidArgumentsException

        params = dict(target=target, query=query)

        data = self._call(self.host, params)

        return data

    def kin(self, target='kin', query='', display=10, start=1, sort='sim'):
        """
        @parameter sort : sorting options, [sim, date, count, point]
        """
        if target != 'kin':
            raise InvalidArgumentsException

        if sort not in ['sim', 'date', 'count', 'point']:
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def movie(self, target='movie', query='', display=10, start=1, genre=None,
              country=None, yearfrom=None, yearto=None):
        """
        @parameter genre : str, range(1, 29), see http://goo.gl/RraCGu
        @parameter country : [KR, JP, US, HK, GB, FR, ETC]
        @parameter yearfrom : mimimum year value
        @parameter yaerto : maximum year value
        """
        if target != 'movie':
            raise InvalidArgumentsException

        if genre is not None and int(genre) not in range(1, 29):
            raise InvalidArgumentsException

        countries = ['KR', 'JP', 'US', 'HK', 'GB', 'FR', 'ETC']
        if country is not None and country not in countries:
            raise InvalidArgumentsException

        if (yearfrom is None and yearto is not None) or \
           (yearfrom is not None and yearto is None):
            raise InvalidArgumentsException

        params = dict(target=target, query=query, display=display, start=start)

        if genre is not None:
            params['genre'] = genre

        if country is not None:
            params['country'] = country

        if yearfrom is not None and yearto is not None:
            params['yearfrom'] = yearfrom
            params['yearto'] = yearto

        data = self._call(self.host, params)

        return data

    def car(self, target='car', query='', display=10, start=1,
            yearfrom=None, yearto=None):
        raise APIServiceEndedException

        if target != 'car':
            raise InvalidArgumentsException

        if (yearfrom is None and yearto is not None) or \
           (yearfrom is not None and yearto is None):
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start,
            yearfrom=yearfrom, yearto=yearto
        )

        data = self._call(self.host, params)

        return data

    def cafearticle(self, target='cafearticle', query='', display=10, start=1,
                    sort='sim'):
        """
        @parameter sort : sorting options, [sim, date]
        """
        if target != 'cafearticle':
            raise InvalidArgumentsException

        if sort not in ['sim', 'date']:
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def adult(self, target='adult', query=''):
        if target != 'adult':
            raise InvalidArgumentsException

        params = dict(target=target, query=query)

        data = self._call(self.host, params)

        return data

    def image(self, target='image', query='', display=10, start=1, sort='sim',
              filter='all'):
        """
        @parameter sort : sorting options, [sim, date]
        @parameter filter : size filtering, [all, large, medium, small]
        """
        if target != 'image':
            raise InvalidArgumentsException

        if sort not in ['sim', 'date']:
            raise InvalidArgumentsException

        if filter not in ['all', 'large', 'medium', 'small']:
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start,
            sort=sort, filter=filter
        )

        data = self._call(self.host, params)

        return data

    def movieman(self, target='movieman', query='', display=10, start=1):
        raise APIServiceEndedException

        if target != 'movieman':
            raise InvalidArgumentsException

        params = dict(target=target, query=query, display=display, start=start)

        data = self._call(self.host, params)

        return data

    def encyc(self, target='encyc', query='', display=10, start=1):
        if target != 'encyc':
            raise InvalidArgumentsException

        params = dict(target=target, query=query, display=display, start=start)

        data = self._call(self.host, params)

        return data

    def webkr(self, target='webkr', query='', display=10, start=1,
              domain=None):
        """
        @parameter domain : specific site domain for search, #need to test
        """
        if target != 'webkr':
            raise InvalidArgumentsException

        params = dict(target=target, query=query, display=display, start=start)

        if domain is not None:
            params['domain'] = domain

        data = self._call(self.host, params)

        return data

    def errata(self, target='errata', query=''):
        if target != 'errata':
            raise InvalidArgumentsException

        params = dict(target=target, query=query)

        data = self._call(self.host, params)

        return data

    def doc(self, target='doc', query='', display=10, start=1):
        if target != 'doc':
            raise InvalidArgumentsException

        params = dict(target=target, query=query, display=display, start=start)

        data = self._call(self.host, params)

        return data

    def local(self, target='local', query='', display=10, start=1,
              sort='random'):
        """
        @parameter sort : sorting options, [random, comment, vote]
        """
        if target != 'local':
            raise InvalidArgumentsException

        if sort not in ['random', 'comment', 'vote']:
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def blog(self, target='blog', query='', display=10, start=1, sort='sim'):
        """
        @parameter sort : sorting options, [sim, date]
        """
        if target != 'blog':
            raise InvalidArgumentsException

        if sort not in ['sim', 'date']:
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def news(self, target='blog', query='', display=10, start=1, sort='date'):
        """
        @parameter sort : sorting options, [date, sim]
        """
        if target != 'blog':
            raise InvalidArgumentsException

        if sort not in ['date', 'sim']:
            raise InvalidArgumentsException

        params = dict(
            target=target, query=query, display=display, start=start, sort=sort
        )

        data = self._call(self.host, params)

        return data

    def shortcut(self, target='shortcut', query=''):
        raise APIServiceEndedException

        if target != 'shortcut':
            raise InvalidArgumentsException

        params = dict(target=target, query=query)

        data = self._call(self.host, params)

        return data

    def _call(self, host, params):
        params['key'] = self.key

        if 'dispaly' in params and params['display'] > 100:
            raise InvalidArgumentsException

        if 'start' in params and params['start'] > 1000:
            raise InvalidArgumentsException

        encoded_params = []
        for key, value in params.items():
            encoded_params.append((key, _utf8(value)))

        params = dict(encoded_params)

        request = '%(host)s?%(params)s' % {
            'host': host,
            'params': urllib.urlencode(params),
        }

        code, data = http.get(request, self.user_agent)

        return data

