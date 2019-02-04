import uuid as g_uuid
import hashlib
from django.db import models


class FileHistory(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    path_file = models.CharField(max_length=1000)
    checksum = models.CharField(max_length=64, unique=True)

    @classmethod
    def create_file_history(cls, path_file, text):
        checksum = hashlib.sha256(text.encode('utf-8')).hexdigest()
        cls.objects.create(path_file=path_file, checksum=checksum)
