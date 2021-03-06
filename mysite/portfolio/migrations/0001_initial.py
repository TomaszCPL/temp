# Generated by Django 2.0.1 on 2018-01-14 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=120)),
                ('slug', models.SlugField(default='', unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=portfolio.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField(default='')),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
