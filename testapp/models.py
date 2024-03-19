from django.db import models

from import_export.resources import ModelResource


class StringModel(models.Model):
    chars = models.CharField(max_length=255)
    text = models.TextField()


class StringResource(ModelResource):
    class Meta:
        model = StringModel
        fields = [
            "text",
            "chars",
        ]
        export_order = fields
