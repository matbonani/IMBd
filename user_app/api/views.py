from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegistrationSerializer


@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"message": "Logout"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            account = serializer.save()
            data['response'] = "Registration Sucessfuly !"
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token

            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #    'refresh': str(refresh),
            #    'access': str(refresh.access_token),
            # }

            return Response(data, status=status.HTTP_201_CREATED)

        return Response({"message": "Some problem with the server"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"message": "This method not allowed"}, status=status.HTTP_401_UNAUTHORIZED)
