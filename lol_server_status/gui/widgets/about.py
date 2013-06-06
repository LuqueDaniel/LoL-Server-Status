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
from lol_server_status import __version__
from lol_server_status import __author__
from lol_server_status import __license__
from lol_server_status import __source__

#PyQt4.QtGui imports
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QMessageBox

#PyQt4.QtCore imports
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL


class aboutWidget(QWidget):

    def __init__(self, parent=None):
        super(aboutWidget, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('LoL Server Status - About')
        self.setMinimumWidth(parent.width())
        self.move(parent.pos())
        self.setFocus(False)

        #label_title
        self.label_title = QLabel('LoL Server Status')
        self.label_title.setObjectName('label_title')
        self.label_title.setAlignment(Qt.AlignCenter)

        #label_source
        self.label_source = QLabel(
            'Source: <a style="color:#0073de" href="%s">Github repository</a>' %
            __source__)
        self.label_source.setOpenExternalLinks(True)

        #btn_about_qt
        self.btn_about_qt = QPushButton('About Qt')

        #General layout
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label_title)
        vbox.addWidget(QLabel('Version: %s' % __version__))
        vbox.addWidget(QLabel('Author: %s' % __author__))
        vbox.addWidget(QLabel('License: %s' % __license__))
        vbox.addWidget(self.label_source)
        vbox.addWidget(self.btn_about_qt)

        #CONNECT SGNALS
        self.connect(self.btn_about_qt, SIGNAL('clicked()'), self.open_about_qt)

    def open_about_qt(self):
        about_qt = QMessageBox.aboutQt(self, 'About Qt')

    def mousePressEvent(self, event):
        self.close()
