# Generated by Django 5.0.6 on 2024-06-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='image/', verbose_name='Логотип сайта')),
                ('banner', models.ImageField(upload_to='banner/', verbose_name='Фото баннера')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='instagram')),
            ],
            options={
                'verbose_name': 'Настройка сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]