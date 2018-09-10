# Generated by Django 2.1.1 on 2018-09-09 19:38

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
            name='GithubRepositories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Github Repositories',
            },
        ),
        migrations.CreateModel(
            name='RepositoryContributors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('last_hundred_actions_percent', models.CharField(blank=True, max_length=25, null=True)),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repos.GithubRepositories')),
            ],
            options={
                'verbose_name_plural': 'Repository Contributors',
            },
        ),
    ]
