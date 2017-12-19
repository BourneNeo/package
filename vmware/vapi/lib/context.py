"""
Factory methods for creating application context
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2011-2012 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


import uuid

from vmware.vapi.core import ApplicationContext
from vmware.vapi.lib.constants import OPID


def create_operation_id():
    """
    Create a new operation id. It is a randomly generated uuid

    :rtype: :class:`str`
    :return: Newly created operation id
    """
    return str(uuid.uuid4())


def create_default_application_context():
    """
    Create a default application context. The
    created context will only have opId.

    :rtype: :class:`vmware.vapi.core.ApplicationContext`
    :return: Newly created application context
    """
    return ApplicationContext({OPID: create_operation_id()})


def insert_operation_id(app_ctx):
    """
    Add an operation id to the application context if there is none present.
    If an operation id is present, then this is a no op.

    :type app_ctx: :class:`vmware.vapi.core.ApplicationContext`
    :param app_ctx: Application context
    """
    if app_ctx and OPID not in app_ctx:
        app_ctx.setdefault(OPID, create_operation_id())
