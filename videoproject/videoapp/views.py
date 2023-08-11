from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .models import *
from .serializers import *

class UploadVideo(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        video_file = request.data['file']
        title = request.data.get('title', 'Untitled Video')

        video = Video(video_file=video_file, title=title)
        video.save()

        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateSubtitle(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubtitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetSubtitles(APIView):
    def get(self, request, video_id, *args, **kwargs):
        try:
            subtitles = Subtitle.objects.filter(video_id=video_id)
            serializer = SubtitleSerializer(subtitles, many=True)
            return Response(serializer.data)
        except Subtitle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)