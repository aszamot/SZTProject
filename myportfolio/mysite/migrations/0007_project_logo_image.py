# Generated by Django 2.0.1 on 2018-01-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_project_projectimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/projects_logo/'),
        ),
    ]
