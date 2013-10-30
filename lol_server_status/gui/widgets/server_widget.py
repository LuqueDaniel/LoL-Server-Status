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
from lol_server_status.resources import COLOR_SCHEME

#PyQt4.Qtgui imports
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QPalette
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QLinearGradient

#PyQt4.QtCore imports
from PyQt4.QtCore import QPointF
from PyQt4.QtCore import Qt


class serverWidget(QWidget):

    def __init__(self, parent=None, server=None):
        super(serverWidget, self).__init__()
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.Highlight)

        #Check status
        if server['status'] == 1:
            label_name = QLabel('%s' % (server['short_name'].upper()))
            label_status = QLabel('<font color="%s">%s</font>' % (
                                       COLOR_SCHEME['server_online'], 'ONLINE'))

            self.setToolTip('%s server is currently online' % (server['name']))

        elif server['status'] == 2:
            label_name = QLabel('%s' % (server['short_name'].upper()))
            label_status = QLabel('<font color="%s">%s</font>' % (
                                       COLOR_SCHEME['server_busy'], 'BUSY'))

            self.setToolTip('%s server is currently busy' % (server['name']))

        elif server['status'] == 0:
            label_name = QLabel('%s' % (server['short_name'].upper()))
            label_status = QLabel('<font color="%s">%s</font>' % (
                                     COLOR_SCHEME['server_offline'], 'OFFLINE'))

            self.setToolTip('%s server is currently offline' % (server['name']))

        else:
            label_name = QLabel('%s' % (server['short_name'].upper()))
            label_status = QLabel('<font color="%s">UNDEFINED</fon>' % (
                                    COLOR_SCHEME['server_undefined']))

            self.setToolTip("""%s server is currently undefined
check your internet connection""" % (server['name']))

        #set aligment
        label_name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_status.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        #General layout
        hbox = QHBoxLayout()
        hbox.addWidget(label_name)
        hbox.addWidget(label_status)

        self.setLayout(hbox)

    def paintEvent(self, event):
        """This function create gradient background"""

        painter = QPainter(self)
        start = QPointF(100, 0)
        stop = QPointF(100, 100)
        gradient = QLinearGradient(start, stop)
        gradient.setColorAt(1, QColor(COLOR_SCHEME['server_widget_bg1']))
        gradient.setColorAt(0, QColor(COLOR_SCHEME['server_widget_bg2']))
        painter.fillRect(self.rect(), gradient)
