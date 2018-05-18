# Generated by Django 2.0.5 on 2018-05-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp_generator', '0002_auto_20180518_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default='no answer'),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(null=True, upload_to='question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('mcq', 'Mcq'), ('subjective', 'Subjective'), ('fb', 'fill in the blanks'), ('Tf', 'true or false'), ('Match', 'match the following')], max_length=50),
        ),
    ]
