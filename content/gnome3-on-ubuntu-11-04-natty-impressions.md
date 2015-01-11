Title: Gnome3 on Ubuntu 11.04 Natty (impressions)
Date: 2011-06-15 18:31
Category: misc
Tags: gnome3, ubuntu
Summary: Because Unity sucks and I got bored with Gnome 2.


I decided to take a leap of faith and install Gnome3 and gnome-shell on
my Ubuntu box.

First the installation:

    % sudo add-apt-repository ppa:gnome3-team/gnome3
    % sudo apt-get update
    % sudo apt-get dist-upgrade
    % sudo apt-get install gnome-shell

Some fixes after restart:

    % sudo apt-get purge unity scrollbar* gnome-accessibility-themes
    % sudo apt-get install gnome-themes-standard

Extra installs:

    % sudo apt-get install gnome-tweak-tool dconf-tools gnome-shell-extensions-common gnome-shell-extensions-user-theme

Edit startup applications (the shortcut is missing from the applications
list):

    % gnome-session-properties

If you want to revert everything:

    % sudo apt-get install ppa-purge
    % sudo ppa-purge ppa:gnome3-team/gnome3

Nice features I discovered so far:

-   the interface overall (nautilus looks great)
-   the quick access to applications using the Super key (this made me
    remove Gnome Do)
-   alt+tab separates applications from different workspaces, groups
    instances of the same application
-   dynamic workspace adding depending on your open applications
-   on dual monitor setup the second monitor does not flip over when
    switching workspaces (this behavior is configurable)

Annoyances:

-   a little slower than expected
-   crashes sometimes (not very often though)
-   a bug with menus inside maximized applications that use JDK ([bug \#777425][1])

On the way I stumbled upon a great Ubuntu resource site:
[http://www.webupd8.org/][2]

I found some nice gnome-shell related articles there:

-   [ThemeSelector: GNOME Shell Extension To Change Themes (With
    Previews)][3]
-   [GNOME Shell System Monitor Extension Gets A Preferences Dialog And
    Lots Of New Features][4]
-   [Move Icons From Message Tray To The Top GNOME Shell Panel (Top Bar)
    Using IconManager Extension][5]


[1]: https://bugs.launchpad.net/ubuntu/+source/openjdk-6/+bug/777425
[2]: http://www.webupd8.org/ "Web Upd8: Ubuntu / Linux blog"
[3]: http://www.webupd8.org/2011/04/themeselector-gnome-shell-extension-to.html
    "ThemeSelector: GNOME Shell Extension To Change Themes (With Previews)"
[4]: http://www.webupd8.org/2011/06/gnome-shell-system-monitor-extension.html
    "GNOME Shell System Monitor Extension Gets A Preferences Dialog And Lots Of New Features"
[5]: http://www.webupd8.org/2011/06/move-icons-from-message-tray-to-top.html
    "Move Icons From Message Tray To The Top GNOME Shell Panel (Top Bar) Using IconManager Extension"
