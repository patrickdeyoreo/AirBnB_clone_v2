#!/usr/bin/python3
"""
Archive and deploy the contents of web_static
"""

from time import strftime


def do_pack():
    """
    Archive the contents of web_static
    """
    # name = 'web_static_{}.tgz'.format(strftime('%Y%m%d%H%M%S'))


def do_deploy(archive_path):
    """
    Deploy an archive to Holberton web servers
    """
