# Generated by Django 4.2.1 on 2023-05-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('hashed_url', models.CharField(max_length=200)),
                ('use_limit', models.IntegerField(blank=True, null=True)),
                ('used_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'url_detail',
            },
        ),
    ]
