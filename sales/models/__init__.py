from django.core.exceptions import ValidationError
from django.db import models


class BaseBlank(models.Model):
    def __new__(cls, *args, **kwargs):
        new = super().__new__(cls)
        if hasattr(cls, 'CustomMeta'):
            if hasattr(cls.CustomMeta, 'blank_together'):
                setattr(new, '__blank_together__', cls.CustomMeta.blank_together)
        return new

    def save(self, *args, **kwargs):
        # returns False if any but not all of the __blank_together__ fields
        # are not blank
        blank_together = not (any([getattr(self, field, None) for field in getattr(self, '__blank_together__', None)]) and \
                              not all([getattr(self, field, None) for field in getattr(self, '__blank_together__', None)]))
        if not blank_together:
            raise ValidationError(f"{getattr(self, '__blank_together__', None)} must all be blank together.")
        return super().save(*args, **kwargs)


    class Meta:
        # prevents Django from having some bad behavior surrounding
        # inheritance of models that are not explicitly abstract
        abstract = True


class BaseModelMixin(BaseBlank, models.Model):
    pass