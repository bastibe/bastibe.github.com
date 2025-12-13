---
title: Matlab and Audio Files
date: 2015-04-22 00:00
filetags: matlab audio
---

So I wanted to work with audio files in Matlab. In the past, Matlab could only do this with `auread` and `wavread`, which can read _*.au_ and _*.wav_ files. With 2012b, Matlab introduced [`audioread`](http://mathworks.com/help/matlab/ref/audioread.html), which claims to support _*.wav_, _*.ogg_, _*.flac_, _*.au_, _*.mp3_, and _*.mp4_, and simultaneously deprecated `auread` and `wavread`.

Of these file formats, only _*.au_ is capable of storing more than 4 Gb of audio data. But the documentation is actually wrong: `audioread` can _actually_ read more data formats than documented: it reads _*.w64_, _*.rf64_, and _*.caf_ no problem. And these can store more than 4 Gb as well.

It's just that, while `audioread` supports all of these nice file formats, [`audiowrite`](http://mathworks.com/help/matlab/ref/audiowrite.html) is more limited, and only supports _*.wav_, _*.ogg_, _*.flac_, and _*.mp4_. And it does not support any undocumented formats, either. So it seems that there is no way of writing files larger than 4 Gb. But for the time being, `auwrite` is still available, even though deprecated. I tried it, though, and it didn't finish writing 4.8 Gb in half an hour.

In other words, Matlab is incapable of writing audio files larger than 4 Gb. It just can't do it.
