# Generated by Django 5.0.1 on 2024-02-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rating_rating_user_alter_rating_rated_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to=''),
        ),
    ]
