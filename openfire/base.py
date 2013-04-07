# -*- coding: utf-8 -*-

try:
    # python 3
    from urllib.request import urlopen
    from urllib.error import URLError
    from urllib.parse import urlparse
except ImportError:
    # python 2
    from urllib2 import urlopen, URLError
    from urlparse import urlparse

from exception import HTTPException


class OpenFireBase(object):
    def __init__(self, url, api_path):
        """
        :param url:
        :param api_path:
        """
        self.url = url
        self.api_path = api_path

        uri = urlparse(self.url)
        self.hostname = uri.hostname

    def _submit_request(self, params):
        try:
            response = urlopen(self._build_query(params))

            return self._parse_response(response.read())
        except URLError, e:
            raise HTTPException(e.reason)

    def _build_query(self, params):
        query_params = []
        for key in params:
            if params[key] is not None:
                query_params.append('%s=%s' % (key, params[key]))
        uri_query = '&'.join(query_params)

        return u'%s%s?%s' % (self.url, self.api_path, uri_query)

    def _parse_response(self, data):
        raise NotImplementedError()
