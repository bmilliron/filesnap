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

import os, configparser, sys
from datetime import datetime
from tempfile import TemporaryFile
from Db import Db
from File import File

#Params
root_dir_count = 0

#get config
config = configparser.ConfigParser()
config.read('filesnap.cfg')
paths = config['path_config']
settings = config['settings']
base_url = paths['base_dir']

#instances
db_worker = Db()
file_worker = File()

for subdir, dirs, files in os.walk(base_url):
    root_dir_count = 0
    for file in files:
        f = os.path.join(subdir, file)
        #Make the new basline
        # file modification timestamp of a file
        m_time = os.path.getmtime(f)
        # convert timestamp into DateTime object
        dt_m = datetime.fromtimestamp(m_time).replace(microsecond=0)
        #Convert
        dt_m_1 = str(dt_m)
        #final_modified time
        dt_m_2 = datetime.strptime(dt_m_1, "%Y-%m-%d %H:%M:%S")
        #String time
        dt_m_3 = str(dt_m_2)
        #file creation timestamp in float
        c_time = os.path.getctime(f)
        #convert creation timestamp into DateTime object
        dt_c = datetime.fromtimestamp(c_time)
        #Check for the file insert if not logged
        try:
            file_check = db_worker.check_for_file(f)
            if file_check:
                pass
                print(f"file_check: {file_check}")
                print(f"f: {f}")
            else:
                print(f"file_check: {file_check}")
                print(f"f: {f}")
                db_worker.insert_file_info(f, dt_m_2)
                baseline_stamp = db_worker.get_modified_dates(f)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
        #Confirm
        #print(os.path.join(subdir, file))
        #print(f"Current: {dt_m}")
        #print(f"Baseline: {baseline_stamp[0][0]}")
        #Get the dates the file was modified
        baseline_stamp = db_worker.get_modified_dates(f)
        print(f"baseline_stamp: {baseline_stamp[0][0]}")
        print(f"subdir: {subdir}")
        print(f"dt_m_2: {dt_m_2}")
        print(repr(baseline_stamp))
        print(repr(dt_m_3))
        if baseline_stamp[0][0] == dt_m_3 and baseline_stamp is not None:
            print("Not Changed") 
        else:
            print("Changed")
            if root_dir_count == 0:
                try:
                    #print(subdir.rsplit('/', 1)[-1])
                    #print(f)
                    db_worker.update_base_folder(subdir, f)
                    root_dir_count = 1
                    db_worker.update_base_file_mod_time(f, dt_m)
                    file_worker.backup_file(f)

                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            
            

            


            
    


