"""Fetching Populi's public reference site. No key; it is a static site."""

from __future__ import annotations

import os
import time
import urllib.request
from urllib.parse import urlsplit

import httpx
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from .parse import BASE_URL

USER_AGENT = "populi-api-docs (WTS internal reference copy)"
DELAY_SECONDS = 0.25


class RetryableStatusError(Exception):
    pass


def proxy_for(url: str) -> str | None:
    """The proxy the environment names for `url`, if any.

    Read through the standard library, not httpx: httpx fails outright on a
    bracketed IPv6 entry in NO_PROXY (`[::1]`), which some local proxy setups
    write.
    """
    host = urlsplit(url).hostname or ""
    if urllib.request.proxy_bypass(host):
        return None
    return urllib.request.getproxies().get(urlsplit(url).scheme)


class Fetcher:
    def __init__(self, delay: float = DELAY_SECONDS) -> None:
        self.delay = delay
        self.client = httpx.Client(
            base_url=BASE_URL,
            headers={"User-Agent": USER_AGENT},
            timeout=30,
            follow_redirects=True,
            trust_env=False,
            proxy=proxy_for(BASE_URL),
            verify=os.environ.get("SSL_CERT_FILE") or True,
        )
        self._last = 0.0

    @retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential(multiplier=1, max=20),
        retry=retry_if_exception_type((httpx.TransportError, RetryableStatusError)),
        reraise=True,
    )
    def get(self, path: str) -> str:
        wait = self.delay - (time.monotonic() - self._last)
        if wait > 0:
            time.sleep(wait)
        self._last = time.monotonic()
        response = self.client.get(path)
        if response.status_code == 429 or response.status_code >= 500:
            raise RetryableStatusError(f"{path}: HTTP {response.status_code}")
        response.raise_for_status()
        return response.text

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> Fetcher:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
