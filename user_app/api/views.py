from user_app.api.serializer import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutAV(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class RegistrationCreateAV(APIView):
    def post(self, request):
        deserializer = RegistrationSerializer(data=request.data)
        data = {}
        if deserializer.is_valid():
            account = deserializer.save()
            #token = Token.objects.get(user=account).key
            refresh = RefreshToken.for_user(account)
            data = {
                'response' : 'El registro de usuario fue exitoso',
                'username' : account.username,
                'email' : account.email,
                #'token' : token
                'refresh':str(refresh),
                'access': str(refresh.access_token)
                }
        else:
            data = deserializer.errors
        
        return Response(data)