# Generated by Django 2.1.3 on 2019-07-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0005_myexperience_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статус',
            },
        ),
    ]
