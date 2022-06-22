class AuthFailed(Exception):
    """Exception to be raised when auth fails (timeout, server restart, or 5xx error)"""

class FinalActionExecuted(Exception):
    """Exception for the final action being execute so that nothing else happens"""

class PleaseAuth(Exception):
    """Exception if you have not authed and try to preform an auth action"""

class YouAreNotTheOwner(Exception):
    """Exception if you are not the owner and you try to preform an action in which you need to be owner to preform"""

class MustBeFunction(Exception):
    """Exception if something is not a function but must be"""

class ForceType(Exception):
    """Exception if type should be forced but is not"""