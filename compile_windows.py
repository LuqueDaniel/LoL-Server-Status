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


#LoL Server status imports
from lol_server_status import resources
import lol_server_status

#setuptools imports
from setuptools import find_packages

#distutils.core imports
from distutils.core import setup

#py2exe
import py2exe


packages = find_packages()


information = {'script': 'lol-server-status.py',
              'Version': lol_server_status.__version__,
              'copyright': lol_server_status.__license__,
              'name': lol_server_status.__prj__,
              'dest_base': lol_server_status.__prj__,
              'icon_resources': [(1, 'windows_icon.ico')]}


#Add resources files
resources_files = [('images', []), ('resources', [])]

#Add images
for img in resources.IMAGES.items():
    resources_files[0][1].append(img[1])

#Add styles
resources_files[1][1].append(resources.STYLES)


parameters = {
                'name': lol_server_status.__prj__,
                'version': lol_server_status.__version__,
                'description': lol_server_status.__docu__,
                'author': lol_server_status.__author__,
                'author_email': lol_server_status.__mail__,
                'license': lol_server_status.__license__,

                'windows': [information],

                'data_files': resources_files,
                'zipfile': None,
                'options': {
                    'py2exe': {
                        'dll_excludes': ['MSVCP90.dll'],
                        'compressed': 1,
                        'optimize': 2,
                        'includes': ['sip', 'win32com'],
                        'excludes': ['bsddb', 'curses', 'email',
                            'pywin.debugger', 'pywin.debugger.dbgcon',
                            'pywin.dialogs'],
                        'packages': packages,
                        'bundle_files': 1,
                        'dist_dir': 'dist',
                        'xref': False,
                        'skip_archive': False,
                        'ascii': False}
                    }
                }


setup(**parameters)
