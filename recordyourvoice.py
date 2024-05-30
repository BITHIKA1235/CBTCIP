import pyaudio
import wave

def record_audio(output_file, duration=5, chunk=1024, format=pyaudio.paInt16, channels=1, rate=44100):
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    # Record audio
    for i in range(int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    # Stop stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Write audio to file
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Audio saved as:", output_file)

if __name__ == "__main__":
    output_file = "recorded_audio.wav"
    record_audio(output_file)
