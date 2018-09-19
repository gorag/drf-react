from rest_framework import serializers

from persons_information.models import Person


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
        )
