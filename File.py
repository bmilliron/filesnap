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
import datetime
import shutil
from Db import Db
from Util import Util
from time import gmtime, strftime
from pathlib import Path


class File(object):
    '''
    The Db performs database operations.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.logger = Util()
        self.script_path = Path(__file__, '..').resolve()
        self.config = configparser.ConfigParser()
        self.config.read(self.script_path.joinpath('filesnap.cfg'))
        self.paths = self.config['path_config']
        self.backupdest_path = self.paths['backup_base_dir']

    def backup_file(self, path):
        db_worker = Db()
        file_id = db_worker.get_file_id(path)
        backup_folder_path = self.backupdest_path
        backup_folder_name = datetime.datetime.now().strftime("%b_%d_%Y_%H_%M_%S")
        file_name = os.path.basename(path)
        full_backup_folder = f"{backup_folder_path}\{backup_folder_name}\{file_id[0][0]}_{file_name}"
        source_folder = path
        print(f"source_folder: {source_folder}")
        print(f"full_backup_folder: {full_backup_folder}")
        #Test that the folder exists
        try:
            is_file = os.path.isfile(f"{backup_folder_path}\{backup_folder_name}") 
            if is_file:
                pass
            else:
                os.mkdir(f"{backup_folder_path}\{backup_folder_name}")

        except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)

        try:
            shutil.copy(source_folder, full_backup_folder)

        except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
        #Check for the folder
        #create the folder
        # DO THIS shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given


