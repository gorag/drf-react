from rest_framework import viewsets

from persons_information.models import Person, Document
from persons_information.serializers import PersonSerializer, DocumentSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
