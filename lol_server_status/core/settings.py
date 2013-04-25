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


#PyQt4.QtCore imports
from PyQt4.QtCore import QSettings


def return_update_time():
    """This function return update time for QTimer"""

    #Load QSettings
    qsettings = QSettings()

    #List with time in milliseconds
    LIST_UPDATE_TIME = [60000, 120000, 300000, 600000, 1800000]

    return LIST_UPDATE_TIME[qsettings.value('configs/update_time', 0, type=int)]
