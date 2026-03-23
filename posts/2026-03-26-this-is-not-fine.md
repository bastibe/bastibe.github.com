---
title: 🔥 This is not fine 🔥
date: 2026-03-16
description: where I try to live with Linux
filetags: computers
---

So I was [annoyed with my Apple computer](https://bastibe.de/2026-03-05-apple-woes.html), and decided to try Linux again. I even got a fancy Framework Desktop to do it!

After a week, the hardware arrived. To be honest, I was a bit under-whelmed. It's a cute little black box, but at the end of the day, it is just a black box. Somehow I had hoped it would look a bit more classy. Oh well. At least it's very quiet.

Since I wanted color management in Linux, KDE is the only option until Gnome 50 is released next month. So I installed Fedora KDE. This worked well. All my hardware worked immediately, including the odd headphone amplifier, the weird flightsim controller, and the Apple touchpad. Even the two 4K160 P3 screens came up correctly without issues. Weirdly, the GPU was configured with merely 512 MB of memory by default. But a quick trip to the BIOS fixed that.

Much more annoying was installing apps. I like to use Darktable, Digikam, Signal, Spotify, Zen, and Zed. Installing these required installing AppImages, Flatpaks, and the odd RPM repo, and even hand-editing a few desktop shortcuts. I can deal with this, but elegant it is not. The rest of the software was of course trivially installed from the package repos.

Steam and games worked immediately without any trouble. But gaming performance in Microsoft Flight Simulator was merely good, I had hoped for a bit more.

Performance in Darktable was a bit of a letdown. I had thought the Framework Desktop would clearly outclass my Mac Studio M2. But it didn't. It was slower. After messing with stuff for a while, I found that the RustiCL runtime ran faster than RocM once you set up the environment variable. Fine, be that way. Not the end of the world.

I was less amused about KDE. This was my preferred environment in the past, but even compared to Liquid Glass, it was a bit of a mess. Why are some directory icons monochrome, and others colorful? Why are font sizes and rounding radii and colors inconsistent everywhere? Why do some apps scroll with inertia, and others don't? Why do apps crash frequently? I am apparently spoiled by MacOS.

Meanwhile I noticed that the computer did not recover from sleep correctly. USB would wake it, but then immediately die, so I couldn't enter my password and resume my session. I futzed with GRUB params and udev rules, but that didn't fix anything.

Then I wanted to set up a home banking app. I knew I'd have to use a Windows app for that, and thought Wine should easily be able to handle them. It. Did. Not. After a few hours of tinkering, I gave up. Alright, a VM then. I'd need one for printing and scanning anyways. So I tried to set up VirtualBox.

At this point the plot finally turned. Fedora does not include VirtualBox in its repos. There is hardly any documentation for anything on VirtualBox's website. Meanwhile the _third_ kernel update had installed, and this time it apparently broke the GPU driver. God damn it, I just want a running computer, not a tinkering box. And why do reboots take a long time?

Look, I really wanted to like this. But I'm already fighting with computers eight hours a workday, I don't need this shit at home. I'm not giving up just yet. I have now installed Ubuntu 25.10. It doesn't have proper color management yet, but that's only temporary until 26.04 releases. I'm still trying to make this work. But my patience is close to running out.
