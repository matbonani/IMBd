from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Some problem with the server"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"message": "This method not allowed"}, status=status.HTTP_401_UNAUTHORIZED)
