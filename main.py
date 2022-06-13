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
import configparser
from Util import Util

#Get config
config = configparser.ConfigParser()
config.read(filesnap.cfg)

#Set app options

import datetime
import os
import configparser
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
baseline_on_off = settings['rebase']

#Database workers
db_worker = Db()

#check if rebase is needed
if baseline_on_off == 'Y':
    for subdir, dirs, files in os.walk(base_url):
        for file in files:
            print(os.path.join(subdir, file))
            f = os.path.join(subdir, file)
            #Make the new basline
            # file modification timestamp of a file
            m_time = os.path.getmtime(f)
            # convert timestamp into DateTime object
            dt_m = datetime.datetime.fromtimestamp(m_time)
            #file creation timestamp in float
            c_time = os.path.getctime(f)
            #convert creation timestamp into DateTime object
            dt_c = datetime.datetime.fromtimestamp(c_time)

            #Put it in the database
            db_worker.insert_file_info(f, dt_m)

else:

    for subdir, dirs, files in os.walk(base_url):
        root_dir_count = 0
        for file in files:
            f = os.path.join(subdir, file)
            #Make the new basline
            # file modification timestamp of a file
            m_time = os.path.getmtime(f)
            # convert timestamp into DateTime object
            dt_m = datetime.datetime.fromtimestamp(m_time)
            #file creation timestamp in float
            c_time = os.path.getctime(f)
            #convert creation timestamp into DateTime object
            dt_c = datetime.datetime.fromtimestamp(c_time)
            baseline_stamp = db_worker.get_modified_dates(f)
            #Check for the file insert if not logged
            try:
                file_check = db_worker.check_for_file(f)
                if file_check != f:
                    db_worker.insert_file_info(f, dt_m)
                else:
                    pass
            except:
                print("Something went wrong putting the file into the database.")
            #Confirm
            print(os.path.join(subdir, file))
            print(f"Current: {dt_m}")
            print(f"Baseline: {baseline_stamp[0][0]}")

            print(subdir)  
            if baseline_stamp[0][0] == dt_m:
                print("Not Changed")  
            else:
                print("Changed")
                if root_dir_count == 0:
                    print(subdir.rsplit('/', 1)[-1])
                    #print(f)
                    db_worker.update_base_folder(subdir, f)
                    root_dir_count = 1
                
                #Copy backed up file and change modified base date
                #try:

                
                #except:
                    
                #finally:
                #    db_worker.update_base_file_mod_time(f, m_time)

            


            
    


