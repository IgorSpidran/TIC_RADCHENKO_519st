import numpy as np
from scipy import signal, fft
import matplotlib.pyplot as plt
import os

def generate_random_signal(length, mean, std_dev):
    return np.random.normal(mean, std_dev, length)

def plot_signal(time, signal, xlabel, ylabel, title, save_path=None):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(time, signal, linewidth=1)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=16)
    if save_path:
        fig.savefig(save_path, dpi=600)
    plt.show()

def plot_spectrum(freqs, spectrum, xlabel, ylabel, title, save_path=None):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(freqs, spectrum, linewidth=1)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=16)
    if save_path:
        fig.savefig(save_path, dpi=600)
    plt.show()

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


n = 500
Fs = 1000
F_max = 27


random_signal = generate_random_signal(n, 0, 10)


time = np.arange(n) / Fs


w = F_max / (Fs / 2)
sos = signal.butter(3, w, 'low', output='sos')


filtered_signal = signal.sosfiltfilt(sos, random_signal)


save_directory = './figures/'
ensure_directory_exists(save_directory)


plot_signal(time, filtered_signal, 'Время (секунды)', 'Амплитуда сигнала',
            'Сигнал с максимальной частотой F_max=27Гц', os.path.join(save_directory, 'signal.png'))


spectrum = fft.fft(filtered_signal)
spectrum = np.abs(fft.fftshift(spectrum))
freqs = fft.fftfreq(n, 1/Fs)
freqs = fft.fftshift(freqs)


plot_spectrum(freqs, spectrum, 'Частота (Гц)', 'Амплитуда спектра',
              'Спектр сигнала с максимальной частотой F_max=27Гц', os.path.join(save_directory, 'spectrum.png'))
