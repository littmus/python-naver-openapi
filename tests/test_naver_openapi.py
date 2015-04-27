# -*- coding:utf-8 -*-
import sys
import unittest
sys.path.append('../')
import naver_openapi
from naver_openapi.exceptions import APIServiceEndedException

search_key = '47049ea16d6227d365092fb3fb7fe9c7'
shorturl_key = '32996a710d730b2009c5aa220b3f4cff'


class NaverOpenApiSearchTests(unittest.TestCase):
    def setUp(self):
        self.search = naver_openapi.Search(search_key)

    def test_search_rank(self):
        self.assertRaises(APIServiceEndedException, self.search.rank)
        self.assertRaises(APIServiceEndedException, self.search.rank,
                            target='ranktheme', query='foreignactor')

    def test_search_book(self):
        self.search.book(query='the lord of the rings')
        details = dict(d_titl='harry potter')
        self.search.book(target='book_adv', query='harry potter',
                         details=details)

    def test_search_shop(self):
        self.search.shop(query=u'컴퓨터')

    def test_search_cafe(self):
        self.assertRaises(APIServiceEndedException, self.search.cafe,
                            query=u'사진 찍기')

    def test_search_recmd(self):
        self.assertRaises(APIServiceEndedException, self.search.recmd,
                            query='nhn')

    def test_search_kin(self):
        self.search.kin(query=u'바퀴벌레 없애는 법')

    def test_search_movie(self):
        self.search.movie(query=u'아이언맨')
        self.search.movie(query='love', genre='5', country='FR')

    def test_search_car(self):
        self.assertRaises(APIServiceEndedException, self.search.car,
                            query='BMW')
        self.assertRaises(APIServiceEndedException, self.search.car,
                            query='Ferrari', yearfrom=1990, yearto=2000)

    def test_search_cafearticle(self):
        self.search.cafearticle(query=u'인테리어')

    def test_search_adult(self):
        self.search.adult(query=u'건전')
        self.search.adult(query=u'야동')

    def test_search_image(self):
        self.search.image(query=u'자전거')
        self.search.image(query='landscape', filter='large')

    def test_search_movieman(self):
        self.assertRaises(APIServiceEndedException, self.search.movieman,
                            query='robert downey jr.')

    def test_search_encyc(self):
        self.search.encyc(query=u'광복절')

    def test_search_webkr(self):
        self.search.webkr(query=u'국내 여행')
        self.search.webkr(query=u'휴학', domain='www.koreapas.net')

    def test_search_errata(self):
        self.search.errata(query='vkdlTjs')
        self.search.errata(query=u'대하민국')

    def test_search_doc(self):
        self.search.doc(query=u'맥주')

    def test_search_news(self):
        self.search.news(query=u'월드컵')

    def test_search_shortcut(self):
        self.assertRaises(APIServiceEndedException, self.search.shortcut, 
                            query=u'백악관')


class NaverOpenApiShortURLTests(unittest.TestCase):
    def setUp(self):
        self.shorturl = naver_openapi.ShortURL(key=shorturl_key)

    def test_shorturl(self):
        shorturl = self.shorturl.get_shorturl(url='www.naver.com')
        #self.assertEqual(
        #print shorturl


if __name__ == '__main__':
    unittest.main()
