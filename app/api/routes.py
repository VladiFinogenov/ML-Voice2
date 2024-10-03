import logging
from typing import Annotated

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from app.domain.entities.forms import AudioFile
from app.factory import audio_processor
from app.domain.interactor.audio_processing_interactor import AudioProcessingInteractor


logger = logging.getLogger('my_logger')


router = APIRouter(tags=['audio'])


@router.post("/upload/")
async def upload_audio(
        audio_file: UploadFile = File(...),
        interactor: AudioProcessingInteractor = Depends(audio_processor)):

    logger.info('Вызов эндпоинта upload_audio')

    try:
        # Убедитесь, что оба метода save_file и process_audio могут работать асинхронно
        file_location = await interactor.save_file(audio_file)
        processed_file_location = await interactor.process_audio()

        return JSONResponse(content={"original_file": file_location, "processed_file": 'файл получил'})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))