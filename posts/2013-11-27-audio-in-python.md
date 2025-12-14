---
title: Sound in Python
date: 2013-11-27 00:00
filetags: python audio
---

Have you ever wanted to work with audio data in Python? I know I do. I want to record from the microphone, I want to play sounds. I want to read and write audio files. If you ever tried this in Python, you know it is kind of a pain.

It's not for a lack of libraries though. You can read sound files using [wave](http://docs.python.org/2/library/wave.html), SciPy provides [scipy.io.wavfile](http://docs.scipy.org/doc/scipy/reference/tutorial/io.html#module-scipy.io.wavfile), and there is a SciKit called [scikits.audiolab](http://scikits.appspot.com/audiolab). And except for `scikits.audiolab`, these return the data as raw `bytes`. Like, they parse the WAVE header and that is great and all, but you still have to decode your audio data yourself.

The same thing goes for playing/recording audio: [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) provides nifty bindings to [portaudio](http://www.portaudio.com/), but you still have to decode your raw `bytes` by hand.

But really, what I want is something different: When I record from the microphone, I want to get a NumPy array, not `bytes`. You know, something I can work with! And then I want to throw that array into a sound file, or play it on a different sound card, or do some calculations on it!

So one fateful day, I was sufficiently frustrated with the state of things that I set out to create just that. Really, I only wanted to play around with [cffi](http://cffi.readthedocs.org), but that is beside the point.

So, lets read some audio data, shall we?

```python
import soundfile
data = soundfile.read('sad_song.wav')
```

done. All the audio data is now available as a NumPy array in `data`. Just like that.

Awesome, isn't it?

OK, that was easy. So let's read only the first and last 100 frames!

```python
import soundfile
first = soundfile.read('long_song.flac', stop=100)
last = soundfile.read(start=-100)
```

This really only read the first and last bit. Not everything in between!

Note that at no point I did explicitly open or close a file! This is Python! We can do that! When the `SoundFile` object is created, it opens the file. When it goes out of scope, it closes the file. It's as simple as that. Or just use `SoundFile` in a context manager. That works as well.

Oh, but I want to use the sound card as well! I want to record audio to a file!

```python
from pysoundcard import Stream
from pysoundfile import SoundFile, ogg_file, write_mode
with Stream() as s: # opens your default audio device
    # This is supposed to be a new file, so specify it completely
    f = SoundFile('happy_song.ogg', sample_rate=s.sample_rate,
                  channels=s.channels, format=ogg_file,
                  mode=write_mode)
    f.write(s.read(s.sample_rate)) # one second
```

Read from the stream, write to a file. It works the other way round, too!

And that's really all there is to it. Working with audio data in Python is easy now!

Of course, there is much more you could do. You could create a callback function and be called every four[^1] frames with new audio data to process. You could request your audio data as `int16`, because that would be totally awesome! You could use many different sound cards at the same time, and route stuff to and fro to your hearts desire! And you can run all this on Linux using ALSA or Jack, or on Windows using DirectSound or ASIO, or on Mac using CoreAudio[^2]. And you already saw that you can read Wave files, OGG, FLAC or MAT-files[^3].

You can download these libraries from [PyPi](https://pypi.python.org/pypi), or use the binary Windows installers on Github. Or you can look at the source on Github ([PySoundFile](https://github.com/bastibe/PySoundFile), [PySoundCard](https://github.com/bastibe/PySoundCard)), because Open Source is awesome like that! Also, you might find some bugs, because I haven't found them all yet. Then, I would like you to open an issue on Github. Or if have a great idea of how to improve things, please let me know as well.

*UPDATE:* It used to be that you could use indexing on SoundFile objects. For various political reasons, this is no longer the case. I updated the examples above accordingly.

[^1]: You can use any block size you want. Less than 4 frames per block can be really taxing for your CPU though, so be careful or you start dropping frames.
[^2]: More precisely: Everything that [portaudio](http://www.portaudio.com/) supports.
[^3]: More precisely: Everything that [libsndfile](http://www.mega-nerd.com/libsndfile/) supports.
