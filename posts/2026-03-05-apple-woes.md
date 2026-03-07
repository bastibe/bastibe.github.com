---
title: Apple: enough is enough
date: 2026-03-05
description: where I list my grievances with Apple computers
filetags: computers
---

Yesterday, my wife wanted to use Discord on her Apple laptop. It was right there in the applications folder. But MacOS couldn't find it. Launching it manually took several minutes, for some reason.

We wanted to download a clip using yt_dlp (a Python program). Terminal told us, this would require dev tools (which it doesn't). So we installed Python from python.org instead, which worked. Except, that non-blessed python could not access the internet because of some MacOS "security" feature.

Another "security" feature requires all apps on Apple computers to be notarized, even the ones I built myself. This used to have a relatively easy workaround (right click, open, accept the risk). Now it needs a terminal command.

I maintain a python library for playing and recording real-time audio from the system's sound cards. On some Apple systems, this fails to show any audio devices, "for security reasons".

I live and work in a multi-lingual environment, and regularly switch between the German and English keyboard layout. Lately, the keyboard layout no longer sticks. It resets to English when I press shift. Sometimes it does work, sometimes it doesn't. 

The German keyboard layout for MacOS on non-Apple keyboards is insane. So I made my own layout. This is relatively easy, and worked well. Except, every few OS updates, it reinstates Apple's insane layout.

Sometimes my Mac does not wake from sleep. Pressing the power button does nothing. Hitting keyboard keys does nothing. Only a long-press of the power button eventually reboots it. The power button on the Mac Studio is in an insane place of course.

There is no indication anywhere that the hard drive is getting full. **Edit:** A commenter pointed out that as of 2022, there is at least a _Storage_ page in _System Settings_ → _General_ → _Storage_. Better than nothing.

There is no simple way to reset the computer to factory conditions. **Edit:** A commenter pointed out that this does exist as of 2021, in _System Settings_ → _General_ → _Transfer or Reset_ → _Erase All Content and Settings..._. 

Gaming is largely impossible, even though the hardware is very capable.

Apple computers ship with a backup program called Time Machine. Except Time Machine invariably corrupts its own backup after a few months. Sometimes this can be recovered with some command line surgery, sometimes it can't. In which case, the backup needs to be rebuilt from scratch, and all previous history is lost. I have observed this on many Apple computers with many Time Machine volumes, from Apple's own hardware to external hard drives, to network drives. The only reliable option is to not use Time Machine.

Mac OS is getting less user friendly and usable with every release. Previously, when you renamed a file in Finder.app, Apple's anemic file manager, the file would not immediately re-sort, but wait a second, so as to allow me to arrow over to the next file. This was useful, but it was removed. I won't even explain the new "liquid glass" design.

Suffice it to say, I have ordered a Linx PC, which will replace the Mac. I've had enough. It will require wine for two apps, and a VM for two others. At this point, that's a price I'm willing to pay.
