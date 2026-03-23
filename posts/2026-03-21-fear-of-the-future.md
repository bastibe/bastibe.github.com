---
title: Linux on the Framework Desktop
date: 2026-03-26
description: where I grapple with existential uncertainty, and Linux
filetags: computers
---

I've been feeling unmoored lately. I changed roles at work, from a very comfortable programming position to a challenging new management role. At the same time, AI is threatening to take away the fun part of programming, and leave my profession a hollow shell. So when I relax and edit photos after work, it is with some pent up anxiety and insecurity.

Thus when Apple added their latest “liquid glass” insult to the injury that is modern macOS[^macos], it was the straw that broke the camel's back. I decided it was time to try the grass on the other side, and bought a Framework Desktop. That's a very fanciful small form factor computer that should combine great power in a compact and quiet case. Essentially the PC equivalent to my Mac Studio.

[^macos]: I have a long history of bitching about Apple computers ([2012](https://bastibe.de/2012-07-09-apple-is-failing-me.html), [2015](https://bastibe.de/2015-10-16-finder-woes.html), [2020](https://bastibe.de/2020-01-21-i-miss-my-mac.html), [2020](https://bastibe.de/2020-09-17-dear-computer-we-need-to-talk.html), [2026](https://bastibe.de/2026-03-05-apple-woes.html)).

In particular, I bought this computer specifically to run Linux. My first try with Fedora KDE [went poorly](https://bastibe.de/2026-03-26-this-is-not-fine.html). But the second try with Ubuntu 25.11 resulted in a very pleasant system!

[Compared to the Mac](https://bastibe.de/2023-04-21-os-customization-and-macos.html), GNOME was a breeze to customize to my liking. I replaced the built-in _Ubuntu Tiling Assistant_ extension with the [Tiling Shell](https://extensions.gnome.org/extension/7065/tiling-shell/) extension, to get <kbd>❖-Left</kbd>/<kbd>❖-Right</kbd> window snapping to work across multiple screens, and installed [Touchpad Gesture Customization](https://extensions.gnome.org/extension/7850/touchpad-gesture-customization/) for quad-swipe-up to enable the window switcher. Beyond that, the dock was already on the right, [where it should be](https://bastibe.de/2010-07-03-strangeness-of-widescreen-displays-in-modern-operating-systems.html) (_\*cough\*_ Microsoft), the file manager was fast and simple, and the whole system just worked very well and looked fairly good. All my hardware worked immediately. This was actually the nicest desktop environment I've used in a long while.

Of course there were details that annoyed me a bit. In particular, many apps could only spelling-correct a single language. Mouse acceleration was different from what I'm used to. More annoying was that the computer would not wake from sleep on USB input, if I had switched my KVM to a different source while it was asleep. I'm sure this could be fixed, but I didn't get to it. Well, and since I couldn't wake the computer by just mashing a few keys on the keyboard, I had to crawl under my desk to find the power button on the Framework Desktop, and it is not a good button: it can't be located by touch, wobbles a lot, and just feels cheap. A minor detail, but I felt it daily.

Installing apps was straight-forward. Most apps were either available in the repo or as flatpacks, including Zen, Spotify, Darktable, Thunderbird, Obsidian, DigiKam, Publii, Zed, Signal, and Telegram. There were minor gripes such as the odd window frame not looking right, but that's not something I get hung up on. Only three applications required a VM, for banking, scanning, and photo printing. This was expected, and fine. Affinity was the only application that I'd really need to find an alternative for, but I don't foresee much of a problem with that.

In terms of hardware, the Framework Desktop is a very nice machine. Perhaps I'd have preferred a few more USB ports, and a bit more style than a simple black box. But at the end of the day, it was simply sitting under my desk, and it's certainly pretty enough for that. The fan kept quiet at all times. 

Performance was good, but not much of an upgrade over my current setup:

| Task                                             | Framework | Mac[^mac]       |
| ------------------------------------------------ | --------- | --------------- |
| Darktable [61MP benchmark][bench] export         | 3.4s      | 6.0s            |
| Darktable [61MP benchmark][bench] interact[^int] | 0.30s     | 0.25s           |
| Darktable [24MP benchmark][bench] export         | 1.2s      | 1.2s            |
| Darktable [24MP benchmark][bench] interact[^int] | 0.45s     | 0.25s           |

| Task                                             | Framework | Handheld[^deck] |
| ------------------------------------------------ | --------- | --------------- |
| Gaming: MSFS2020 high preset[^msfs]              | 35 FPS    | 30 FPS          |
| Gaming: MSFS2020 medium preset[^msfs]            | 45 FPS    | 40 FPS          |
| Gaming: System Shock medium preset               | 25 FPS    | 35 FPS          |

[^mac]: A Mac Studio M2 Pro with 32 GB of memory, my previous computer.
[^deck]: A Legion Go S Z1 16G running SteamOS. I play almost exclusively on the handheld, but was considering streaming from the Framework to the handheld for more demanding titles.
[^int]: The time it takes to change the first exposure instance, as measured by `darktable -d perf`.
[^msfs]: On the Framework, at 50% resolution scale (1080p), on the handheld, at 66% resolution scale (720p). That's not a fair comparison, but it's how I'd play them.
[bench]: https://darktable.info/en/system-ui-2/performance-analysis/performance-analysis-why/

These are not fair performance comparisons, but they represent how I use my computer. The Framework did of course run games a bit faster than my handheld, but only 50% more frames for 4x the TDP was less than expected. Darktable performance was actually a bit of a downgrade to my Mac, probably due to relatively poor driver support for OpenCL[^opencl]. But all of that is fine.

[^opencl]: That's with the RustiCL implementation, and pinned memory enabled. ROCm was significantly slower.

Overall, it has to be said, the Framework Desktop turned out to be an awesome system! It does everything I'd hoped for, while being small and quiet and unobtrusive. Truly a great machine.

But, through all of this ordeal of installing Fedora, seeing it _break_ very disconcertingly before my eyes, setting it up again with Ubuntu, figuring things out, blogging about it... _I wasn't having fun_. This new computer was actually wonderful, but it did not fix my annoyance with computers in general, nor my general unease with the direction the tech industry is going. This is of course perfectly obvious in retrospect, but wasn't apparent to me when it overlapped with various other annoyances.

So, a big fat recommendation for the Framework Desktop, and Linux on the Desktop, if that's your jam. But the Framework Desktop was a complication I didn't need, so I'll stick with MacOS for the time being, and work through my other problems first.
