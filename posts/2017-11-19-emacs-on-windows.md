---
title: Installing Emacs on Windows
date: 2017-11-19 00:00
filetags: emacs windows
---

The [official website](https://www.gnu.org/software/emacs/download.html#windows) states that you need to download Emacs from a [nearby GNU mirror](http://ftpmirror.gnu.org/emacs/windows). However, this does not install gnutls, which is required for installing packages from [melpa](http:_melpa-stable.milkbox.net_#_) or [marmalade](https:__marmalade-repo.org_). The [documentation](https://www.gnu.org/software/emacs/manual/html_node/emacs-gnutls/Help-For-Users.html) says that this can be obtained from [ezwinports](https://sourceforge.net/projects/ezwinports/files/).

However, I have found that this does not work any more: As of Emacs 25, Emacs is available in 64 bit, but ezwinport only supplies 32 bit binaries. I had to search a bit, but the (in retrospect, obvious) solution is to download the required binaries from [GnuTLS's website](https://gnutls.org/download.html), directly. Then unpack all `*.dll` from the `bin` directory to your Emacs's `bin` directory, and you are good to go.

This situation is really a bit sad. Installing Emacs should not be this hard. But there is [talk](https://lists.gnu.org/archive/html/emacs-devel/2017-10/msg00805.html) about providing a Windows installer for Emacs in one of the next versions, which will hopefully fix these issues.
