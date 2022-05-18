from django.urls import path, include

# from watch_list.api.views import movie_list, movie_detail
from watch_list.api.views import MovieList, MovieDetail

urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_detail, name='movie-detail'),
    path('list/', MovieList.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie-detail'),

]