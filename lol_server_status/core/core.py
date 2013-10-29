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


#lol_server_status imports
from lol_server_status.gui import main

#sys imports
import sys


def run_lol_server_status():
    """Run LoL Server status"""

    #Change the process name only for GNU/Linux
    #Since kernel version 2.6.9
    if sys.platform != 'win32' and sys.platform != 'darwin':
        try:
            from ctypes import CDLL
            libc = CDLL('libc.so.6')  # Loading C library
            procname = 'LoLServerStatus'
            #Change process name
            #15 value is PR_SET_NAME see "/usr/include/linux/prctl.h"
            libc.prctl(15, '%s\0' % procname, 0, 0, 0)
        except:
            pass

    #START GUI
    main.start()
