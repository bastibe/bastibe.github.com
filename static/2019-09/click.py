from matplotlib import pyplot
import numpy
import signals
import scipy.signal
import matplotlib

matplotlib.rcParams['font.size'] = 7

fig, (ax1, ax2) = pyplot.subplots(ncols=2, sharex=True, figsize=[4, 2])

samplerate = 48000
blocksize = 2048
hopsize = 128

signal = numpy.zeros(samplerate) + 1e-10
signal[int(samplerate * 0.22)] = 1

time = numpy.arange(samplerate)/samplerate
ax1.plot(time, signal)
ax1.set(xlim=[0.2, 0.4])
ax1.set(ylabel='Amplitude', xlabel='Time in s', title='Waveform')

spectrum = 20*numpy.log10(numpy.abs(signals.Spectrogram(
    signal, samplerate, blocksize, hopsize, scipy.signal.hann, 4*blocksize)))

im = ax2.pcolormesh(
    numpy.arange(len(spectrum))*hopsize/samplerate + blocksize/2/samplerate,
    numpy.linspace(0, samplerate/2, len(spectrum[0])),
    spectrum.T, vmin=-20)

ax2.set(ylim=[0, 2000], xlim=[0.2, 0.4])
ax2.set(ylabel='Frequency in Hz', xlabel='Time in s', title='Spectrum')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

ax1.annotate("→", (0.48, 0.5), xycoords='figure fraction',
             horizontalalignment='center', fontsize='xx-large')

fig.tight_layout()

fig.savefig(__file__[:-3] + '.png', dpi=300)
