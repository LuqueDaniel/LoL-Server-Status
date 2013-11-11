# -*- coding: utf-8 -*-
#
# This file is part of LoL Server Status
#
# LoL Server Status is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# LoL Server Status is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LoL Server Status. If not, see <http://www.gnu.org/licenses/>.
#
# Source: <http://github.com/LuqueDaniel/LoL-Server-Status>


"""
    This module contain all functions for get server status of League of Legends
"""

#lol_server_status imports
from lol_server_status.resources import LOL_JSON_BASE_URL
from lol_server_status.resources import LOL_SERVERS

#json imports
from json import loads

#urllib2 imports
from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError

#socket import
import socket


def get_status(server_id, lang):
    """This function obtain status of a specific LoL server

    Parameters:
        server_id: Acronym of the LoL server. Example: NA is North America.
        lang: Principal language of the server.
    """

    url = LOL_JSON_BASE_URL % (server_id, lang)

    try:
        open_url = urlopen(url)
        read_url = open_url.read()
        response = loads(read_url[15:-2])
        return response['serverStatus']
    except URLError, error:
        return error.reason
    except HTTPError, error:
        return error.code
    except socket.error:
        pass


def get_servers_status():
    """This function return a dict with servers information"""

    servers_status = {}
    for server in list(LOL_SERVERS.items()):
        status = get_status(server[1]['id'], server[1]['lang'])

        servers_status[server[0]] = {'short_name': server[1]['short_name'],
                                     'name': server[1]['name'],
                                     'status': status,
                                     'status_url': server[1]['status_url']}

    return servers_status
