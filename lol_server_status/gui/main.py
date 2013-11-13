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
from lol_server_status import __prj__
from lol_server_status import __version__
from lol_server_status.resources import STYLES
from lol_server_status.resources import IMAGES
from lol_server_status.gui.widgets.central_widget import centralWidget

#PyQt4.QtGui imports
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QIcon

#PyQt4.QtCore imports
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtCore import QTextCodec
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSettings

#sys imports
import sys


class mainWindow(QMainWindow):
    """Main window for application"""

    def __init__(self):
        super(mainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumWidth(270)
        self.setWindowTitle('LoL Server Status')
        #Load app settings
        self.load_settings()

        #Init centralWidget
        self.setCentralWidget(centralWidget(self, self.update_time))

    def load_settings(self):
        """This function load the application settings"""

        qsettings = QSettings()

        self.move(qsettings.value('MainWindow/pos',
                self.frameGeometry().center()).toPoint())
        self.update_time = qsettings.value('configs/update_time', 0, type=int)

    def save_settings(self):
        """This function write the application settings"""

        qsettings = QSettings()

        qsettings.setValue('MainWindow/pos', self.pos())

    def closeEvent(self, event):
        """Close event"""
        self.save_settings()


def start():
    #Init Qt Application
    app = QApplication(sys.argv)

    #Set application organization, name and version
    QCoreApplication.setOrganizationName('lol-server-status')
    QCoreApplication.setApplicationName(__prj__)
    QCoreApplication.setApplicationVersion(__version__)

    #Set icon for application
    app.setWindowIcon(QIcon(IMAGES['icon_256']))

    #Codec for QString
    QTextCodec.setCodecForCStrings(QTextCodec.codecForName('utf-8'))

    #Add StyleSheet
    with open(STYLES, 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
        f.close()

    #Run user interface
    window = mainWindow()
    window.show()

    sys.exit(app.exec_())
