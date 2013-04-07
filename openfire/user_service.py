# -*- coding: utf-8 -*-
"""
User Service Plugin
"""

try:
    # python 3
    from urllib.request import urlopen
    from urllib.error import URLError
except ImportError:
    # python 2
    from urllib2 import urlopen, URLError
import re

from exception import (HTTPException, InvalidResponseException, UserServiceDisabledException,
                       RequestNotAuthorisedException, IllegalArgumentException, UserNotFoundException,
                       UserAlreadyExistsException)

EXCEPTION_MAP = {
    'IllegalArgumentException': IllegalArgumentException,
    'UserNotFoundException': UserNotFoundException,
    'UserAlreadyExistsException': UserAlreadyExistsException,
    'RequestNotAuthorised': RequestNotAuthorisedException,
    'UserServiceDisabled': UserServiceDisabledException,
}

class UserService(object):
    def __init__(self, url, secret, api_path='plugins/userService/userservice'):
        """
        :param url:
        :param secret: The secret key that allows access to the User Service.
        :param api_path:
        """
        self.url = url
        self.secret = secret
        self.api_path = api_path

    def add_user(self, username, password, name=None, email=None, groups=None):
        """
        Add user

        :param username: The username of the user. ie the part before the @ symbol.
        :param password: The password of the user
        :param name: The display name of the user
        :param email: The email address of the user
        :param groups: List of groups where the user is a member
        """
        self.__submit_request('add', {
            'username': username,
            'password': password,
            'name': name,
            'email': email,
            'groups': groups,
        })

    def delete_user(self, username):
        """
        Delete user

        :param username: The username of the user. ie the part before the @ symbol.
        """
        self.__submit_request('delete', {
            'username': username
        })

    def update_user(self, username, password, name=None, email=None, groups=None):
        """
        Update user

        :param username: The username of the user. ie the part before the @ symbol.
        :param password: The password of the user
        :param name: The display name of the user
        :param email: The email address of the user
        :param groups: List of groups where the user is a member
        """
        self.__submit_request('update', {
            'username': username,
            'password': password,
            'name': name,
            'email': email,
            'groups': groups,
        })

    def lock_user(self, username):
        """
        Disable user

        :param username: The username of the user. ie the part before the @ symbol.
        """
        self.__submit_request('disable', {
            'username': username
        })

    def unlock_user(self, username):
        """
        Enable user

        :param username: The username of the user. ie the part before the @ symbol.
        """
        self.__submit_request('enable', {
            'username': username
        })

    def __submit_request(self, request_type, params):
        try:
            response = urlopen(self.__build_query(request_type, params))

            return self.__parse_response(response.read())
        except URLError, e:
            raise HTTPException(e.reason)

    def __build_query(self, request_type, params):
        params.update({'secret': self.secret, 'type': request_type})

        query_params = []
        for key in params:
            if params[key] is not None:
                query_params.append('%s=%s' % (key, params[key]))
        uri_query = '&'.join(query_params)

        return u'%s%s?%s' % (self.url, self.api_path, uri_query)

    def __parse_response(self, data):
        match = re.search(r'<error>(.*)</error>', data)
        if match:
            exception = match.group(1)
            if exception in EXCEPTION_MAP:
                raise EXCEPTION_MAP[exception]()
            else:
                raise InvalidResponseException()
        elif re.search(r'<result>ok</result>', data) is None:
            raise InvalidResponseException()

        return True
