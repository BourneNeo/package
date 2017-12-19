"""
Utility functions for managing execution context for an operation
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import threading

# TLS object to store the execution context of a request
TLS = threading.local()
TLS.ctx = None


def set_context(ctx):
    """
    Set the execution context in thread local storage

    :type: :class:`vmware.vapi.core.ExecutionContext`
    :param: Execution context
    """
    TLS.ctx = ctx


def clear_context():
    """
    Clear the execution context from thread local storage
    """
    TLS.ctx = None


def get_context():
    """
    Get the execution context from thread local storage

    :rtype: :class:`vmware.vapi.core.ExecutionContext` or :class:`NoneType`
    :return: The execution context if present
    """
    return getattr(TLS, 'ctx', None)
