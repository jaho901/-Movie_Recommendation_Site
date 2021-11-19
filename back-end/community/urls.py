from django.urls import path
from . import views

app_name="community"

urlpatterns = [
    path('', views.community_list),
    path('community_create/', views.community_create),
    path('<int:community_id>/', views.community_detail),
]
