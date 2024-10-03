import pyaudio
import wave

# настройки аудио
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024


def record_audio(filename: str, duration: int = 5) -> None:
    """
    Записывает аудиофайл с микрофона.

    :param filename: Имя выходного файла для сохранения записи
    :param duration: Продолжительность записи в секундах
    """
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []

    print("Начинаем запись...")
    for _ in range(0, int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Запись завершена.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))