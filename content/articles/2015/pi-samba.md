Title: Turn a RaspberryPi into a simple NAS
Date: 2015-08-19
Category: articles
Slug: turn-raspberrypi-into-a-simple-nas-server
Tags: raspberrypi, nas
Description: This is my step-by-step guide on how to setup a RaspberryPi with an external USB HDD as a network accessed storage (NAS)

This is based on a fresh install of Rasbian downloaded from the [official site][1] and using a NTFS formated external USB drive.

### The setup

Install all the packages we need to save the day:

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install samba samba-common-bin ntfs-3g hdparm
```

Get the drive identifier (ex. sda):

```
$ sudo fdisk -l

Disk /dev/mmcblk0: 15.8 GB, 15803088896 bytes
4 heads, 16 sectors/track, 482272 cylinders, total 30865408 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0xa6202af7

        Device Boot      Start         End      Blocks   Id  System
/dev/mmcblk0p1            8192      122879       57344    c  W95 FAT32 (LBA)
/dev/mmcblk0p2          122880    30865407    15371264   83  Linux
Note: sector size is 4096 (not 512)

Disk /dev/sda: 2000.4 GB, 2000398929920 bytes
255 heads, 63 sectors/track, 30400 cylinders, total 488378645 sectors
Units = sectors of 1 * 4096 = 4096 bytes
Sector size (logical/physical): 4096 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disk identifier: 0xbc81592b

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1            2048   488263544  1953045988    7  HPFS/NTFS/exFAT
/dev/sda2   *   488263545   488378644      460400    c  W95 FAT32 (LBA)
```
My drive identifier is `sda` in this case, so for the rest of the guide I will use that. Please use the identifier returned for your case.

Lets create and set the permissions for the future shared folder, and add a setup line to `/etc/fstab` in order to mount it properly:

```
$ sudo mkdir -p /media/HDD && sudo chmod -R 777 /media/HDD/
$ sudo echo "/dev/sda1       /media/HDD      ntfs-3g defaults,noatime  0       0" >> /etc/fstab
$ sudo umount /dev/sda1 && sudo mount /dev/sda1
```

In the samba config `/etc/samba/smb.conf` uncomment the following lines:

```
security = user
socket options = TCP_NODELAY
```

And add this at the end:

```
[media]
    comment = Media share
    path = /media/HDD
    valid users = @users
    force group = users
    create mask = 0660
    directory mask = 0771
    writeable = yes
    browseable = yes
    guest ok  = no
    read only = no
```
This will allow all users that authenticate properly to access that folder with write access.

Test configuration and restart the server:

```
$ testparm
Load smb config files from /etc/samba/smb.conf
...
Loaded services file OK.
Server role: ROLE_STANDALONE
Press enter to see a dump of your service definitions

[global]
  ...
$ sudo service samba restart
```

Create a local user and add it to samba users:

```
$ sudo useradd <USERNAME> -m -G users
$ sudo passwd <USERNAME>
$ sudo smbpasswd -a <USERNAME>
```

And you're done. You should be able to find the server on the local network now and connect to it with the credentials provided above.

### Extras

#### SD card space

Saves ~1GB disk space on the system card:

```
$ sudo apt-get install deborphan
$ sudo apt-get purge wolfram-engine java-common oracle-java8-jdk
$ sudo apt-get remove --auto-remove --purge libx11-.*
$ sudo apt-get autoremove --purge $(deborphan)
```

#### Restricted folders

Here is a sample Samba config for a folder restricted to a certain user, path and read only:

```
[media-read-only]
  comment = Media Files Read-Only
  path = /media/HDD/path/to/read/only/media/files
  valid users = <USERNAME>
  force group = users
  create mask = 0660
  directory mask = 0771
  browseable = yes
  writeable = no
  guest ok  = no
  read only = yes
```

#### Power savings

If you want to spin-down your external hard drive when it's inactive, this should work on most drives:

```
$ sudo hdparm -S 240 /dev/sda
/dev/sda:
 setting standby to 240 (20 minutes)
```

Unfortunately it did not work on mine, so I had to do the following hack:

```
$ sudo hdparm -S 240 /dev/sda
/dev/sda:
 setting standby to 240 (20 minutes)
 HDIO_DRIVE_CMD(setidle) failed: Invalid argument

$ sudo ls -al /dev/disk/by-id/
total 0
drwxr-xr-x 2 root root 280 Jan  1  1970 .
drwxr-xr-x 6 root root 120 Jan  1  1970 ..
lrwxrwxrwx 1 root root   9 Jan  1  1970 ata-ST2000DM001-1E6164_W1E842SW -> ../../sda  # we are going to use this ID
lrwxrwxrwx 1 root root  10 Jan  1  1970 ata-ST2000DM001-1E6164_W1E842SW-part1 -> ../../sda1
lrwxrwxrwx 1 root root  10 Jan  1  1970 ata-ST2000DM001-1E6164_W1E842SW-part2 -> ../../sda2
lrwxrwxrwx 1 root root  13 Jan  1  1970 memstick-SD16G_0xc70001ff -> ../../mmcblk0
lrwxrwxrwx 1 root root  15 Dec  7 21:41 memstick-SD16G_0xc70001ff-part1 -> ../../mmcblk0p1
lrwxrwxrwx 1 root root  15 Dec  7 21:41 memstick-SD16G_0xc70001ff-part2 -> ../../mmcblk0p2
lrwxrwxrwx 1 root root   9 Jan  1  1970 scsi-SSeagate_Expansion_Desk_NA4KLXK2 -> ../../sda
lrwxrwxrwx 1 root root  10 Jan  1  1970 scsi-SSeagate_Expansion_Desk_NA4KLXK2-part1 -> ../../sda1
lrwxrwxrwx 1 root root  10 Jan  1  1970 scsi-SSeagate_Expansion_Desk_NA4KLXK2-part2 -> ../../sda2
lrwxrwxrwx 1 root root   9 Jan  1  1970 wwn-0x5000c50073e1147a -> ../../sda
lrwxrwxrwx 1 root root  10 Jan  1  1970 wwn-0x5000c50073e1147a-part1 -> ../../sda1
lrwxrwxrwx 1 root root  10 Jan  1  1970 wwn-0x5000c50073e1147a-part2 -> ../../sda2

$ sudo hdparm -B127 -S240 /dev/disk/by-id/ata-ST2000DM001-1E6164_W1E842SW # using the ID found above atributed to sda

/dev/disk/by-id/ata-ST2000DM001-1E6164_W1E842SW:
 setting Advanced Power Management level to 0x7f (127)
 HDIO_DRIVE_CMD failed: Invalid argument
 setting standby to 240 (20 minutes)
 HDIO_DRIVE_CMD(setidle) failed: Invalid argument
 APM_level	= 127
```

Don't worry about the errors, it works just fine. :)


[1]: https://www.raspberrypi.org/downloads/raspbian/
