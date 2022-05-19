from django.urls import path, include

# from watch_list.api.views import movie_list, movie_detail
from watch_list.api.views import WatchListView, WatchDetailView, StreamPlatformView,\
    StreamPlatformDetailView, ReviewListView, ReviewDetailView

urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_detail, name='movie-detail'),
    path('', WatchListView.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailView.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformView.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailView.as_view(), name='streamplatform-detail'),
    path('review/', ReviewListView.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),

]