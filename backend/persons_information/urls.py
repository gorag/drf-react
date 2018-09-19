# from django.conf.urls import url, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from persons_information import views

router = DefaultRouter()
router.register('persons', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('persons/', views.PersonList.as_view(), name='person-list'),
#     path('persons/<int:pk>/', views.PersonDetail.as_view(), name='person-detail'),
# ]
