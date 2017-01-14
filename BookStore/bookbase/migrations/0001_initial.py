# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('category', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=b'')),
                ('description', models.TextField()),
                ('price', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('author', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=20)),
                ('age_group', models.IntegerField(default=0)),
                ('genre', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1)),
                ('quantity', models.IntegerField(default=0)),
                ('book', models.ForeignKey(to='bookbase.Book')),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
                ('pincode', models.IntegerField()),
                ('customer', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
