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


#os import
from os import path

#sys import
import sys


###############################################################################
# PATHs
###############################################################################

# For Py2exe and cx_freeze
if getattr(sys, 'frozen', False):
    # py2exe and cx_freeze
    PROJECT_PATH = path.abspath(path.dirname(sys.executable))
else:
    #Project_path
    PROJECT_PATH = path.abspath(path.dirname(__file__))

###############################################################################
# STYLES
###############################################################################

STYLES = path.join(PROJECT_PATH, 'resources', 'styles.qss')

###############################################################################
# IMAGES
###############################################################################

IMAGES = {'icon_256': path.join(PROJECT_PATH, 'images', 'icon_256.png'),
          'close': path.join(PROJECT_PATH, 'images', 'close.png'),
          'minimize': path.join(PROJECT_PATH, 'images', 'minimize.png'),
          'config': path.join(PROJECT_PATH, 'images', 'config.png'),
          'about': path.join(PROJECT_PATH, 'images', 'about.png')}

###############################################################################
# THEME
###############################################################################

COLOR_SCHEME = {
    'server_online': '#73d217',
    'server_offline': 'red',
    'server_busy': '#d27c17',
    'server_undefined': '#d2d017',
    'server_widget_bg1': '#252525',
    'server_widget_bg2': '#2e2e2e'
    }

###############################################################################
# URLS
###############################################################################

LOL_JSON_BASE_URL = "http://ll.leagueoflegends.com/pages/launcher/%s?lang=%s"

###############################################################################
# LEAGUE OF LEGENDS SERVERS
###############################################################################

LOL_SERVERS = {'NA': {'id': 'na',
                       'short_name': 'na',
                       'lang': 'en',
                       'name': 'North America'},

                'EUW': {'id': 'euw',
                        'short_name': 'euw',
                        'lang': 'en',
                        'name': 'EU West'},

                'EUNE': {'id': 'eune',
                         'short_name': 'eune',
                         'lang': 'en',
                         'name': 'EU Nordic & East'},

                'BR': {'id': 'br',
                       'short_name': 'br',
                       'lang': 'pt',
                       'name': 'Brazil'},

                'TR': {'id': 'tr',
                       'short_name': 'tr',
                       'lang': 'tr',
                       'name': 'Turkey'},

                'RU': {'id': 'ru',
                       'short_name': 'ru',
                       'lang': 'ru',
                       'name': 'Russia'},

                'LAN': {'id': 'la1',
                        'short_name': 'lan',
                        'lang': 'es',
                        'name': 'Latin America North'},

                'LAS': {'id': 'la2',
                        'short_name': 'las',
                        'lang': 'es',
                        'name': 'Latin America South'},

                'OCE': {'id': 'oce',
                        'short_name': 'oce',
                        'lang': 'en',
                        'name': 'Oceanic'},

                'PBE': {'id': 'pbe',
                        'short_name': 'pbe',
                        'lang': 'en',
                        'name': 'Public Beta Environment'}}

###############################################################################
# LIST_UPDATE_TIME
###############################################################################

LIST_UPDATE_TIME = [60000, 120000, 300000, 600000, 1800000]
