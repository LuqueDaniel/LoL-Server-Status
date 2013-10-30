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
from lol_server_status.resources import IMAGES
from lol_server_status.gui.widgets.about import aboutWidget
from lol_server_status.gui.widgets.config import configWidget

#PyQt4.QtGui imports
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QToolButton
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QSizePolicy

#PyQt4.QtCore imports
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSize
from PyQt4.QtCore import SIGNAL


class titleBar(QWidget):

    def __init__(self, app=None):
        super(titleBar, self).__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.app = app

        #button_close
        button_close = QToolButton()
        button_close.setIcon(QIcon(IMAGES['close']))
        button_close.setIconSize(QSize(30, 14))

        #button_minimize
        button_minimize = QToolButton()
        button_minimize.setIcon(QIcon(IMAGES['minimize']))
        button_minimize.setIconSize(QSize(30, 14))

        #button_config
        button_config = QToolButton()
        button_config.setIcon(QIcon(IMAGES['config']))
        button_config.setIconSize(QSize(30, 14))
        button_config.setToolTip('Configuration')

        #button_about
        button_about = QToolButton()
        button_about.setIcon(QIcon(IMAGES['about']))
        button_about.setIconSize(QSize(30, 14))
        button_about.setToolTip('About LoL Server Status')

        #label_title
        label_title = QLabel('LoL Server Status')
        label_title.setAlignment(Qt.AlignCenter)

        #General layout
        hbox = QHBoxLayout(self)
        hbox.setMargin(0)
        hbox.setSpacing(1)
        hbox.addWidget(label_title)
        hbox.addWidget(button_about)
        hbox.addWidget(button_config)
        hbox.addWidget(button_minimize)
        hbox.addWidget(button_close)

        #CONNECT SIGNALS
        self.connect(button_about, SIGNAL('clicked()'), self.open_about_window)
        self.connect(button_config, SIGNAL('clicked()'),
                     self.open_config_window)
        self.connect(button_close, SIGNAL('clicked()'), self.app.close)
        self.connect(button_minimize, SIGNAL('clicked()'),
                     self.app.showMinimized)

    def open_about_window(self):
        """Open about dialog"""
        self.about = aboutWidget(self.app)
        self.about.show()

    def open_config_window(self):
        """Open config dialog"""
        self.config = configWidget(self.app)
        self.config.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.app.moving = True
            self.app.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.app.moving:
            self.app.move(event.globalPos() - self.app.offset)
