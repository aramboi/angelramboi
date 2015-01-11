Title: Keyboard shortcuts for Pidgin menu items
Date: 2011-01-23 11:30
Category: misc
Tags: pidgin, windows
Summary: Crouching config, hidden settings.

If you migrated from Yahoo Messenger! to Pidgin you probably found out
that some handy keyboard shortcuts are missing and no alternatives are
defined by default.

For example, I used to *Ctrl+h* to hide/show my offline buddies, but I
didn't have a shortcut for that in Pidgin. I did not find a working
solution on the *interwebs*. Also tried a bunch of plugins, but they
didn't cover the offline buddies part.

So I decided to poke around in the Pidgin configuration folder *.purple*
and I found this file: ***accels***. I did a leap o faith, uncommented
and edited this part:

    (gtk\_accel\_path "\<PurpleMain\>/Buddies/Show/Offline Buddies" "\<Control\>h")

Restarted Pidgin and it worked. There's a bunch of unused actions in
that file so feel free to experiment. :)
