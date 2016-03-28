#!/usr/bin/env python

import os
import datetime

base_folder = '/Installation_Folder'
backup_additional_groups = True
backup_samba_config = True

# Create the date part of the filename
today = datetime.datetime.today()
date_format = "%Y-%m-%dT%H-%M-%S"
s = today.strftime(date_format)

# Copy external groups file to /backup
if backup_additional_groups:
    os.system('cp ' + base_folder + '/server/data/conf/additional-groups.txt' + base_folder + '/server/data/backups/additional-groups-' + s + '.txt')


# Backup smb.conf
if backup_samba_config:
    os.system('cp /etc/samba/smb.conf ' + base_folder + '/server/data/backups/smb-' + s + '.conf')


'''
Perform an offline backup of PapercutMF by:
  1. Stop the app server
  2. Issue a DB export command
  3. Start the app server
'''
os.system(base_folder + '/server/bin/linux-x64/stop-server')
os.system(base_folder + '/server/bin/linux-x64/db-tools export-db')
os.system(base_folder + '/server/bin/linux-x64/start-server')


'''Delete backup files older than 3 months
3 x 31 days = 93
If you need a difference day period, alter accordingly'''

os.system('find ' + base_folder + '/server/data/backups/*.* -type f -mtime +93 | xargs rm')
