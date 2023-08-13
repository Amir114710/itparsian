from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Ticket(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = RichTextUploadingField(max_length=3000)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'تیکت های سایت'
        verbose_name_plural = 'تیکت های سایت'
