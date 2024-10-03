$(document).ready(function() {
    $('#audio-upload').on('change', function(e) {
        var file = e.target.files[0];
        var formData = new FormData();
        formData.append('audio_file', file);

        $.ajax({
            url: '/upload/', // URL для эндпоинта загрузки файлов в FastAPI
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