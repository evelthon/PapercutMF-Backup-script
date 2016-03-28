# PapercutMF Backup script

**Make sure you test this before using on a production server.
Use at your own risk!**

### About
This is a shell script for creating a backup of up PapercutMF. It was created
for a CentOS7 installation. It also makes a copy of:
* any additional groups set in `additonal-groups.txt`
* the Samba config file, `smb.conf`.

### Setup
1. Edit _backup.py_ and set proper values for `base_folder`, `backup_additional_groups`,
`backup_samba_config`.
2. Test that everything work ok in a test environment by issuing the command `python backup.py`
3. Install on your production server and execute on specific time-frames with a `cron job`.

#### Note
* _base_folder_: The folder where PapercutMF was installed
* _backup_additional_groups_: True or False
* _backup_samba_config_: True or False