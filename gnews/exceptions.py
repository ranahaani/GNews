"""
Custom exception classes for the GNews library.

These exceptions provide more specific and descriptive
error messages, improving debugging and user experience.
"""

class GNewsException(Exception):
    """Base exception for all GNews-related errors."""
    pass


class RateLimitError(GNewsException):
    """Raised when the API rate limit is exceeded."""
    pass


class InvalidConfigError(GNewsException):
    """Raised when an invalid configuration is detected."""
    pass


class NetworkError(GNewsException):
    """Raised when a network-related issue occurs."""
    pass
