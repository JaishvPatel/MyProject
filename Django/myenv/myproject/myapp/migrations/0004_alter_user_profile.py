# Generated by Django 4.2.8 on 2024-01-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(default='', upload_to='profile/'),
        ),
    ]