# Generated by Django 3.0.5 on 2020-05-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200512_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='resulttable',
            name='CompiledFile',
            field=models.CharField(max_length=50, null=True),
        ),
    ]