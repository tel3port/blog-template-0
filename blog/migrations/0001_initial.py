# Generated by Django 3.1 on 2020-08-30 04:11

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
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_title', models.CharField(max_length=1000)),
                ('entry_text', models.TextField(max_length=50000)),
                ('entry_tags', models.TextField(max_length=50000)),
                ('site_sub_id', models.CharField(max_length=1000)),
                ('image', models.FileField(blank=True, upload_to='media')),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=5000, null=True, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1)),
                ('entry_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'blog entries',
            },
        ),
    ]