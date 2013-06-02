# -*- coding: utf-8 -*-

VERSION = (0, 2, 3, 'beta', 0)

from exception import (HTTPException, InvalidResponseException, UserServiceDisabledException,
                       RequestNotAuthorisedException, IllegalArgumentException, UserNotFoundException,
                       UserAlreadyExistsException)

from user_service import UserService
from presence import Presence


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    else:
        if VERSION[3] != 'final':
            version = "%s %s" % (version, VERSION[3])
            if VERSION[4] != 0:
                version = '%s %s' % (version, VERSION[4])
    return version
