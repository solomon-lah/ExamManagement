# Generated by Django 3.0.5 on 2020-05-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LecturerId', models.CharField(max_length=20)),
                ('Class', models.CharField(max_length=12)),
                ('Session', models.CharField(max_length=11)),
                ('Semester', models.CharField(max_length=15)),
                ('CourseCode', models.CharField(max_length=7)),
                ('Units', models.IntegerField()),
                ('ExamSheet', models.FileField(upload_to='result/')),
                ('DateUploaded', models.DateTimeField()),
            ],
        ),
    ]
