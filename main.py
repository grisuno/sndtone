import sys
import pyaudio
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QFileDialog
import platform
import wave
import soundfile as sf

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

        self.layout.addWidget(self.frequency_label)
        self.layout.addWidget(self.frequency_input)

        duration_layout = QHBoxLayout()
        duration_layout.addWidget(self.duration_label)
        duration_layout.addWidget(self.duration_input)
        self.layout.addLayout(duration_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.save_button)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    generator = ToneGenerator()
    generator.show()
    sys.exit(app.exec())

