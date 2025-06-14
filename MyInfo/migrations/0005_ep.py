# Generated by Django 5.2.1 on 2025-05-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyInfo', '0004_alter_management_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='EP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ОП')),
                ('direct', models.CharField(verbose_name='Направление')),
                ('education_material', models.TextField(verbose_name='Что изучают студенты')),
                ('advantage', models.TextField(verbose_name='Преимущества')),
                ('persp', models.TextField(verbose_name='Перспективы')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на ОП')),
            ],
            options={
                'verbose_name': 'ОП',
                'verbose_name_plural': 'ОП',
            },
        ),
    ]
