# Generated by Django 5.0.2 on 2024-02-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_author_genre_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]