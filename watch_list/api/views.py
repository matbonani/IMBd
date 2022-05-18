from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from watch_list.models import Movie
from .serializers import MovieSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        qs = Movie.objects.all()
        serializer = MovieSerializer(qs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        qs = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(qs)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = MovieSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
