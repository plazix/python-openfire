# -*- coding: utf-8 -*-
"""
User Service Plugin
"""

import re

from base import OpenFireBase
from exception import (InvalidResponseException, UserServiceDisabledException, RequestNotAuthorisedException,
                       IllegalArgumentException, UserNotFoundException, UserAlreadyExistsException)

EXCEPTION_MAP = {
    'IllegalArgumentException': IllegalArgumentException,
    'UserNotFoundException': UserNotFoundException,
    'UserAlreadyExistsException': UserAlreadyExistsException,
    'RequestNotAuthorised': RequestNotAuthorisedException,
    'UserServiceDisabled': UserServiceDisabledException,
}

class UserService(OpenFireBase):
    def __init__(self, url, secret, api_path='plugins/userService/userservice'):
        """
        :param url:
        :param secret: The secret key that allows access to the User Service.
        :param api_path:
        """
        super(UserService, self).__init__(url, api_path)

        self.secret = secret

    def add_user(self, username, password, name=None, email=None, groups=None):
        """
        Add user

        :param username: The username of the user. ie the part before the @ symbol.
        :param password: The password of the user
        :param name: The display name of the user
        :param email: The email address of the user
        :param groups: List of groups where the user is a member
        """
        groups_str = None
        if groups:
            groups_str = ','.join(groups)

        return self._submit_request({
            'type': 'add',
            'username': username,
            'password': password,
            'name': name,
            'email': email,
            'groups': groups_str,
        })

    def delete_user(self, username):
        """
        Delete user

        :param username: The username of the user. ie the part before the @ symbol.
        """
        return self._submit_request({
            'type': 'delete',
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
        groups_str = None
        if groups:
            groups_str = ','.join(groups)

        return self._submit_request({
            'type': 'update',
            'username': username,
            'password': password,
            'name': name,
            'email': email,
            'groups': groups_str,
        })

    def lock_user(self, username):
        """
        Disable user

        :param username: The username of the user. ie the part before the @ symbol.
        """
        return self._submit_request({
            'type': 'disable',
            'username': username
        })

    def unlock_user(self, username):
        """
        Enable user

        :param username: The username of the user. ie the part before the @ symbol.
        """
        return self._submit_request({
            'type': 'enable',
            'username': username
        })

    def _build_query(self, params):
        params.update({'secret': self.secret})

        return super(UserService, self)._build_query(params)

    def _parse_response(self, data):
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
