# Generated by Django 2.1.3 on 2019-07-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_auto_20190705_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='myeducation',
            name='year',
            field=models.IntegerField(blank=True, default=0, verbose_name='Лет Обучение'),
        ),
    ]