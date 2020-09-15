Title: Install Ubuntu side by side with Windows 10 on an Alienware 13"
Date: 2015-11-10
Category: articles
Slug: install-ubuntu-on-alienware-13
Tags: ubuntu, windows
Description: The Alienware 13 is an awesome gaming rig, so of course the Linux the support is ... meh!

The Alienware 13 R2 (2015) laptop is probably the best compact gaming rig out there, so as you'd expect the Linux the support is underwhelming, to say the least. This setup assumes we want to keep the Windows 10 install and have a dual-boot system.

### Windows preparations

First we need to shrink the main Windows partition (a guide for that can be found [here][4] on _How-to Geek_). By default Dell makes some extra partitions for the recovery and the Windows installation kit. Also, Windows 10 adds its own two extra system partitions, so be careful not to mess those up. I did a backup of the Dell ones and deleted them, but you can keep them, it should be the same either way.

I was unable to to get enough space for Ubuntu without disabling the `Page File` and `System Restore`, shrink partition and enable them back again, but you might not have to.

I also disabled the `fastboot` feature provided since Windows 8. What this does is putting the computer in hibernation instead of completely turning it off when the user issues a shut down from the `Power` menu. This allows for faster startup times when turning the laptop back on, but it can interfere with restarting when you are trying to reboot to get into Ubuntu instead.

### Ubuntu install

Make sure you have a wired network connection before starting this, otherwise you won't be able to get the updates for the video and wi-fi cards.

When you get to the install menu you need to change the boot sequence a bit. With `Install Ubuntu` selected, press `e` and add `nomodeset` just after `splash`. Then `Ctrl+x` or `F10` to continue booting. You should be able to install the system as you normally would.

### Video drivers

I was unable to boot properly into Ubuntu after install and it was relatively hard to pinpoint the issue because the error messages would appear only briefly on screen. After some research I concluded that the video card was the culprit and had to install the proprietary drivers to get things working.

To do that boot into recovery mode by selecting `Advanced options for Ubuntu` and then the second option in the boot menu, the one that has appended `recovery menu` to the latest kernel version string. You will be presented with several options as seen below:

![Ubuntu recovery menu][3]

Choose the `Enable networking` option and press `OK`. After that is finished choose the option to `Drop into root shell prompt`. In the shell do:

```
$ ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:1c.4/0000:03:00.0 ==
model    : GM107M [GeForce GTX 960M]
modalias : pci:v000010DEd0000139Bsv00001028sd000006E1bc03sc02i00
vendor   : NVIDIA Corporation
driver   : xserver-xorg-video-nouveau - distro free builtin
driver   : nvidia-352-updates - distro non-free
driver   : nvidia-352 - distro non-free recommended

$ apt-get install nvidia-352  # the number must match the version you got above
$ nvidia-xconfig
$ reboot
```

There is a good part though to using proprietary driver, you can choose the video chipset the OS uses, either nVidia or Intel (which promises longer battery life). The not so cool part is that this switch does not happen on the fly and you have to log out and log in again to apply the change.

### Touchpad

Getting the Synaptic touchpad to work was a lucky find. After doing a lot of messing around with `xinput` and having little success, I found a seemingly unrelated post that suggested blacklisting the `i2c_hid` kernel module:

```
$ sudo echo "blacklist i2c_hid" >> /etc/modprobe.d/blacklist.conf
$ sudo reboot
```

### Wi-fi

##### **UPDATE:** This should work with Ubuntu 15.10 out of the box after install and system updates. They seem to have added the patch around 6th of December 2015.

The wi-fi was the nastiest part, and it seems to be a recurring theme when it comes to installing Linux on a more _bleeding edge_ laptop. My initial research found this bug report: "[Atheros Qualcomm Killer N1525 Wireless-AC [168c:003e] is not supported][1]" and it seemed like the chances were pretty slim on getting this working with 15.04 which had kernel 3.19 still.

For a while the solution was a patch from kernel upstream, but it was pretty ugly. Then a `dkms` package was released, namely `ath10k-dkms_1.0_all.deb` and then an updated version `ath10k-dkms_1.1_all.deb` (can't find any reliable download links any more, even though this might be the only way to get the wi-fi working in 15.04).

The solution should have came with the release of Ubuntu 15.10. Not only it is the most stable October version in quite a while, it also comes with kernel 4.2 which in theory should have included the binaries for the Killer NIC chipset, sadly it did not. The bug report description said it will be available via an `apt-get update` within a week, but I can't figure out when that edit was made to the ticket (they should have made a new post). So I ran out of patience and just downloaded the binaries from [kernel.org][2] and copied them over into `/lib/firmware/ath10k/`. Rebooted and everything works as it should.

### AlienFX

You are out of luck here, friend! Pressing `Fn+F12` does not turn off/on the keyboard lighting and the only lead I found on changing the light configuration was this Python package on [github][6], but is almost 2 years old and targeted at the M14xR1 model (did not test it on my machine).

The good news is that customizations done in Windows to any of the LEDs carries out to Ubuntu also.

### Conclusion

Alienware 13 R2 is a great and powerful gaming laptop, and with a bit of work it behaves really well under Linux also. I played the native Steam version of "Bioshock Infinite" on high settings with very good frame rate under Ubuntu 15.10, so I am very happy with how things turned up.

PS: For this blog post I wanted to do also a recording with "Bioshock Infinite" running native on Ubuntu, but the frame rates while recording were horrendous and lowering the settings would not have done the game justice.


[1]: https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1383184
[2]: https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/ath10k/QCA6174
[3]: /images/2015/ubuntu-recovery-mode-menu.png "Ubuntu recovery menu"
[4]: http://www.howtogeek.com/howto/windows-vista/resize-a-partition-for-free-in-windows-vista/
[5]: /images/2015/ubuntu-install-boot.png
[6]: https://github.com/ashwinm76/alienfx
