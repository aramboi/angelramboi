Title: Installing Firefox 4 beta with Adobe Flash Player on Ubuntu 64bit
Date: 2011-01-23 11:08
Category: misc
Tags: adobe, firefox, flash, ubuntu
Summary: Hint - you won't find it in the normal release channels.

You can get the latest Firefox build from the [launchpad ppa repositories][1],
but I found that the periodical beta release on Mozilla's website tends to be
more stable and usable than the daily builds.

Unfortunately the downloadable build is only 32bit, thus not compatible
with the installed plugins in Ubuntu 64bit version. After a bit of
research I found out how to solve this little problem.

First you need to download the [Firefox beta][2]. Then untar it to
either you home folder or to "/opt/" (I like this way better, but you
have to use sudo to copy files here). You can *cd* to that folder and
launch Firefox (use: *./firefox* or *./firefox -P* to be able to create
and/or choose your profile, more on that [here][3])

As you can see there are no plugins in the add-ons page. Copying the
plugin folder from the default installation does not work (duh!). So I
thought to myself: this is some kind of standalone Firefox installation,
then I would need a standalone version of Adobe Flash. And I found it
here: [http://www.adobe.com/support/flashplayer/downloads.html][4]. There
is a Linux version of the *Flash Player 10.1 Plugin content debugger*,
as it is called. Download it and untar it to the "plugins" folder in
your Firefox installation.

And there you have it, Adobe Flash Player in Firefox 4 beta. (Please
keep in mind that both Firefox and Flash need to be updated manually if
installed this way)

[1]: https://launchpad.net/~ubuntu-mozilla-daily/+archive/ppa
    "Mozilla PPA"
[2]: http://www.mozilla.com/en-US/firefox/all-beta.html
    "Mozilla Firefox Beta"
[3]: http://www.altshiftkill.com/2010/11/different-profiles-for-firefox-3-6-and-4-beta-on-windows/
    "Different profiles for Firefox 3.6 and 4 beta on Windows"
[4]: http://www.adobe.com/support/flashplayer/downloads.html
    "Flash Player download"
