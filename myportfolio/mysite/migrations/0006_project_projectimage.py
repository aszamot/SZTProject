# Generated by Django 2.0.1 on 2018-01-13 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_art_article_artimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('github_url', models.CharField(max_length=200)),
                ('project_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/projects/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Project')),
            ],
        ),
    ]