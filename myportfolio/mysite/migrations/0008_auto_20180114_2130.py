# Generated by Django 2.0.1 on 2018-01-14 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_project_logo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artimage',
            name='art',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mysite.Art'),
        ),
    ]