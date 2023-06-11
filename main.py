import sys
import pyaudio
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class ToneGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Tonos")
        self.layout = QVBoxLayout()

        self.frequency_label = QLabel("Frecuencia (Hz):")
        self.frequency_input = QLineEdit()
        self.play_button = QPushButton("Tocar")
        self.play_button.clicked.connect(self.play_tone)

        self.layout.addWidget(self.frequency_label)
        self.layout.addWidget(self.frequency_input)
        self.layout.addWidget(self.play_button)

        self.setLayout(self.layout)

    def play_tone(self):
        frequency = float(self.frequency_input.text())
        duration = 1.0  # Duración del tono en segundos

        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=44100,
                        output=True)

        samples = []
        for i in range(int(duration * 44100)):
            samples.append(0.3 * np.sin(2 * np.pi * frequency * i / 44100))

        samples = np.array(samples, dtype=np.float32)

        stream.write(samples.tobytes())
        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    generator = ToneGenerator()
    generator.show()
    sys.exit(app.exec_())
