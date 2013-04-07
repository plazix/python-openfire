# -*- coding: utf-8 -*-

class HTTPException(Exception):
    pass

class InvalidResponseException(Exception):
    pass

class UserServiceDisabledException(Exception):
    pass

class RequestNotAuthorisedException(Exception):
    pass

class IllegalArgumentException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class UserAlreadyExistsException(Exception):
    pass
