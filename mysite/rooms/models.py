from django.db import models
from django.urls import reverse


class Rooms(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование комнаты')
    content = models.TextField(verbose_name='Комментария', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Занята')
    teachers = models.ForeignKey('Teachers', on_delete=models.PROTECT, null=True, verbose_name='Учитель')
    time = models.ForeignKey('TimeGr', on_delete=models.PROTECT, null=True, blank=True,  verbose_name='Время')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Teachers(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('teachers', kwargs={"teachers_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учители'


class TimeGr(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Время кружка')

    def get_absolute_url(self):
        return reverse('time', kwargs={"time_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'