# Generated by Django 4.0.5 on 2022-06-07 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_avatar_alter_customuser_fecebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatar'),
        ),
    ]
