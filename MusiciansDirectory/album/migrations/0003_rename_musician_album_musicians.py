# Generated by Django 4.2.8 on 2024-01-17 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='musician',
            new_name='musicians',
        ),
    ]
