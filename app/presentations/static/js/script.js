$(document).ready(function() {
    $('#audio-upload-form').on('submit', function(e) {
        // Предотвращаем стандартную отправку формы
        e.preventDefault();

        // Получаем файл из input
        var file = $('#audio-upload')[0].files[0];
        var formData = new FormData();
        formData.append('audio_file', file);

        $.ajax({
            url: 'http://127.0.0.1:8000/upload/', // URL для эндпоинта загрузки файлов в FastAPI
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#transcription-text').val(response.text);
            },
            error: function(error) {
                console.error('Ошибка при загрузке файла:', error);
            }
        });
    });
});