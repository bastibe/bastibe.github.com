import matplotlib
from matplotlib import pyplot
import numpy
import soundfile
import signals
import scipy.signal
from librosa.core import cqt, cqt_frequencies

matplotlib.rcParams['font.size'] = 7

blocksize = 512
hopsize = 64

fig, (ax1, ax2) = pyplot.subplots(nrows=2, sharex=True, figsize=[4, 2.5],
                                  gridspec_kw=dict(height_ratios=[4, 1]))

signal, samplerate = soundfile.read("Mann_short.wav")
cq_spectrogram = cqt(signal, samplerate, hopsize, filter_scale=0.25)

im = ax1.pcolormesh(
    numpy.linspace(0, hopsize*cq_spectrogram.shape[1]/samplerate, cq_spectrogram.shape[1]),
    cqt_frequencies(cq_spectrogram.shape[0], 32.7),
    20*numpy.log10(numpy.abs(cq_spectrogram)), vmin=-20)

fig.colorbar(im, ax=ax1, label='magnitude in dB')
ax1.set(ylim=[0, 2000], ylabel='frequency in Hz')

ax2.plot(numpy.linspace(0, len(signal)/samplerate, len(signal)), signal)
ax2.set(xlabel='time in s', xlim=[0.95, 1.05], ylim=[-1.1, 1.1])

fig.tight_layout()
pos1 = ax1.get_position().bounds; pos2 = ax2.get_position().bounds
ax2.set_position([pos2[0], pos2[1], pos1[2], pos2[3]])

fig.savefig(__file__[:-3] + '.png', dpi=300)
