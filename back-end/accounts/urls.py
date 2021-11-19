from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('api-token-auth/', obtain_jwt_token),
    path('<user_pk>/', views.profile, name='profile'),
    # path('delete/', views.user_delete),
    # path('')
]
