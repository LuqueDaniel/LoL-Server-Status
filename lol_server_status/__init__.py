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


__prj__ = 'LoL Server Status'
__author__ = 'Daniel Luque'
__mail__ = 'danielluque14 at gmail dot com'
__source__ = 'http://github.com/LuqueDaniel/LoL-Server-Status'
__version__ = '1.1'
__license__ = 'GPLv3'
__docu__ = """LoL Server Status is an application for checking servers status of
League of Legends"""


def run():
    #Import lol_server_status CORE
    from lol_server_status import core

    core.run_lol_status_server()
