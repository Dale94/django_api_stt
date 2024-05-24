# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import speech_recognition as sr
import os
import ffmpeg

class SpeechToTextView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']

        # Ensure the 'uploads' directory exists
        upload_dir = 'uploads'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        raw_audio_path = os.path.join(upload_dir, 'raw_audio.wav')
        converted_audio_path = os.path.join(upload_dir, 'converted_audio.wav')

        with open(raw_audio_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        # Remove the existing converted audio file if it exists
        if os.path.exists(converted_audio_path):
            os.remove(converted_audio_path)

        # Convert the audio file to WAV format using ffmpeg
        try:
            ffmpeg.input(raw_audio_path).output(converted_audio_path).run()
        except ffmpeg.Error as e:
            return Response({"error": "Audio conversion failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        recognizer = sr.Recognizer()
        with sr.AudioFile(converted_audio_path) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio)
                return Response({"text": text}, status=status.HTTP_200_OK)
            except sr.UnknownValueError:
                return Response({"error": "Could not understand audio"}, status=status.HTTP_400_BAD_REQUEST)
            except sr.RequestError as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            finally:
                os.remove(raw_audio_path)
