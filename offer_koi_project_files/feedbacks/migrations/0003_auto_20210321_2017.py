# Generated by Django 3.1.7 on 2021-03-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_auto_20210321_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedbacks',
            name='feedback',
            field=models.BooleanField(choices=[(None, ''), (True, 'Good'), (False, 'Bad')], default=None),
        ),
    ]