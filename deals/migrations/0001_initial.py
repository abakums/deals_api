# Generated by Django 3.2.5 on 2021-07-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_name', models.CharField(max_length=150, verbose_name='Название загрузки')),
                ('date_from', models.DateField(verbose_name='Дата первой сделки')),
                ('date_to', models.DateField(verbose_name='Дата последней сделки')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('file', models.FileField(upload_to='csv_files/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Загруженный файл',
                'verbose_name_plural': 'Загуженные файлы',
            },
        ),
    ]
