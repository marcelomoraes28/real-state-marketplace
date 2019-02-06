from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        lookup_field = 'uuid'
