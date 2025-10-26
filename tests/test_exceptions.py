import pytest
from gnews.exceptions import (
    GNewsException,
    RateLimitError,
    InvalidConfigError,
    NetworkError,
)

def test_base_exception_inheritance():
    """All custom exceptions should inherit from GNewsException."""
    assert issubclass(RateLimitError, GNewsException)
    assert issubclass(InvalidConfigError, GNewsException)
    assert issubclass(NetworkError, GNewsException)

def test_exception_messages():
    """Check that each exception correctly stores its message."""
    with pytest.raises(RateLimitError, match="rate limit"):
        raise RateLimitError("rate limit exceeded")

    with pytest.raises(InvalidConfigError, match="invalid"):
        raise InvalidConfigError("invalid configuration")

    with pytest.raises(NetworkError, match="network"):
        raise NetworkError("network error")
