import math
import numpy


class SignalBlocks:
    def __init__(self, signal, samplerate, blocksize=2048, hopsize=1024):
        self.signal = signal
        self.samplerate = int(samplerate)
        self.blocksize = int(blocksize)
        self.hopsize = int(hopsize)
        self.numblocks = math.ceil( (len(signal)-blocksize) / hopsize )

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[n] for n in range(*index.indices(self.numblocks))]
        if index >= self.numblocks:
            raise IndexError("block index out of range")
        start = index * self.hopsize
        stop = start + self.blocksize
        return self.signal[start:stop]

    def __len__(self):
        return self.numblocks

    @property
    def duration(self):
        return len(self.signal)/self.samplerate


class Spectrogram(SignalBlocks):
    def __init__(self, signal, samplerate, blocksize, hopsize, window, nfft=None):
        super().__init__(signal, samplerate, blocksize, hopsize)
        if callable(window):
            self.window = window(blocksize)
        else:
            self.window = window
        if nfft is None:
            self.nfft = blocksize
        else:
            self.nfft = nfft

    def __getitem__(self, index):
        block = super().__getitem__(index)
        return numpy.fft.rfft(block*self.window, self.nfft)
