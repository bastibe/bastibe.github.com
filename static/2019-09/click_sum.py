from matplotlib import pyplot
import numpy
import matplotlib

matplotlib.rcParams['font.size'] = 7

fig, (ax1, ax2) = pyplot.subplots(ncols=2, sharex=True, figsize=[4, 2])

samplerate = 48000
blocksize = 2048
hopsize = 128

signal = numpy.zeros(samplerate) + 1e-10
signal[int(samplerate * 0.2)] = 1

time = numpy.arange(samplerate)/samplerate
ax1.plot(time, signal)
ax1.set(xlim=[0.19, 0.21])
ax1.set(ylabel='Amplitude', xlabel='Time in s', title='Waveform')

for idx, f in enumerate(numpy.arange(100, 550, 50)):
    ax2.plot(time, 0.03*numpy.cos(time*numpy.pi*2*f + numpy.pi*2*f*0.2)+idx/20, color='black', alpha=0.5)

ax2.set(xlim=[0.19, 0.21])
ax2.set(ylabel='Frequencies', xlabel='Time in s', title='Fourier Series')
ax2.set(yticks=numpy.arange(0, 0.45, 0.1), yticklabels=numpy.arange(100, 550, 100))
ax2.set_yticks(numpy.arange(0, 0.45, 0.05), minor=True)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

ax1.annotate("→", (0.5, 0.5), xycoords='figure fraction',
             horizontalalignment='center', fontsize='xx-large')

fig.tight_layout()

fig.savefig(__file__[:-3] + '.png', dpi=300)
