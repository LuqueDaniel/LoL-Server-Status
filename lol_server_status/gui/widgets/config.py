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


#PyQt4.QtGui imports
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QVBoxLayout

#PyQt4.QtCore imports
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSettings


class configWidget(QWidget):

    def __init__(self, parent=None):
        super(configWidget, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('LoL Server Status - Config')
        self.setMinimumWidth(parent.width())
        self.move(parent.pos())
        self.setFocus(False)

        #label_title
        label_title = QLabel('Configurations')
        label_title.setObjectName('label_title')
        label_title.setAlignment(Qt.AlignCenter)

        #combo_update_time
        self.combo_update_time = QComboBox()
        for item in ("1 minute", "2 minutes", "5 minutes", "10 minutes",
                     "20 minutes"):
            self.combo_update_time.addItem(item)

        #LAYOUTS
        #layout_update_time
        layout_update_time = QHBoxLayout()
        layout_update_time.addWidget(QLabel('Update time:'))
        layout_update_time.addWidget(self.combo_update_time)

        #General layout
        vbox = QVBoxLayout(self)
        vbox.addWidget(label_title)  # Add label_title
        vbox.addLayout(layout_update_time)  # Add layout_update_time

        self.load_config()

    def save_config(self):
        """This function save settings"""

        qsettings = QSettings()
        qsettings.setValue('configs/update_time',
                           self.combo_update_time.currentIndex())

    def load_config(self):
        """This function load settings"""

        qsettings = QSettings()
        self.combo_update_time.setCurrentIndex(
                    qsettings.value('configs/update_time', 0, type=int))

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.save_config()
            self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.save_config()
            self.close()
