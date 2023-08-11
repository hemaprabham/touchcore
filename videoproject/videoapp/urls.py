from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.UploadVideo.as_view(), name='upload-video'),
    path('subtitles/', views.CreateSubtitle.as_view(), name='create-subtitle'),
    path('subtitles/<int:video_id>/', views.GetSubtitles.as_view(), name='get-subtitles'),
]
