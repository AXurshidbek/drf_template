from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if update_fields and "updated_at" not in update_fields:
            update_fields.append("updated_at")

        super().save(force_insert=force_insert,
                     force_update=force_update,
                     using= using,
                     update_fields= update_fields)
