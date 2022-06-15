"""
Filesnap - File snapshot backup utility
Copyright 2022 Ben Milliron
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
You can email inquiries to sapadian@protonmail.com
"""

import sys
import os
import configparser
import time
import datetime

class Util(object):
    '''
        Performs misc. utility operation
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.logger = Util()
        self.config = configparser.ConfigParser()
        self.config.read('filesnap.cfg')
        self.settings = self.config['settings']
        self.log_dir = self.paths['log_file_path']

    def get_url(self, feed_name):
        config = configparser.ConfigParser()
        config.read('app.cfg')
        url = config['urls'][feed_name]

        return url

    def log_op(self, msg):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
        log_file_path = self.log_dir
        log_file = open(log_file_path, 'a')
        log_file.write("{0}{1}".format(st, "\n"))
        log_file.write("{0}{1}".format(msg, "\n"))
        log_file.close()