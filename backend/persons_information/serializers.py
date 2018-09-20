from rest_framework import serializers

from persons_information.models import Person, Document


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = (
            'url',
            'id',
            'full_name',
            'date_of_birth',
            'gender',
            'start_date',
            'end_date',
            'training_group',
            'educational_institution',
            'documents',
        )


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = (
            'url',
            'id',
            'number',
            'date_of_issue',
            'type',
            'scan_document',
            'person',
        )
