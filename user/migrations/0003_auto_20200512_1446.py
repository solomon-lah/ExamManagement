# Generated by Django 3.0.5 on 2020-05-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_resulttable'),
    ]

    operations = [
        migrations.AddField(
            model_name='resulttable',
            name='AcceptedByHod',
            field=models.CharField(default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='resulttable',
            name='Compiled',
            field=models.CharField(default='No', max_length=3),
        ),
    ]
