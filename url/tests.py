import random

from django.test import TestCase
from url.views import UrlDetailViewSet
from django.http import HttpRequest

# Create your tests here.


class TestUrlApis(TestCase):

    def setUp(self):
        self.objects=[
            {
                "url": "https://www.google.com/",
                "use_limit": 2

            },
            {
                "url": "https://www.facebook.com/?query=1&place=2",
                "use_limit": 3

            }

        ]








    def test_creation(self):
        url_viewset = UrlDetailViewSet()
        url_viewset.format_kwarg = {}

        response_dict=[]
        request_obj = HttpRequest()
        for obj in self.objects:
            request_obj.data = obj

            url_viewset.request = url_viewset

            response = url_viewset.create(request_obj)
            response_dict.append(response.data)

        print('---Creation Successful---')

        for r in response_dict:
            for lim in range(r['use_limit']):
                res_get=url_viewset.get_by_hash(request_obj,hashed_url=r['hashed_url'])
                if res_get.status_code!=200:
                    self.fail('creation failed')


        for r in response_dict:
            res_get = url_viewset.get_by_hash(request_obj, hashed_url=r['hashed_url'])
            if res_get.status_code!=404:
                self.fail('limit test failed')

        print('---Limit Test Successful---')










