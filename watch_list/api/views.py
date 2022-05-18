from rest_framework.response import Response
from rest_framework.decorators import api_view

from watch_list.models import Movie
from .serializers import MovieSerializer


@api_view(['GET'])
def movie_list(request):
    qs = Movie.objects.all()
    serializer = MovieSerializer(qs)
    print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, pk):
    qs = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(qs)
    print(serializer)
    return Response(serializer.data)
