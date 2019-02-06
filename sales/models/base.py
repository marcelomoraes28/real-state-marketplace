
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseBlank(models.Model):
    def __new__(cls, *args, **kwargs):
        new = super().__new__(cls)
        if hasattr(cls, 'CustomMeta'):
            if hasattr(cls.CustomMeta, 'blank_together'):
                setattr(new, '__blank_together__', cls.CustomMeta.blank_together)
        return new

    def save(self, *args, **kwargs):
        blank_together = not (any([getattr(self, field, None) for field in getattr(self, '__blank_together__', None)]) and \
                              not all([getattr(self, field, None) for field in getattr(self, '__blank_together__', None)]))
        if not blank_together:
            raise ValidationError({field: _('must all be blank or filled together') for field in getattr(self, '__blank_together__', None)})
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
