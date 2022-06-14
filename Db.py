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
import sqlite3
from Util import Util
from time import gmtime, strftime


class Db(object):
    '''
    The Db performs database operations.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.conn = sqlite3.connect('filesnap.db')
        self.logger = Util()


    def insert_file_info(self, full_path, modify_date_time):

            try:
                cur = self.conn.cursor()
                cur.execute("INSERT INTO files (full_path,modify_date_time) VALUES ('{0}','{1}')".format(full_path,modify_date_time))

            except sqlite3.Error as err:
                self.logger.log_op("There is an error in the db class inserting file info.")
                self.logger.log_op(err)

            finally:
                self.conn.commit()
                cur.close()

    def get_modified_dates(self, path):
        cur = self.conn.cursor()
        cur.execute("SELECT modify_date_time FROM files where full_path = '{0}'".format(path))
        rows = cur.fetchall()
        if rows == None:
            rows = "None"
        return rows

    def update_base_folder(self, subdir, path):
        cur = self.conn.cursor()
        cur.execute("UPDATE files set base_folder = '{0}' where full_path = '{1}'".format(subdir, path))
        self.conn.commit()
        cur.close()

    def update_base_file_mod_time(self, path, new_stamp):
        cur = self.conn.cursor()
        cur.execute("UPDATE files set modify_date_time = '{0}' where full_path = '{1}'".format(new_stamp, path))
        self.conn.commit()
        cur.close()

    #check for the existence of 
    def check_for_file(self, path):
        cur = self.conn.cursor()
        cur.execute("SELECT full_path FROM files where full_path = '{0}'".format(path))
        rows = cur.fetchall()
        return rows
