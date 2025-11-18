import sounddevice as sd
from scipy.io.wavfile import write

class AudioTool:
    def record_audio(self, filename, duration=5, sample_rate=44100):
        print("[Audio] Recording audio...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
        sd.wait()
        write(filename, sample_rate, audio_data)
        print("[Audio] Recording finished.")
