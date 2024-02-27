# Generated by Django 5.0.2 on 2024-02-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]