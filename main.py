import sys
import math
import numpy as np
import pygame
import time
import pyaudio
import wave
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.fft import fft
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QColor
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

# Manejador de eventos para el desplazamiento de la rueda del mouse
def wheelEvent(event):
    global freq, angle_per_sample
    delta = event.angleDelta().y()
    freq += delta / 8  # Dividimos por 8 para disminuir la sensibilidad del dial
    freq = max(dial.minimum(), min(dial.maximum(), freq))
    dial.setValue(freq)
    angle_per_sample = 2.0 * math.pi * freq / sample_rate

class ToneGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Tonos")
        self.layout = QVBoxLayout()

        self.frequency_label = QLabel("Frecuencia (Hz):")
        self.frequency_input = QLineEdit()

        self.duration_label = QLabel("Duración (segundos):")
        self.duration_input = QLineEdit()

        self.play_button = QPushButton("Tocar")
        self.play_button.clicked.connect(self.play_tone)

        self.save_button = QPushButton("Guardar")
        self.save_button.clicked.connect(self.save_tone)

        self.generate_button = QPushButton("Generar")
        self.generate_button.clicked.connect(self.generate_waveform)

        self.layout.addWidget(self.frequency_label)
        self.layout.addWidget(self.frequency_input)

        duration_layout = QHBoxLayout()
        duration_layout.addWidget(self.duration_label)
        duration_layout.addWidget(self.duration_input)
        self.layout.addLayout(duration_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.generate_button)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

    def play_tone(self):
        frequency = float(self.frequency_input.text())
        duration = float(self.duration_input.text())

        p = pyaudio.PyAudio()

        output_device = None
        info = p.get_host_api_info_by_index(0)
        num_devices = info.get('deviceCount')
        for i in range(num_devices):
            device_info = p.get_device_info_by_host_api_device_index(0, i)
            if device_info.get('maxOutputChannels') > 0:
                output_device = device_info.get('name')
                break

        if output_device is None:
            print("No se encontró un dispositivo de salida de audio válido.")
            return

        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=44100,
                        output=True,
                        output_device_index=None)  # Reemplaza None con el índice del dispositivo si es necesario

        samples = []
        for i in range(int(duration * 44100)):
            samples.append(0.3 * np.sin(2 * np.pi * frequency * i / 44100))

        samples = np.array(samples, dtype=np.float32)

        stream.write(samples.tobytes())
        stream.stop_stream()
        stream.close()
        p.terminate()

    def save_tone(self):
        frequency = float(self.frequency_input.text())
        duration = float(self.duration_input.text())

        sample_rate = 44100
        num_samples = int(sample_rate * duration)
        time = np.arange(num_samples) / sample_rate
        tones = 0.3 * np.sin(2 * np.pi * frequency * time)

        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar tono", "", "Archivos de audio (*.wav *.ogg)")
        if file_path:
            try:
                file_extension = file_path.split(".")[-1]
                if file_extension == "wav":
                    with wave.open(file_path, 'wb') as wav_file:
                        wav_file.setnchannels(1)
                        wav_file.setsampwidth(2)
                        wav_file.setframerate(sample_rate)
                        wav_file.writeframes(tones.astype(np.int16))
                elif file_extension == "ogg":
                    sf.write(file_path, tones, sample_rate)
                else:
                    raise ValueError(f"Formato de archivo no compatible: {file_extension}")

                QMessageBox.information(self, "Éxito", "El tono se ha guardado correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el tono.\nError: {str(e)}")

    def generate_waveform(self):
        frequency = float(self.frequency_input.text())
        duration = float(self.duration_input.text())

        sample_rate = 44100
        num_samples = int(sample_rate * duration)
        time = np.arange(num_samples) / sample_rate
        waveform = 0.3 * np.sin(2 * np.pi * frequency * time)

        # Gráfico de forma de onda
        plt.subplot(2, 2, 1)
        plt.plot(time, waveform)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Amplitud')
        plt.title('Forma de onda')

        # Transformada de Fourier de la forma de onda
        fft_spectrum = fft(waveform)
        frequencies = np.linspace(0, sample_rate / 2, num_samples // 2)
        amplitudes = np.abs(fft_spectrum[:num_samples // 2])

        plt.subplot(2, 2, 2)
        plt.plot(frequencies, amplitudes)
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Amplitud')
        plt.title('Espectro de frecuencia')

        # Histograma de la forma de onda
        plt.subplot(2, 2, 3)
        plt.hist(waveform, bins=50, color='skyblue', edgecolor='black')
        plt.xlabel('Amplitud')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de amplitud')

        # Visualización de la señal de audio
        plt.subplot(2, 2, 4)
        plt.specgram(waveform, Fs=sample_rate, cmap='viridis')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Frecuencia (Hz)')
        plt.title('Espectrograma')

        # Ajustar el diseño de la figura
        plt.tight_layout()

        # Mostrar la figura con todas las visualizaciones
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    generator = ToneGenerator()
    generator.show()
    sys.exit(app.exec())

