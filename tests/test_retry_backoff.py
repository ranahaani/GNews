"""Tests for HTTP 429 retry/backoff behaviour in ``GNews._get_news``."""
from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import patch

import pytest

from gnews import GNews
from gnews.exceptions import InvalidConfigError, RateLimitError


def _feed(status: int = 200, entries=None):
    return SimpleNamespace(status=status, entries=entries or [])


class TestRetryConfigValidation:
    def test_negative_max_retries_rejected(self):
        with pytest.raises(InvalidConfigError):
            GNews(max_retries=-1)

    def test_non_positive_backoff_rejected(self):
        with pytest.raises(InvalidConfigError):
            GNews(retry_backoff_base=0)
        with pytest.raises(InvalidConfigError):
            GNews(retry_backoff_max=0)


class TestBackoffDelay:
    def test_exponential_growth_capped(self):
        g = GNews(retry_backoff_base=1.0, retry_backoff_max=8.0)
        with patch("gnews.gnews.random.uniform", return_value=0.0):
            assert g._backoff_delay(0) == 1.0
            assert g._backoff_delay(1) == 2.0
            assert g._backoff_delay(2) == 4.0
            assert g._backoff_delay(3) == 8.0
            assert g._backoff_delay(10) == 8.0  # capped

    def test_jitter_added_within_base(self):
        g = GNews(retry_backoff_base=2.0, retry_backoff_max=100.0)
        with patch("gnews.gnews.random.uniform", return_value=1.5):
            # capped term = 2.0 * 2**1 = 4.0, jitter = 1.5
            assert g._backoff_delay(1) == 5.5


class TestRetryOn429:
    def test_succeeds_after_429_then_200(self):
        g = GNews(max_retries=3, retry_backoff_base=0.01, retry_backoff_max=0.01)
        calls = [_feed(429), _feed(200, entries=[])]
        with patch.object(g, "_fetch_feed", side_effect=calls) as fetch, \
             patch.object(g, "_sleep") as sleep:
            result = g._get_news("/search?q=test")
        assert result == []
        assert fetch.call_count == 2
        assert sleep.call_count == 1

    def test_raises_after_exhausting_retries(self):
        g = GNews(max_retries=2, retry_backoff_base=0.01, retry_backoff_max=0.01)
        with patch.object(g, "_fetch_feed", return_value=_feed(429)) as fetch, \
             patch.object(g, "_sleep") as sleep, \
             pytest.raises(RateLimitError):
            g._get_news("/search?q=test")
        # max_retries=2 means 3 total attempts and 2 sleeps between them
        assert fetch.call_count == 3
        assert sleep.call_count == 2

    def test_no_retry_when_disabled(self):
        g = GNews(max_retries=0, retry_backoff_base=0.01, retry_backoff_max=0.01)
        with patch.object(g, "_fetch_feed", return_value=_feed(429)) as fetch, \
             patch.object(g, "_sleep") as sleep, \
             pytest.raises(RateLimitError):
            g._get_news("/search?q=test")
        assert fetch.call_count == 1
        assert sleep.call_count == 0

    def test_non_429_does_not_retry(self):
        g = GNews(max_retries=3, retry_backoff_base=0.01, retry_backoff_max=0.01)
        with patch.object(g, "_fetch_feed", return_value=_feed(200, entries=[])) as fetch, \
             patch.object(g, "_sleep") as sleep:
            result = g._get_news("/search?q=test")
        assert result == []
        assert fetch.call_count == 1
        assert sleep.call_count == 0
