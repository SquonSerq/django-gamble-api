from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from players import views

urlpatterns = [
    path('players/<int:bot_id>', views.PlayerDetailViewSet.as_view()),
    path('admin/', admin.site.urls),
]
