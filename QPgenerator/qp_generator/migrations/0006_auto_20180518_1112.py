# Generated by Django 2.0.5 on 2018-05-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp_generator', '0005_auto_20180518_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(null=True),
        ),
    ]