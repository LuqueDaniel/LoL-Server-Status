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


#lol_server_status import
import lol_server_status
from lol_server_status import resources

#cx_Freeze imports
from cx_Freeze import setup, Executable

#shutil imports
import shutil

#os imports
import os


#Check if exists dist folder
if os.path.exists('dist'):
    #remove dist folder
    shutil.rmtree('dist')
elif os.path.exists('build'):
    shutil.rmtree('build')

###############################################################################
# ADD RESOURCE FILES
###############################################################################

#Add image files
resources_files = [
    (x, x[len(resources.PROJECT_PATH)+1:]) for x in resources.IMAGES.values()]

#Add styles
resources_files.append(
    (resources.STYLES, resources.STYLES[len(resources.PROJECT_PATH)+1:]))

###############################################################################
# EXCLUDE MODULES
###############################################################################

module_excludes = ['email', 'Tkinter', 'unittest', 'curses', 'pywin.debugger',
                   'pywin.debugger.dbgcon', 'pywin.dialogs']

###############################################################################
# OPTIONS
###############################################################################

build_options = {
    "optimize": 2,
    "excludes": module_excludes,
    "base": "Win32GUI",
    "compressed": True,
    "create_shared_zip": True,
    "icon": "windows_icon.ico",
    "include_msvcr": False,  # MVisual C runtime DLLs
    "copy_dependent_files": True,
    "include_in_shared_zip": True,
    'include_files': resources_files}

###############################################################################
# SETUP
###############################################################################

setup(name=lol_server_status.__prj__,
      version=lol_server_status.__version__,
      description=lol_server_status.__docu__,
      author_email=lol_server_status.__mail__,
      license=lol_server_status.__license__,
      options={"build_exe": build_options},
      executables=[Executable("lol-server-status.py",
                              targetName="LoL Server Status.exe",
                              shortcutName="LoL Server Status.exe")])
