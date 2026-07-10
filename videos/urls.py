from django.urls import path
from . import views as views
urlpatterns = [
    path('create/', views.CreateVideo.as_view(), name='video-create'),
    path('get-recommendations/<str:category>', views.get_recommended_videos),
    path('upload-video-chunk/', views.upload_chunk, name='upload-chunk'),
    path('<slug:id>/', views.redirect_video),
    path('<slug:id>', views.DetailVideo.as_view(), name='video-detail'),
    path('<slug:id>/update', views.UpdateVideo.as_view(), name='video-update'),
    path('<slug:id>/delete', views.DeleteVideo.as_view(), name='video-delete'),
    path('<slug:id>/like', views.AddLike.as_view(), name='video-like'),
    path('<slug:id>/dislike', views.Dislike.as_view(), name='video-dislike'),
    path('<slug:id>/download', views.DownloadVideo.as_view(), name='video-download'),
    path('<slug:id>/recommend', views.Recommend.as_view(), name='video-recommend'),
    path('<slug:id>/nominate', views.Nominate.as_view(), name='video-nominate'),
    path('<slug:id>/update-view-count/', views.update_video_view_count),
]
