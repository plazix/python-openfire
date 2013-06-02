# -*- coding: utf-8 -*-
"""
User Service Plugin.

See http://www.igniterealtime.org/projects/openfire/plugins/userservice/readme.html
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
    SUBSCRIPTION_REMOVE = -1
    SUBSCRIPTION_NONE = 0
    SUBSCRIPTION_TO = 1
    SUBSCRIPTION_FROM = 2
    SUBSCRIPTION_BOTH = 3

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

    def add_roster(self, username, item_jid, name=None, subscription=None):
        """
        :param username: The username of the user. ie the part before the @ symbol.
        :param item_jid: The JID of the roster item
        :param name: The display name of the new user
        :param subscription: Type of subscription
        """
        return self._submit_request({
            'type': 'add_roster',
            'username': username,
            'item_jid': item_jid,
            'name': name,
            'subscription': subscription
        })

    def update_roster(self, username, item_jid, name=None, subscription=None):
        """
        :param username: The username of the user. ie the part before the @ symbol.
        :param item_jid: The JID of the roster item
        :param name: The display name of the new user
        :param subscription: Type of subscription
        """
        return self._submit_request({
            'type': 'update_roster',
            'username': username,
            'item_jid': item_jid,
            'name': name,
            'subscription': subscription
        })

    def delete_roster(self, username, item_jid):
        """
        :param username: The username of the user. ie the part before the @ symbol.
        :param item_jid: The JID of the roster item
        """
        return self._submit_request({
            'type': 'delete_roster',
            'username': username,
            'item_jid': item_jid
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
