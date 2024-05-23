from django.db import models

class Count(models.Model):
    count = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Количество'
        verbose_name_plural = 'Количество'

class Edges(models.Model):
    out = models.IntegerField('1')
    to = models.IntegerField('2', choices=((None, 'None'), (1, 'Вершина 1'), (2, 'Вершина 2'), (3, 'Вершина 3')))
    weight = models.IntegerField('3')

    def get_absolute_url(self):
        return f'/edges/{self.num}'

    class Meta:
        verbose_name = 'Ребро'
        verbose_name_plural = 'Ребра'

class Names(models.Model):
    num = models.IntegerField('Номер', primary_key=True)
    name = models.CharField('Название', max_length=100)
    dangerous = models.BooleanField('Опасное состояние')

    def get_absolute_url(self):
        return f'/edges/{self.num}'

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'


class Infr(models.Model):
    num = models.IntegerField('Порядковый номер', primary_key=True)
    name = models.TextField('Название', max_length=200)
    description = models.TextField('Корректировка')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктуры'

        