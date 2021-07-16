from django.db import models
from rest_framework.reverse import reverse


class UploadFile(models.Model):
    """Загруженные файлы"""
    upload_name = models.CharField("Название загрузки", max_length=150)
    date_from = models.DateField("Дата первой сделки")
    date_to = models.DateField("Дата последней сделки")
    comment = models.TextField("Комментарий")
    file = models.FileField("Файл", upload_to='csv_files/')

    def __str__(self):
        return str(self.id) + " " + self.upload_name

    #def get_absolute_url(self):
    #    return reverse('file:id', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Загруженный файл"
        verbose_name_plural = "Загуженные файлы"
