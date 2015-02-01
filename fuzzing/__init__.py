# coding=utf-8
"""Tools for development.

Logger.
Random testing tool.

Copyright (c) 2015 Stefan Braun

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from .log import LoggerFactory
from .fuzzer import fuzzer, fuzz_string, FuzzExecutor, TestStatCounter, Status
import logging


# Symbols available when importing with *.
__all__ = ['LoggerFactory', 'fuzzer', 'fuzz_string', 'FuzzExecutor', 'TestStatCounter', 'Status']


# Configure NullHandler to prevent warning in case logging is not configured.
# See https://docs.python.org/2/howto/logging.html#library-config
logging.getLogger('fuzzing').addHandler(logging.NullHandler())
