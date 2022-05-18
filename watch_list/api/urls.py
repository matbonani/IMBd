from django.urls import path, include

# from watch_list.api.views import movie_list, movie_detail
from watch_list.api.views import WatchListView, WatchDetailView, StreamPlatformView, StreamPlatformDetailView

urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_detail, name='movie-detail'),
    path('', WatchListView.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailView.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformView.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailView.as_view(), name='stream-detail'),

]