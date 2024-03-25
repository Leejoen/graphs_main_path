from django.db import models

class Count(models.Model):
    count = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Количество'
        verbose_name_plural = 'Количество'

class Edges(models.Model):
    out = models.IntegerField('1')
    to = models.IntegerField('2')
    weight = models.IntegerField('3')

    class Meta:
        verbose_name = 'Ребро'
        verbose_name_plural = 'Ребра'

class Names(models.Model):
    num = models.IntegerField('Номер',primary_key=True)
    name = models.CharField('Название', max_length=100)
    dangerous = models.BooleanField('Опасное сост.')

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'
