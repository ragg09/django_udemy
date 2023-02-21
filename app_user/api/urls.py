# this will give us the token if we send the credentials
from rest_framework.authtoken.views import obtain_auth_token
from app_user.api.views import registration_view, logout_view

# # JWT Imports
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from django.urls import path

urlpatterns = [
    # TOKEN AUTHENTICATION
    # no views required since it is built-in in Django
    # just provide the obtain_auth_token and you can now use the url
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    
    # #JWT Authentication
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

