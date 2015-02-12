from django.db import models
from django.conf import settings
from django.db.models.fields.files import FileField
from django.db.models.fields import DateTimeField

UPLOAD_DIRS = getattr(settings, "UPLOADS_DIR", "uploads")

class File(models.Model):
    file = FileField(upload_to=UPLOAD_DIRS)
    created_on = DateTimeField(auto_now_add=True)
    modifed_on = DateTimeField(auto_now_add=True, auto_now=True)