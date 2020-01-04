#!/usr/bin/python3
"""
Create a tarball containing the contents of web_static
"""

from time import strftime


def do_pack():
    """
    Archive the contents of web_static
    """
    # name = 'web_static_{}.tgz'.format(strftime('%Y%m%d%H%M%S'))
