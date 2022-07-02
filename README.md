# **Filesnap - File snapshot backup utility**

## **Introduction**

Filesnap was designed to track modified times of files, and if changes are made to the files it will make backups of the modified files to individual directories in the configured backup location.

Filesnap is designed to be run via cron or another scheduler.  The program has been tested on Windows and Ubuntu Linux, but should run on varying versions of Linux and Windows operating systems.

Performance has been tested antidotically with a base directory containing approximately 20,000 files, with a run time of approximately 1 minute 30 seconds. CPU performance averaged around 25% on a dual core CPU, this will vary depending on your server or VM configuration.

## **Usage**

Configuration is done via the filesnap.cfg file. The frequency of the running of the application can be done via your scheduler of choice. To run, schedule python to run the main.py file. The code was test on varying versions of Python 3.

## **Configuration Parameters**

**base_dir** - This is the path to the directory that is to be tracked for modified files.

**backup_base_dir** - This is the path to the directory that will be user to store your modified file backups.

**log_file_path** - This is the path to your Filesnap log file, where operations will be logged.

## Road Map
A rough list of features I would like to add include:

**2022 - 2023**
 - Compression of back up directory files
 - Multiple base directory targets
 - Multiple backup directory targets

## License

Copyright 2022 Ben Milliron
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

You can email inquiries to sapadian@protonmail.com
