from app.domain.interactor.audio_processing_interactor import AudioProcessingInteractor
from app.core.config import media_dir


def audio_processor() -> AudioProcessingInteractor:
    return AudioProcessingInteractor(media_dir=media_dir)


