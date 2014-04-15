"""Defines the StartResponseMock class.

Copyright 2013 by Rackspace Hosting, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from falcon import util


class StartResponseMock:
    """Mock object that represents a WSGI start_response callable

    Attributes:
        call_count: Number of times start_response was called.
        status: HTTP status line, e.g. "785 TPS Cover Sheet not attached".
        headers: Headers array passed to start_response, per PEP-333
        headers_dict: Headers array parsed into a dict to facilitate lookups

    """

    def __init__(self):
        """Initialize attributes to default values"""

        self._called = 0
        self.status = None
        self.headers = None
        self.exc_info = None

    def __call__(self, status, headers, exc_info=None):
        """Implements the PEP-3333 start_response protocol"""

        self._called += 1
        self.status = status

        # NOTE(kgriffs): Normalize headers to be lowercase regardless
        # of what Falcon returns, so asserts in tests don't have to
        # worry about the case-insensitive nature of header names.
        self.headers = [(name.lower(), value) for name, value in headers]

        self.headers_dict = util.CaseInsensitiveDict(headers)
        self.exc_info = exc_info

    @property
    def call_count(self):
        return self._called
