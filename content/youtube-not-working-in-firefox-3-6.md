Title: Youtube not working in Firefox 3.6
Date: 2010-11-08 16:54
Category: misc
Tags: firefox, youtube, dom, storage
Summary: DOM storage disabled? No cookies for you then.

For the past couple of days YouTube did not work properly when accessed
via Firefox 3.6 (at least on my home PC).

Here's how the front page looked:

![youtube][1]


I wasn't able to access any videos or my account. Also Firebug showed
about 10 JavaScript errors. But it worked OK in Google Chrome and
Internet Explorer.

So what was the problem?!? It seems that YouTube is not satisfied with
the normal cookie anymore and demands the DOM Storage feature to be
enabled, which allows more data to be stored on the client side. I also
read reports that Gmail has the same problem, but I was unable to
reproduce this on my computer.

I managed to get it working by going in **about:config** and changing
the **dom.storage.enabled** property to **true**.

The weird part is that YouTube works in Internet Explorer 8 even with
DOM Storage disabled.

**UPDATE**: The new version of Twitter doesn't work either if DOM
Storage is disabled.

[1]: /images/2011/youtube_no_thumbs.jpg
    "YouTube with no thumbs"
