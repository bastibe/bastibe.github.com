---
title: My Projects
date: 2018-06-13
filetags: nocomments
---

## [X-Plane Mission Generator](https://missiongenerator.eu/)
A plugin for the [X-Plane](https://www.x-plane.com/) flight simulator, using the awesome [SASL](https://1-sim.com/) Lua adapter for writing X-Plane plugins. Randomly generates mission briefings, follows your flight, gives detailed debriefings, and lets you level up with experience points. My first commercial project, being sold on the [X-Plane.org store](https://store.x-plane.org_Mission-Generator_p_877.html). (Status: released)
## [SoundFile](https://github.com/bastibe_SoundFile)
Read and write audio files from Python as Numpy arrays, using the fantastic C library [libsndfile](http://www.mega-nerd.com/libsndfile/) and [CFFI](https://cffi.readthedocs.org/). Developed in collaboration with [@mgeier](https://github.com/mgeier). Install using `pip install soundfile`. Documentation at [pysoundfile.readthedocs.io](http://pysoundfile.readthedocs.io/). (Status: mature)
## [SoundCard](https://github.com/bastibe_SoundCard)
Play and record audio from Python as Numpy arrays, using the native audio libraries of [Linux](https://freedesktop.org/software/pulseaudio/doxygen/index.html), [Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371455(v=vs.85).aspx), and [macOS](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/Introduction/Introduction.html). My third attempt at cross-platform audio in Python. This grew out of my frustration with existing cross-platform audio libraries, because I wanted correct default sound cards and channel maps and convenient sound card selection. Watch me talk about this on [EuroScipy 2017 (Youtube)](https://www.youtube.com_watch?v=mc8ru37dwf8). Install using `pip install soundcard`. (Status: alpha, but getting there)
## [Transplant](https://github.com/bastibe_transplant)
Call Matlab code from Python, without fighting it. Uses [ZeroMQ](http://zeromq.org/) sockets and includes a complete [MessagePack](https://msgpack.org/) and JSON parser in Matlab, because Matlab does not support any of these natively. And since Matlab is started safely in a subprocess, you can even crash Matlab without sacrificing your Python. Install using `pip install transplant`. (Status: mature)
## [org-journal](https://github.com/bastibe_org-journal)
Keep a journal as one org file per day. And if you want, carry TODO items with you until they are DONE, search your journal quickly even if it has thousands of files, and add future journal entries to remember appointments. Integrates with the [agenda](https://orgmode.org/manual/Agenda-views.html) and the [calendar](https://www.gnu.org/software/emacs/manual/html_node/emacs_Calendar_002fDiary.html). Install using `(package-install 'org-journal)`. (Status: mature and ever expanding)
## [org-static-blog](https://github.com/bastibe_org-static-blog)
The engine this blog is built upon. A very simple collection of org files get transformed into static HTML and CSS, without any external dependencies beyond Emacs itself. (Status: works for me)
## [RunForrest](https://github.com/bastibe_RunForrest)
Run many tasks in parallel, even if they crash, kernel panic, and wreak havoc. If you run enough scientific code, your processes _will/ crash, leak memory, exhaust file descriptors, and destroy your file system. To stay sane anyway, runforrest runs every task in its own process, and saves everything to disk the moment it is done. /Very_ simple, because simplicity is your only defense against the inhuman terror that is scientific code. (Status: easy to debug)
## [JBOF - Just a Bunch Of Files](https://github.com/bastibe_jbof)
Store collections of binary data as collections of files, with JSON metadata. Something like HDF, but thread safe and easy to browse and debug. (Status: beta)
## [TimeUp](https://github.com/bastibe_timeup)
Back up your data with rsync, and keep different numbers of hourly, daily, weekly, and monthly copies. (Status: use at your own risk. Works, though)
## [pomodoro-timer.org](http://pomodoro-timer.org)
A simple [pomodoro timer](https://en.wikipedia.org/wiki_Pomodoro_Technique), with a pretty canvas animation of a rotating tomato, and local storage for keeping track of your past pomos. (Status: mature)
## [Qt for Python Video Tutorial](http://bastibe.de_2020-03-20-qt-for-python-tutorial.html)
A video series explaining the use of [Qt for Python](https://www.qt.io_qt-for-python) by building a small GUI application. In German, because that's the language I teach in. (Status: released)

## PhD Dissertation
### [Pitch of Voiced Speech in the Short-Time Fourier Transform: Algorithms, Ground Truths, and Evaluation Methods](https://bastibe.github.io/Dissertation-Website/)
or _Speech has a Pitch, but what is Pitch Anyway?_

My dissertation started from the design of a pitch estimation algorithm, originally destined for quite a different task. Surprisingly, I found the true scientific challenge not the algorithm itself but how to evaluate its accuracy: Traditionally, pitch estimation algorithms are evaluated against a _ground truth_ that is just assumed to be accurate. Pitch is a human perception, not a measurable, physical quantity. As it turns out, these ground truths are based on pitch estimation algorithms themselves, and often ones derived from laryngograph measurements instead of acoustic recordings, which are not ideal for the task. Furthermore, the error measures used for evaluating pitch estimation algorithms are woefully inadequate.

So I set out to design a better ground truth, which does not rely on a single pitch estimation algorithm, but a large number of them, and is based on acoustic recordings. This does not solve the categorical mismatch between an algorithm's estimate and a human perception, but at least it sidesteps the biases of any one algorithm and laryngographs.

With that, I conducted a huge comparison study between a very large number of pitch estimation algorithms and speech databases, and introduced a number of new evaluation methods. This study was unprecedented in the area of research, and produced a number of interesting results. Chiefly among them, that the differences between speech and noise databases used for evaluation far outweigh any minute differences between algorithms. In other words, a strong case of overfitting across the entire area of research.

In the end, the work was more about data science than signal processing. Regrettably, I was [not able to publish](https://bastibe.de_2019-07-09-publish-or-perish.html) my results in journals.

## Finished or Abandoned Projects
### [PySoundCard](https://github.com/bastibe_PySoundCard)
My second attempt at getting cross-platform audio to work in Python. Uses [CFFI](https://cffi.readthedocs.org/) and [portaudio](http://www.portaudio.com/), much like [SoundFile](https://github.com/bastibe/SoundFile). But it just didn't work out between portaudio and me. Use [SoundCard](https://github.com/bastibe/SoundCard) for a better solution, or [SoundDevice](https://github.com/spatialaudio_python-sounddevice) for a maintained portaudio bridge. (Status: starting to smell)
### [Map-Matlab](https://github.com/bastibe_Map-Matlab)
Show an asynchronously-loading, interactive map in a Matlab figure. This is an example for my lecture on programming Matlab. (Status: educational)
### [WebGL-Spectrogram](https://github.com/bastibe_WebGL-Spectrogram)
Draw a smooth, interactive, zooming spectrogram using WebGL and a Python web server. Built as a technology demonstration for WebGL. (Status: probably doesn't even start any more)
### [MatlabCodeAnalyzer](https://github.com/bastibe_MatlabCodeAnalyzer)
Parse and criticize Matlab code. This was meant as a tool for students to help them improve their code quality, but turned out to be too nit-picky to be useful. (Status: works)
### [MatType](https://github.com/bastibe_MatType)
A typing tutor in pure Matlab. See how fast you can type in Matlab. Writing a text editing widget from scratch was fun. (Status: fun hack)
### [Violinplot-Matlab](https://github.com/bastibe_Violinplot-Matlab)
Plot violin plots in Matlab. Because everyone is using box plots and thus don't realize that their data is non-gaussian and too sparse. Violin plots show the same thing, but more beautifully and less wrong. (Status: useful)
### [annotate.el](https://github.com/bastibe_annotate.el)
Annotate arbitrary files as a minor mode in Emacs. Didn't turn out to be quite as useful as I'd hoped, but I learned a lot about Emacs. Install using `(package-install 'annotate)`. (Status: works)
### [MatlabXML](https://github.com/bastibe_MatlabXML)
It was literally faster to write my own XML parser for Matlab than to wait for Matlab's own parser to parse my 150 Mb XML file. No support for text nodes, cdata nodes, or any kind of schema validation. (Status: useful)
### [Matlab-MsgPack](https://github.com/bastibe_matlab-msgpack)
JSON parsing turned out to be the largest performance bottleneck in [Transplant](https://github.com/bastibe/transplant), so I use MsgPack instead. But Matlab lacked a MsgPack parser_dumper, so here is one. (Status: tested and complete)

## Contributions
### [Lunatic-Python](https://github.com/bastibe_lunatic-python)
Call Python from Lua, or Lua from Python. I ported this to Python 3, back in the day. But the original developer was nowhere to be found, so it ended up on my Github. Nowadays it is maintained by a dedicated group of wonderful volunteers. (Status: alive and kicking)
### [Matplotlib](https://github.com/matplotlib/matplotlib/pull_6254)
I often work with cyclic phase data, which wraps around such that its highest value is also its lowest value. Matplotlib didn't have a convenient color map for this kind of data, so I created one. And now this color map is part of Matplotlib. (Status: awesome!)
### [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
My first attempt at getting cross-platform audio to work in Python. Back then, PyAudio was the best choice, but it didn't support Python 3 yet. So I helped out, and ported it to Python 3. (Status: still maintained)

## Student Projects
### [audioanalyzer.net](http://audioanalyzer.net/)
Analyze audio files with waveform, spectrogram and phase-spectrogram in the browser. Developed as part of a one-semester student project I supervised.
### [Earyx](https://github.com/TGM-Oldenburg_earyx)
Run psychoacoustic experiments in the browser. A port of [Psylab](https://github.com/TGM-Oldenburg/Psylab) for Python, by [@stvol](https://github.com/stvol), [@zngguvnf](https://github.com_zngguvnf), and Nils. Developed as part of a one-semester student project I supervised.
### [MSound](https://github.com/TGM-Oldenburg_Msound)
A cross-platform audio mex file for Matlab, based on portaudio. I worked on this back when I was a student. (Status: still alive)
