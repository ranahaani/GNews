
class GNewsException(Exception):
    """
    Base exception for the GNews library.
    All custom exceptions in this library inherit from this class.
    """
    pass


class RateLimitError(GNewsException):
    """
    Raised when the GNews API rate limit is exceeded.
    """
    pass


class InvalidConfigError(GNewsException):
    """
    Raised when the library is misconfigured or required settings are missing/invalid.
    """
    pass


class NetworkError(GNewsException):
    """
    Raised when network requests fail due to connectivity issues,
    DNS errors, timeouts, or unexpected response states.
    """
    pass





