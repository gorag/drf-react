from rest_framework import viewsets

from persons_information.models import Person
from persons_information.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
