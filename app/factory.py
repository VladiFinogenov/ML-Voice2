from domain.interactor.audio_processing_interactor import AudioProcessingInteractor
from app.main import media_dir


def audio_processor() -> AudioProcessingInteractor:
    return AudioProcessingInteractor(media_dir=media_dir)


