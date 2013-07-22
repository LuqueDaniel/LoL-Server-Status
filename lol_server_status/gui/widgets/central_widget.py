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


#LoL Server Status imports
from lol_server_status.resources import LIST_UPDATE_TIME
from lol_server_status.core.get_status import get_servers_status
from lol_server_status.gui.widgets.tittle_bar import titleBar
from lol_server_status.gui.widgets.server_widget import serverWidget
from lol_server_status.gui.widgets.about import aboutWidget
from lol_server_status.gui.widgets.config import configWidget

#PyQt4.QtGui imports
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout

#PyQt4.QtCore imports
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QTimer


class centralWidget(QWidget):

    def __init__(self, parent=None, updateTime=0):
        super(centralWidget, self).__init__()
        self.parent = parent
        self.setMouseTracking(True)

        #title_bar
        self.title_bar = titleBar(self, parent)

        #LAYOUTS
        #Title_bar layout
        title_bar_layout = QHBoxLayout()
        title_bar_layout.setContentsMargins(0, 0, 0, 8)
        title_bar_layout.addWidget(self.title_bar)

        #General Layout
        self.vbox = QVBoxLayout(self)
        self.vbox.addLayout(title_bar_layout)

        #Load servers
        self.load_server_widgets()

        #Set QTimer for update status
        self.timer = QTimer(self)
        self.timer.start(LIST_UPDATE_TIME[updateTime])

        #CONNECT SIGNALS
        self.connect(self.title_bar.button_about, SIGNAL('clicked()'),
                     self.open_about_window)
        self.connect(self.title_bar.button_config, SIGNAL('clicked()'),
                     self.open_config_window)
        self.connect(self.timer, SIGNAL('timeout()'), self.update_server_status)

    def load_server_widgets(self):
        #Load servers status
        servers = get_servers_status()

        #Instance servers widgets
        self.na = serverWidget(self, servers['NA'])
        self.euw = serverWidget(self, servers['EUW'])
        self.eune = serverWidget(self, servers['EUNE'])
        self.br = serverWidget(self, servers['BR'])
        self.lan = serverWidget(self, servers['LAN'])
        self.las = serverWidget(self, servers['LAS'])
        self.oce = serverWidget(self, servers['OCE'])
        self.tr = serverWidget(self, servers['TR'])
        self.ru = serverWidget(self, servers['RU'])
        self.pbe = serverWidget(self, servers['PBE'])

        #Add serverWidget to layout
        self.vbox.addWidget(self.na)
        self.vbox.addWidget(self.euw)
        self.vbox.addWidget(self.eune)
        self.vbox.addWidget(self.br)
        self.vbox.addWidget(self.lan)
        self.vbox.addWidget(self.las)
        self.vbox.addWidget(self.oce)
        self.vbox.addWidget(self.tr)
        self.vbox.addWidget(self.ru)
        self.vbox.addWidget(self.pbe)

    def update_server_status(self):
        #Remove serverWidget
        self.vbox.removeWidget(self.na)
        self.vbox.removeWidget(self.euw)
        self.vbox.removeWidget(self.eune)
        self.vbox.removeWidget(self.br)
        self.vbox.removeWidget(self.lan)
        self.vbox.removeWidget(self.las)
        self.vbox.removeWidget(self.oce)
        self.vbox.removeWidget(self.tr)
        self.vbox.removeWidget(self.ru)
        self.vbox.removeWidget(self.pbe)

        #Reload server widgets
        self.load_server_widgets()

    def open_about_window(self):
        """Open about dialog"""
        self.about = aboutWidget(self.parent)
        self.about.show()

    def open_config_window(self):
        """Open config dialog"""
        self.config = configWidget(self.parent)
        self.config.show()
