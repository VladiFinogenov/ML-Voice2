import os
from fastapi import UploadFile


class AudioProcessingInteractor:

    def __init__(self, media_dir: str):
        self.media_dir = media_dir

    def save_file(self, file: UploadFile):
        # Сохраняем файл в директории media
        file_location = os.path.join(self.media_dir, file.filename)
        with open(file_location, "wb") as f:
            f.write(file.file.read())

        return file_location

    def process_audio(self):
        pass