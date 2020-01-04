#!/usr/bin/python3
"""
Create a tarball containing the contents of web_static
"""

from os import path
from shlex import quote
from time import strftime
from fabric.api import local


def do_pack():
    """
    Archive the contents of web_static
    """
    now = strftime('%Y%m%d%H%M%S')
    tgz = path.join('versions', 'web_static_{}.tgz'.format(now))
    local('mkdir -p versions')
    local('tar -czf {} web_static'.format(quote(tgz)))
    return tgz if path.isfile(tgz) else None
