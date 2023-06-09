# Generated by Django 4.1.2 on 2023-05-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to=''),
        ),
    ]
