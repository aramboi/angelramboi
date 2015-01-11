Title: Different profiles for Firefox 3.6 and 4 beta on Windows
Date: 2010-11-08 13:14
Category: misc
Tags: firefox, profiles
Summary: This is one of those case when I miss a sane CLI in Windows.

When installing Mozilla Minefield (Firefox daily builds) on Ubuntu, it
automatically creates a new profile and copies your current profile
there. But on Windows this thing doesn't happen.

When installing Firefox 4b6 on Windows 7 the same profile as the regular
installation is used. This can cause a lot of problems, specially if you
use add-ons. Some of these problems are:

-   Most of the add-ons are disabled. Partial solution is to install the
    [Add-on Compatibility Reporter][1]
-   Sync add-on is disabled because it is build in Firefox now.
    Recommendation: do not sync your stable release with any beta/daily
    builds. I did this and after a while I got an error from the stable
    release that said I should update Sync, but there was no update
    available. So Sync didn't work for a while. This happened to me with
    Minefield b7.
-   The biggest problem is Firebug. The beta release (1.6) that works
    with Firefox 4 is buggy, becomes unusable sometimes and crashes the
    browser.

The solution is pretty straight forward. First we must create an
additional profile. To do this you must access the Firefox profile
manager. Go to your Firefox 3.6 shortcut properties and add "-P" to the
Target field. It should look like this:

    "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -P


Save and open Firefox with that shortcut. The profile manager windows
should appear (image bellow), click on Create Profile and create the
"beta" profile.

![Firefox Profile Manager][2]

To make the shortcut access the profile directly without the profile
manager window you have to edit once more the Target of the shortcut
like so:

    "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -P default

Also edit the Firefox beta shortcut like so:

    "C:\Program Files (x86)\Mozilla Firefox 4.0 Beta 6\firefox.exe" -P beta

That's it. Happy testing.

**UPDATE**: Another way to solve this is to install the [portable
version of Firefox beta][3].

[1]: https://addons.mozilla.org/en-US/firefox/addon/15003/
    "Add-on Compatibility Reporter"
[2]: /images/2011/firefox-profilemanager.jpg
    "Firefox profile manager"
[3]: http://portableapps.com/apps/internet/firefox_portable/test
    "Firefox portable"
