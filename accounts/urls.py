from django.contrib import admin
from django.urls import include, path
from .views import SecretMessageDetail, UserDetail, SecretMessagesList

urlpatterns = [
    path('auth/', include('rest_auth.urls')),    
    path('auth/register/', include('rest_auth.registration.urls')),
    path('auth/user/', UserDetail.as_view()),
    path('auth/user/secrets/', SecretMessagesList.as_view()),
    path('auth/user/secrets/<uuid:secret_id>/', SecretMessageDetail.as_view()),
    # path('user/<int:pk>/', UserDetail.as_view()),
    # path('user/<int:userpk>/secrets/', SecretMessagesList.as_view()),
    # path('user/<int:userpk>/secrets/<int:pk>/', SecretMessageDetail.as_view())
]
