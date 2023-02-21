from rest_framework.decorators import api_view
from app_user.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from app_user import models

from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        
        data = {}
        
        if(serializer.is_valid()):
            account = serializer.save()
            
            # Token Authentication
            #getting token
            token = Token.objects.get(user = account).key
            
            # # JWT Authentication
            # #generate token on registration
            # refresh = RefreshToken.for_user(account)
            # token = {
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token),
            # }
            
            data['message'] = "Registration successful"
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = token
        else:
            data = serializer.errors
        
        return Response(data)
    
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        # just simply delete token 
        request.user.auth_token.delete()
        return Response(status = status.HTTP_200_OK)