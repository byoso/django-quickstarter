# Generated by Django 4.1.4 on 2022-12-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='unconfirmed_email',
            field=models.EmailField(db_index=True, max_length=64, null=True),
        ),
    ]