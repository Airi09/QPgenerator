# Generated by Django 2.0.5 on 2018-06-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp_generator', '0018_paper_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]