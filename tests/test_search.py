import sys
import unittest
sys.path.append('../')
import naver_openapi

key = 'enter_your_key'


class NaverOpenApiSearchTests(unittest.TestCase):
    def setUp(self):
        self.search = naver_openapi.Search(key)

    def test_search_rank(self):
        self.search.rank()

    def test_search_book(self):
        self.search.book(query='the lord of the rings')

    def test_search_shop(self):
        self.search.shop()

    def test_search_(self):
        pass

if __name__ == '__main__':
    unittest.main()
