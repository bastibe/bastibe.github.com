import matplotlib
from matplotlib import pyplot
import numpy
import soundfile
import signals
import scipy.signal

matplotlib.rcParams['font.size'] = 7

blocksize = 2048
hopsize = 256

fig, (ax1, ax2) = pyplot.subplots(nrows=2, sharex=True, figsize=[4, 2.5],
                                  gridspec_kw=dict(height_ratios=[4, 1]))

signal, samplerate = soundfile.read("Mann_short.wav")
spectrogram = signals.Spectrogram(signal, samplerate,
                                  blocksize=blocksize, hopsize=hopsize,
                                  window=scipy.signal.hann(blocksize))

# just to get the colorbar right:
im = ax1.imshow(
    numpy.abs(spectrogram).T,
    origin='lower', aspect='auto',
    extent=[blocksize/samplerate/2-hopsize/samplerate/2,
            len(spectrogram)*hopsize/samplerate+blocksize/samplerate/2,
            0, samplerate/2])

# the same, but in greyscale:
ax1.imshow(
    numpy.abs(spectrogram).T,
    origin='lower', aspect='auto',
    extent=[blocksize/samplerate/2-hopsize/samplerate/2,
            len(spectrogram)*hopsize/samplerate+blocksize/samplerate/2,
            0, samplerate/2],
    cmap='gray', vmin=-40)

# highlight selected specra in color:
times = numpy.arange(len(spectrogram))*hopsize/samplerate+blocksize/samplerate/2
for idx in range(len(spectrogram)):
    if times[idx] > 0.9 and times[idx] < 1.1 and idx % 4 == 3:
        ax1.imshow(
            numpy.abs(spectrogram[idx][:, None]),
            origin='lower', aspect='auto',
            extent=[times[idx]-hopsize/samplerate/2, times[idx]+hopsize/samplerate-hopsize/samplerate/2,
                    0, samplerate/2])

fig.colorbar(im, ax=ax1, label='magnitude in dB')
ax1.set(ylim=[0, 2000], ylabel='frequency in Hz')

ax2.plot(numpy.linspace(0, spectrogram.duration, len(signal)), signal)
ax2.set(xlabel='time in s', xlim=[0.9, 1.1], ylim=[-1.1, 1.1])
for idx, xoffset in enumerate(numpy.arange(0.9, 1.08, blocksize/samplerate/2)):
    yoffset = (idx % 4) / 3
    ax2.plot(numpy.arange(blocksize)/samplerate+xoffset, scipy.signal.hann(blocksize)-yoffset, color='black', alpha=0.5)

fig.tight_layout()
pos1 = ax1.get_position().bounds; pos2 = ax2.get_position().bounds
ax2.set_position([pos2[0], pos2[1], pos1[2], pos2[3]])

# do this after tight_layout, to keep axes from moving:
for idx, xoffset in enumerate(numpy.arange(0.9, 1.08, blocksize/samplerate/2)):
    yoffset = (idx % 4) / 3
    ax2.annotate('',
                 (xoffset+blocksize/samplerate/2, -yoffset+0.9),
                 (xoffset+blocksize/samplerate/2, 2.5),
                 arrowprops=dict(arrowstyle='<|-', alpha=0.7), annotation_clip=False)

fig.savefig(__file__[:-3] + '.png', dpi=300)
