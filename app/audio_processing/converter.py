import speech_recognition as sr


def convert_audio_to_text(audio_file: str) -> str:
    """
    Преобразует аудиофайл в текст.

    :param audio_file: Путь к аудиофайлу
    :return: Преобразованный текст
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        # text = recognizer.recognize_google(audio_data, language='ru-RU')
        text = recognizer.recognize_google_cloud(audio_data, language='ru-RU')
        return text
    except sr.UnknownValueError:
        return "Не удалось распознать речь."
    except sr.RequestError:
        return "Ошибка при обращении к сервису распознавания."