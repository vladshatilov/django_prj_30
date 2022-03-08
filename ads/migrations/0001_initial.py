# Generated by Django 4.0.2 on 2022-03-07 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=6)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(choices=[('member', 'Member'), ('admin', 'Admin')], default='member', max_length=30)),
                ('age', models.PositiveSmallIntegerField(blank=True)),
                ('locations', models.ManyToManyField(to='ads.City')),
            ],
            options={
                'verbose_name': 'Юзер',
                'verbose_name_plural': 'Юзеры',
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ads.categories')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-price'],
            },
        ),
    ]
