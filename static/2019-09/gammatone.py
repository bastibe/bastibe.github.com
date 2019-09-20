import matplotlib
from matplotlib import pyplot
import numpy
import soundfile
from pyfilterbank import gammatone

matplotlib.rcParams['font.size'] = 7

blocksize = 512
hopsize = 64

fig, (ax1, ax2) = pyplot.subplots(nrows=2, sharex=True, figsize=[4, 2.5],
                                  gridspec_kw=dict(height_ratios=[4, 1]))

signal, samplerate = soundfile.read("Mann_short.wav")
fbank = gammatone.GammatoneFilterbank(
    samplerate, startband=-15, endband=27, order=4, density=1/2)
bands, states = zip(*fbank.analyze(signal))
bands = list(fbank.delay(bands))

im = ax1.pcolormesh(
    numpy.arange(len(signal))/samplerate,
    fbank.centerfrequencies,
    bands, cmap='twilight')

fig.colorbar(im, ax=ax1, label='amplitude')
ax1.set(ylim=[0, 2000], ylabel='center frequency in Hz')

ax2.plot(numpy.linspace(0, len(signal)/samplerate, len(signal)), signal)
ax2.set(xlabel='time in s', xlim=[0.95, 1.05], ylim=[-1.1, 1.1])

fig.tight_layout()
pos1 = ax1.get_position().bounds; pos2 = ax2.get_position().bounds
ax2.set_position([pos2[0], pos2[1], pos1[2], pos2[3]])

fig.savefig(__file__[:-3] + '.png', dpi=300)
