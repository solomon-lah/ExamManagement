# Generated by Django 3.0.5 on 2020-05-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_resulttable_compiledfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulttable',
            name='CompiledFile',
            field=models.CharField(max_length=150, null=True),
        ),
    ]