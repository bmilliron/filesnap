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
from util import Util
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

    def delete_articles(self):
        del_conn = self.conn.cursor()
        del_conn.execute("DELETE FROM NewsLinks")
        self.conn.commit()
        del_conn.close()


    def insert_article(self, pub_date, article_cat, link_url, link_title):

            try:

                cur = self.conn.cursor()
                cur.execute("INSERT INTO NewsLinks (linkCat,linkUrl,linkDate,articleTitle) VALUES ('{0}','{1}','{2}','{3}')".format(article_cat,link_url,pub_date,link_title))

            except sqlite3.Error as err:
                self.logger.log_op("There is an error in the db class inserting from insert_article().")
                self.logger.log_op(err)

            finally:
                self.conn.commit()
                cur.close()