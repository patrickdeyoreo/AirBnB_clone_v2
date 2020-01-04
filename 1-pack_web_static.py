#!/usr/bin/python3
"""
Create a tarball containing the contents of web_static
"""

from os.path import isfile
from time import strftime
from fabric.api import local


def do_pack():
    """
    Archive the contents of web_static
    """
    tgz = 'versions/web_static_{}.tgz'.format(strftime('%Y%m%d%H%M%S'))
    local('mkdir -p versions')
    local('tar -czf {} web_static'.format(tgz))
    return tgz if isfile(tgz) else None
