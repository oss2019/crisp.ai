# Generated by Django 2.2.1 on 2019-05-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190519_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_image',
            field=models.ImageField(default='media/default.png', upload_to='profile pics'),
        ),
    ]