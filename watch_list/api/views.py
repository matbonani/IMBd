from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from watch_list.models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer


class WatchListView(APIView):

    def get(self, request):
        qs = WatchList.objects.all()
        serializer = WatchListSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailView(APIView):

    def get(self, request, pk):
        try:
            qs = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(qs)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            qs = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            qs = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformView(APIView):

    def get(self, request):
        qs = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class StreamPlatformDetailView(APIView):

    def get(self, request, pk):
        try:
            qs = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Stream Platform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(qs, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            qs = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Stream Platform not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            qs = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Stream Platform not found"}, status=status.HTTP_404_NOT_FOUND)

        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





"""
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
"""