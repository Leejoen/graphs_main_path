# Generated by Django 5.0.3 on 2024-05-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_names_id_alter_names_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infr',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False, verbose_name='Порядковый номер')),
                ('name', models.TextField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Корректировка')),
            ],
            options={
                'verbose_name': 'Инфраструктура',
                'verbose_name_plural': 'Инфраструктуры',
            },
        ),
        migrations.AlterField(
            model_name='edges',
            name='to',
            field=models.IntegerField(choices=[(None, 'None'), (1, 'Вершина 1'), (2, 'Вершина 2'), (3, 'Вершина 3')], verbose_name='2'),
        ),
        migrations.AlterField(
            model_name='names',
            name='dangerous',
            field=models.BooleanField(verbose_name='Опасное состояние'),
        ),
    ]