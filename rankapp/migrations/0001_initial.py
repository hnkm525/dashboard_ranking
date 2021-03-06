# Generated by Django 3.1.2 on 2020-10-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(max_length=100)),
                ('post_url', models.CharField(max_length=200)),
                ('title', models.TextField(default='', null=True)),
                ('body', models.TextField(default='', null=True)),
                ('caption', models.TextField(default='', null=True)),
                ('link', models.TextField(default='', null=True)),
                ('source', models.TextField(default='', null=True)),
                ('images', models.ImageField(default='static/default.png', null=True, upload_to='')),
            ],
        ),
    ]
