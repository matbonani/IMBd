from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watch_list.api.views import movie_list, movie_detail
from watch_list.api.views import WatchListView, WatchDetailView,\
    ReviewListView, ReviewDetailView, ReviewCreateView, StreamPlatformViewSet

router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    # path('list/', movie_list, name='movie-list'),                  function view
    # path('<int:pk>', movie_detail, name='movie-detail'),
    path('', WatchListView.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailView.as_view(), name='movie-detail'),

    # path('stream/', StreamPlatformView.as_view(), name='stream'),     APIView
    # path('stream/<int:pk>', StreamPlatformDetailView.as_view(), name='streamplatform-detail'),
    path('', include(router.urls)),


    # path('review/', ReviewListView.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
    path('<int:pk>/review-create/', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewListView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]