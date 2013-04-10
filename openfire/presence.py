# -*- coding: utf-8 -*-
"""
Presence Plugin
"""

from base import OpenFireBase
from exception import UserNotFoundException


class Presence(OpenFireBase):
    STATUS_AVAILABLE = 'available'
    STATUS_CHAT = 'chat'
    STATUS_AWAY = 'away'
    STATUS_XA = 'xa'
    STATUS_DND = 'dnd'
    STATUS_OFFLINE = 'offline'
    STATUS_FORBIDDEN = 'forbidden'

    RESPONSE_TYPE_IMAGE = 'image'
    RESPONSE_TYPE_TEXT = 'text'
    RESPONSE_TYPE_XML = 'xml'

    def __init__(self, url, api_path='plugins/presence/status'):
        """
        :param url:
        :param api_path:
        """
        super(Presence, self).__init__(url, api_path)

    def status(self, username, response_type=RESPONSE_TYPE_TEXT):
        """
        Check user status

        :param username: The username of the user. ie the part before the @ symbol.
        :param type:
        """
        return self._submit_request({
            'jid': self._get_full_username(username),
            'type': response_type
        })

    def _get_full_username(self, username):
        return u'%s@%s' % (username, self.hostname)

    def _parse_response(self, data):
        status = data.strip()
        if 'null' == status:
            raise UserNotFoundException()

        return status
