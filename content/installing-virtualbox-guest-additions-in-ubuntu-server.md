Title: Installing VirtualBox Guest Additions in Ubuntu Server
Date: 2011-01-06 20:47
Category: misc
Tags: ubuntu, virtualbox
Summary: Getting shared folders to work for non-GUI virtual machines.

If you need to use features like "Shared folders" in Virtualbox guests
you have to install the Guest Additions. With Ubuntu desktop or Windows
this is a breeze, but I couldn't find a unified guide on how to do it in
a server environment.

First you need to install these:

    % sudo apt-get install dkms
    % sudo apt-get install build-essential linux-headers-`uname -r`

Make sure the VBoxGuestAdditions.iso is mounted.

![vbox-image][1]

Reboot system. Then do:

    % sudo mkdir /media/cdrom
    % sudo mount /dev/sr0 /media/cdrom
    mount: block device /dev/sr0 is write-protected, mounting read-only
    % cd /media/cdrom
    % sudo ./VBoxLinuxAdditions-x86.run

If you have 64bit Ubuntu you should run the *VBoxLinuxAdditions-amd64.run* file.

**UPDATE:** VirtualBox 4.0 merged the two files in one,
*VBoxLinuxAdditions.run*. Also the above image is not accurate for this
version, use 'Install Guest Additions...' (Host+D) to load the virtual
drive.

You should see something like this:

    Verifying archive integrity... All good.
    Uncompressing VirtualBox 3.2.12 Guest Additions for Linux........
    VirtualBox Guest Additions installer
    Removing installed version 3.2.10 of VirtualBox Guest Additions...
    Uninstalling old VirtualBox DKMS kernel modules ...done.
    Building the VirtualBox Guest Additions kernel modules
    Doing non-kernel setup of the Guest Additions ...done.
    You should restart your guest to make sure the new modules are actually used
    Installing the Window System drivers ...fail!
    (Could not find the X.Org or XFree86 Window System.)

Don't worry about the windows system drivers error as you don't use them
on Ubuntu server edition.

After reboot you will be able to mount your shared folders like so:

    % sudo mount -t vboxsf shared_folder_name /path/to/folder

To mount the shared folders automatically every time you boot, add  this
line (without the *sudo*) to the end of */etc/init.d/rc.local*.

To uninstall the guest additions use:

    % sudo /opt/VBoxGuestAdditions*/uninstall.sh

[1]: /images/2011/vbox.jpg "VirtualBox Additions"
