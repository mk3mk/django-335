# Generated by Django 5.0.2 on 2024-02-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_post_poster_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.TextField(default=''),
        ),
    ]