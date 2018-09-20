from django.urls import path, include
from rest_framework.routers import DefaultRouter

from persons_information import views

router = DefaultRouter()
router.register('persons', views.PersonViewSet)
router.register('documents', views.DocumentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
