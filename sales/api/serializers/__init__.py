from django.db import transaction
from rest_framework import serializers

from sales.helpers.dict_ import count_dict


class BaseSerializer(serializers.ModelSerializer):

    @transaction.atomic
    def update(self, instance, validated_data):
        return self._update(instance, validated_data)

    def _update(self, instance, validated_data):
        for k, attr in dict(validated_data).items():
            if isinstance(attr, dict):
                if count_dict(attr) != 1:
                    self._update(getattr(instance, k), attr)
                else:
                    for kx, attrx in attr.items():
                        setattr(getattr(instance, k), kx, attrx)
                        getattr(instance, k).save()
            elif isinstance(attr, list):
                for at in attr:
                    getattr(instance, k).update_or_create(**at)
            else:
                setattr(instance, k, attr)
        instance.save()

        return instance

    class Meta:
        lookup_field = 'uuid'
