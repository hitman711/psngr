# Generated by Django 2.0.5 on 2018-05-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
